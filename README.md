# ZEPPELIN
A python program that scrapes lyrics from any artist on lyrics.com and train a lyrics predictor model to predict the artist of a given lyrics text.

## Usage
python predictor.py

## Description
The program starts by asking the user to enter the url, directory and names of two artists and then it scrapes lyrics of the given artists from wwww.lyrics.com and merge and save them as a list. Then, after vectorizing the lyrics, a Naive Bayes model will be trained on lyrics corpus list by using the name of the artists as the target. Finally, the user can enter any new lyrics from either artist and the model will predict the name of the artist of that song/text.

## Used tech
- Python
- requests
- BeautifulSoup
- pandas
- scikit-learn

## Scripts
- **predictor.py:** The main py file to run the program.
- **scrape_lyrics.py:** scrapes lyrics from an arist page on www.lyrics.com using requests and BeautifulSoup and saves them as text files in the specified directory.
- **create_lyricscorpus.py:** Extract all text files from a selected directory and add into a list.
- **model:** This program vectorizes the lyrics list using TfidVectorizer and creates a Dataframe with artist label list as index. In addition, it trains a Multinominal Naive Bayes model on the vectorized lyrics to predict the name of the artist for new text given by the user.
