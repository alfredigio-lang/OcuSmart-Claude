# OcuSmart for Claude (v0.2.0)

Experimental ophthalmology research and education for professionals, using previously anonymized material only.
Scientific direction: Dr. Alfredo Di Giovanni. Not clinically validated; not for diagnosis, screening, treatment, surgery or patient-care decisions.

## Install
Claude Code: `/plugin marketplace add <path-or-repo>` then `/plugin install ocusmart`, or load locally with `claude --plugin-dir ./ocusmart`.

## Commands
- `/ocusmart [question]` — entry point (privacy gate + routing)
- `/trueref [references]` — bibliography verification via real retrieval
- `/academy [topic]` — specialist lessons on fictional cases
- `/longitudinal [data]` — serial-measurement research with executed arithmetic

## Layout
`skills/ocusmart/SKILL.md` (gates, workflow, routing) · `references/` (privacy, imaging, specialties, longitudinal, oculomics, evidence, documentation, academy) · `scripts/research_math.py` (descriptive arithmetic, stdin/stdout JSON).

Everything runs on Claude alone: no external clinical server, no second model, no patient archive.
