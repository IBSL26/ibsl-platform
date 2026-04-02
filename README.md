# IBSL Strategy2Result® Digital Platform

## Folder Structure

```
ibsl-platform/
├── index.html              Landing page + authentication
├── assets/
│   ├── logo.png            IBSL badge logo (transparent background)
│   └── style.css           Shared styles used across all pages
├── facilitator/
│   └── unit1.html          Unit 1 — Facilitator control view (all 6 modules)
├── participant/
│   └── unit1.html          Unit 1 — Participant guided journey (reflections)
└── api/
    └── README.md           Backend schema — ready for database integration
```

## Access Codes

### Facilitator Portal
IBSL-FAC-2025 · FAC-LEAD-001 · S2R-CTRL-77 · IBSL-SYNTH-F · FACILITATOR-X

### Participant Portal
IBSL-S2R-2025 · S2R-PART-001 · CESI-JOIN-42 · IBSL-GUIDE-P · PARTICIPANT-X

All codes expire 90 days from first use. Contact: info@ibsleadership.com

## Deployment (GitHub Pages)

1. Push this folder to a GitHub repository
2. Settings → Pages → Deploy from branch → main
3. Live at: https://[username].github.io/ibsl-platform

## Adding Unit 2–4 files

Copy the structure of unit1.html into:
- facilitator/unit2.html
- participant/unit2.html

Update the portal view in index.html to link to the new files.
