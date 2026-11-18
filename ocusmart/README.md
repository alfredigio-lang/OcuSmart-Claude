# OcuSmart for Claude

OcuSmart is an advanced research platform in generative artificial intelligence applied to ophthalmology. It brings specialist scientific reasoning, exploratory imaging review (OCT, fundus, visual fields, corneal tomography, OCT-A), longitudinal research, oculomics, bibliographic verification (TrueRef) and specialist teaching (Academy) into a single Claude environment, with explicit methodological and privacy safeguards.

Scientific direction: Dr. Alfredo Di Giovanni.

**OcuSmart is free and intended exclusively for eye-care professionals and researchers, not for patients.** It is experimental, not clinically validated, and not for diagnosis, screening, treatment, surgery or patient-care decisions. Submit only previously anonymized material: OcuSmart stops when it detects or cannot exclude identifying information.

## How to use it

In the Claude app, add OcuSmart from the plugin directory (Customize → Plugins → Discover). In Claude Code:

```
/plugin install ocusmart --marketplace alfredigio-lang/OcuSmart-Claude
```


After adding the plugin, write **"Start OcuSmart"** (or "Avvia OcuSmart") in any chat and describe your question in your own words. In Claude Code the commands `/ocusmart`, `/trueref`, `/academy` and `/longitudinal` are also available.

## What it runs, sends and stores

- **Instructions only.** The plugin consists of skill and command instructions. It contains no hooks, no MCP servers, no agents and no background processes.
- **Web access.** When the user asks for literature or bibliography verification, OcuSmart uses Claude's own web search and fetch to consult public sources such as PubMed, Crossref, DOI resolvers and publisher pages. Only general scientific terms or bibliographic metadata are sent; patient narratives, case data, files and images are never included in searches.
- **Calculation.** `skills/ocusmart/references/research-math.md` gives the formulas for descriptive arithmetic (spherical equivalent, interval change, linear trend, OSDI score) and a reference implementation that Claude runs in its own code-execution environment when available. It writes no files and makes no network calls. The plugin contains no executable files.
- **No data collection.** OcuSmart has no server, database, analytics or telemetry. It does not store case material, does not write to Claude's memory and sends nothing to its author or to third parties.

## Licence

MIT. See `LICENSE`.
