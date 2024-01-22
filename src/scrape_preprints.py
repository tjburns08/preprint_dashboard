from paperscraper.get_dumps import biorxiv, medrxiv, chemrxiv

# The whole thing
chemrxiv()  #  Takes ~45min and should result in ~20 MB file
medrxiv()  #  Takes ~30min and should result in ~35 MB file
biorxiv()  # Takes ~1h and should result in ~350 MB file

# By date
#biorxiv(begin_date="2024-01-01", end_date="2024-01-21")
#medrxiv(begin_date="2024-01-01")
#chemrxiv(begin_date="2024-01-01")

# Experimental: the whole thing
#paperscraper.get_dumps(".*")