# Preprint Dashboard for BioRxiv, MedRxiv, and ChemRxiv

# Description
This project scrapes the entire corpus of biorxiv, medrxiv, and chemrxiv preprints (with updating as needed), and visualizes it as an interactive table in a Dash web app.

# Instalation
Clone this repository

```bash
git clone https://github.com/tjburns08/preprint_dashboard/tree/main/src/scraping_preprints
```

Install the necessary requirements

```bash
pip install -r requirements.txt
```
# Usage

## Setup

Create a data directory. My current convention is that I have a "latest" subdirectory within that. This is where the scraped jsonl files will go.