# MoRE-GS project website

Static project website for **MoRE-GS: Motion-Regime Experts for Future Gaussian
Splatting**. The design is intentionally buildless so the same `dist/` folder
can be deployed through GitHub Pages or another static host.

## Local preview

```bash
python -m http.server 8000 --directory dist
```

Open `http://localhost:8000`.

## Validate

```bash
python scripts/validate_site.py
```

## GitHub Pages

The included workflow publishes `dist/` whenever `main` is updated. In the
GitHub repository settings, select **GitHub Actions** as the Pages source.

Expected repository name: `MoRE-GS-website`  
Expected URL: `https://advanced-vision-and-learning-lab.github.io/MoRE-GS-website/`

The code button targets
`https://github.com/advanced-vision-and-learning-lab/MoRE-GS`. If the final
organization or repository name changes, update the three code links in
`dist/index.html` before publication.

