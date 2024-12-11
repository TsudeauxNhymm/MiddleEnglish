# MiddleEnglish
A small collection of code designed for use with Middle to Early Modern English

The scraper will scrape from the Oxford University website that hosts Early English Books Online. Just run "python scraper.py" in your terminal, and it should take about three days to scrape all the books.

The cleaner file will change the books from html format to txt, and a few other things.

Lastly, the vectorizer will turn the text files into files that contain a vector of word counts, which can then be used by the MLAgePredictor Jupyter file to train and predict the dacade in which a document was written.

Also included are the visualizations used, and a powerpoint presentation used to present the preliminary results of this invesigation.
