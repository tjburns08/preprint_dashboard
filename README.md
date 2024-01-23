# Preprint Dashboard for BioRxiv, MedRxiv, and ChemRxiv

# Description
This project uses the [paperscraper](https://github.com/PhosphorylatedRabbits/paperscraper) python package to scrape the entire corpus of biorxiv, medrxiv, and chemrxiv preprints (with updating as needed), and visualizes it as an interactive table in a Dash web app.

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

## Scraping
Create a "data" directory, and in there create a "latest" subdirectory. In it will go three files: biorxiv.jsonl, chemrxiv.jsonl and medrxiv.jsonl. You have two options as to where you get those files. The first is to simply scrape_preprints.py, which will detect that the directory does not contain the respective files and scrape the pre-prints from the beginning. However, this is a slow process. The second option is made possible by the benevolence of AstroWaffleRobot in [this comment thread](https://github.com/PhosphorylatedRabbits/paperscraper/issues/33) in the paperscraper package. In short, the most recent jsonl files are on their s3 bucket. This is how I got the data the first time.

Otherwise, if you run scrape_preprints.py, it will detect the most recent date of any preprint in each json file, and start the scraping with that begin date.

## Using the web app
Once you have the data where it's supposed to be, run preprint_dashboard.py. This will combine the data, convert it into a dataframe, and convert that into an interactive Dash table. When you run the script, an local URL will show up in the command line. Go there on your browser of choice, and you'll get to the app, where you should see a table, front and center. If you scroll to the bottom, you'll see that it's organized in pages, as opposed to the [infinite scroll](https://tjburns08.github.io/scrolling_problem.html). You'll also see a row underneath the row with column names. There, you can filter any column by anything you type in.

