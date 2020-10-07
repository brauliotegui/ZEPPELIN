""" This is the main module to run the program.

It accepts three outputs:
 1. Name of the first artist
 2. Name of the second artist
 3. The lyrics that the user wants to predict
 If the csv file of the artist's lyrics doesnt exist the program scrape it and
 save it as a csv file and train a naive bayes model to predict the artitst of
 the given lyrics
 """
from scrape_lyrics import save_all_lyrics
from create_lyricscorpus import create_corpuslist
from model import predict


if __name__ == '__main__':
    print("Please enter the url of the first artist's lyrics page from lyrics.com:\n")
    URL_1 = input()
    print("Please enter the directory you want to save these lyrics:")
    print("Example: /Users/braulio/Documents/Funkadelic/ \n")
    DIRECTORY_1 = input()
    print("Please enter the artist name:\n")
    ARTIST_1 = input()
    save_all_lyrics(URL_1, DIRECTORY_1)
    create_corpuslist(DIRECTORY_1, ARTIST_1)
    print("Now enter the url of the second artist's lyrics page from lyrics.com:\n")
    URL_2 = input()
    print("Enter a different directory you want to save these lyrics:")
    print("Example: /Users/braulio/Documents/Funkadelic/ \n")
    DIRECTORY_2 = input()
    print("Now enter the name of the second artist:\n")
    ARTIST_2 = input()
    save_all_lyrics(URL_2, DIRECTORY_2)
    create_corpuslist(DIRECTORY_2, ARTIST_2)

    print("\nWrite a song that you want to predict or write END to finish:\n")
    NEW_TEXT = input()
    while NEW_TEXT != "END":
        predict(NEW_TEXT)
        print("Write another song that you want to predict or write END to finish:\n")
        NEW_TEXT = input()
    if NEW_TEXT == "END":
        print("Thank you and see you soon!")
