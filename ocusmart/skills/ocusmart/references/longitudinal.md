# Longitudinal research

Apply both gates. Use relative elapsed times supplied by the professional, never request birth dates or exact case dates. Do not retain a patient registry. An anonymized case record may be reconstructed only from currently available permitted material.

1. Build a table of source, eye, relative time, parameter, raw value, unit, device/method, quality and reported intervention exposure. Do not merge eyes or assume matching scan locations.
2. Check ordering, duplicates, missingness, scale/unit consistency, calibration and comparability. Distinguish unreliable from excluded and record the reason. Do not fill missing values implicitly.
3. Quantify descriptive changes on comparable measures. Separate endpoint change, interval rate, fitted trend and forecast. Short-interval annualization is a descriptive extrapolation, not a prediction.
4. Inspect repeated versus isolated changes, floor/ceiling effects, testing strategies, learning, segmentation, treatment timing and measurement noise when pertinent.
5. Report concordance, discordance or insufficient evidence with the observations supporting it. Non-significance is not stability and a straight line is not proof of progression.

Use scripts/research_math.py via Python for supported arithmetic on privacy-cleared numeric inputs only. It accepts JSON on stdin, returns JSON on stdout, writes no files and makes no network calls. Commands: se, interval, trend, osdi. Read its schema in the file before use. It has no privacy detector and must not receive raw files or identifiers. Host execution must actually be available. Never claim this script is a clinical algorithm.

For glaucoma, compare structure and function topographically where supported, accounting for sector/hemifield mapping and sampling. Do not predict a new acceleration or a personal risk from a narrative heuristic. Advanced statistical models are research candidates requiring enough observations, explicit assumptions and comparison with a prespecified baseline. Do not force Lorenz/GARCH/fractal models, assume their superiority or hide their provenance.

For myopia, preserve refraction method/cycloplegia, axial-length device and separate eyes. SE = sphere + cylinder/2. Report signed changes; increasing myopia usually yields a negative SE difference. Do not use unsigned thresholds accidentally. Do not apply fixed progression labels to all ages. No default atropine concentration or treatment escalation.

For corneal ectasia, compare same-device comparable maps, acquisition quality and repeatability; do not treat a Kmax difference alone as a definitive progression or CXL indication. For anti-VEGF research, separate functional/anatomic endpoints and recorded exposure; do not infer response causality or treatment failure from one change. No injection or visit scheduling.

Forecasting research: require a stated target, prediction horizon, data cutoff, model specification and evaluation protocol. Prevent future-data leakage and patient-level split contamination. Distinguish exploratory scores from calibrated probabilities. Export descriptive data/plots only with limitations and experimental labeling; never alter an input to make a result look clinically convincing.
