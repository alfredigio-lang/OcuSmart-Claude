"""Descriptive research arithmetic. No clinical classifications or privacy detection.
Input JSON via stdin, exact schemas:
{"op":"se","sphere":-2,"cylinder":-1}
{"op":"interval","before":80,"after":78,"elapsed_days":365.25,"comparable":true}
{"op":"trend","time_years":[0,1,2],"values":[80,79,78],"comparable":true}
{"op":"osdi","scores":[0,1,null,2,3,4,0,1,2,3,4,0]}
Only pass privacy-cleared numbers. Unknown fields are rejected. No file/network writes.
OLS slope is descriptive, with no p-value, progression verdict or forecast.
"""
import json
import math
import sys


def number(x):
    if isinstance(x, bool) or not isinstance(x, (int, float)) or not math.isfinite(x):
        raise ValueError('Finite numeric inputs required')
    return float(x)


def calculate(d):
    if not isinstance(d, dict):
        raise ValueError('Object required')
    schemas = {'se': {'op','sphere','cylinder'},
               'interval': {'op','before','after','elapsed_days','comparable'},
               'trend': {'op','time_years','values','comparable'},
               'osdi': {'op','scores'}}
    op = d.get('op')
    if not isinstance(op,str) or op not in schemas or set(d) != schemas[op]:
        raise ValueError('Unknown operation or mismatched fields')
    if op in ('interval','trend') and d['comparable'] is not True:
        raise ValueError('Comparability must be established before calculation')
    if op == 'se':
        out = {'spherical_equivalent_D': number(d['sphere']) + number(d['cylinder']) / 2}
    elif op == 'interval':
        days = number(d['elapsed_days'])
        if days <= 0:
            raise ValueError('Elapsed days must be positive')
        change = number(d['after']) - number(d['before'])
        out = {'signed_change': change, 'annualized_signed_change': change * 365.25 / days,
               'note': 'Descriptive annualization, not a forecast; input units retained'}
    elif op == 'trend':
        if not isinstance(d['time_years'],list) or not isinstance(d['values'],list):
            raise ValueError('Arrays required')
        t = [number(x) for x in d['time_years']]
        v = [number(x) for x in d['values']]
        if len(t) != len(v) or len(t) < 3:
            raise ValueError('At least three paired observations required')
        if any(b <= a for a,b in zip(t,t[1:])):
            raise ValueError('Times must be strictly increasing')
        mt,mv = sum(t)/len(t),sum(v)/len(v)
        den = sum((x-mt)**2 for x in t)
        slope = sum((x-mt)*(y-mv) for x,y in zip(t,v))/den
        out = {'n':len(t),'slope_per_year':slope,'intercept':mv-slope*mt,
               'note':'Descriptive unweighted OLS only; no significance, clinical classification or forecast'}
    else:
        scores = d['scores']
        if not isinstance(scores,list) or len(scores) != 12:
            raise ValueError('Exactly 12 item slots required, null for unanswered/not applicable')
        valid = []
        for x in scores:
            if x is None:
                continue
            y = number(x)
            if y not in (0,1,2,3,4):
                raise ValueError('Item scores must be integers 0 to 4 or null')
            valid.append(y)
        if not valid:
            raise ValueError('No answered items')
        out = {'score':sum(valid)*25/len(valid),'answered_items':len(valid),
               'note':'Arithmetic only; missingness and questionnaire applicability require review'}
    out['use'] = 'Experimental research/education only; not for clinical use'
    return out


def reject_duplicates(pairs):
    d = {}
    for k,v in pairs:
        if k in d:
            raise ValueError('Duplicate JSON keys rejected')
        d[k] = v
    return d


if __name__ == '__main__':
    try:
        data = json.load(sys.stdin, object_pairs_hook=reject_duplicates)
        print(json.dumps(calculate(data), allow_nan=False))
    except (ValueError, TypeError, OverflowError, ZeroDivisionError):
        print(json.dumps({'error':'Invalid or non-comparable input; calculation not performed'}))
        sys.exit(2)
