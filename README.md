# OcuSmart for Claude

Public Claude plugin marketplace for **OcuSmart** — experimental ophthalmology research and education (anonymized material only; not clinically validated; not for patient care).

## Use it in the Claude app (no technical skills needed)

**OcuSmart is free and intended exclusively for eye-care professionals and researchers, not for patients.** The plans below are Claude subscriptions; they only decide how you add OcuSmart.

**Option A — paid Claude plans (Claude Pro, Max, Team, Enterprise):**
1. In Claude, open **Customize** in the left sidebar → **Plugins**.
2. Click **Add** → **Add marketplace** and enter `alfredigio-lang/OcuSmart-Claude`.
3. Add **OcuSmart**, then in any chat write: *Start OcuSmart*.

**Option B — any Claude plan, including the free Claude plan:**
1. Download **[ocusmart-skill.zip](https://github.com/alfredigio-lang/OcuSmart-Claude/raw/main/dist/ocusmart-skill.zip)** (do not unzip it).
2. Make sure **code execution and file creation** is on (Settings → Capabilities).
3. Open **Customize** → **Skills** → **+** → **Create skill** → **Upload a skill**, and choose the zip.
4. In any chat write: *Start OcuSmart*.

## Install (Claude Code)
```
/plugin install ocusmart --marketplace alfredigio-lang/OcuSmart-Claude
```
Or in two steps:
```
/plugin marketplace add alfredigio-lang/OcuSmart-Claude
/plugin install ocusmart@ocusmart
```
Commands: `/ocusmart`, `/trueref`, `/academy`, `/longitudinal`.

Scientific direction: Dr. Alfredo Di Giovanni.

## License
MIT — see LICENSE.
