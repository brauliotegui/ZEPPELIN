'''extract all text files from a selected directory and add into a list '''
import os

CORPUS = []
LABEL = []

def create_corpuslist(directory, artist_name):
    """
    Create a list out of every song lyrics downloaded.

    Parameters
    ----------
    Directory = the directory where you want to get all files from and storage the text
    in the corpus list.Directory must be passed as a string,
    artist_name = name of the artist, must be passed as string

    Returns
    -------
    a list, in which each item is a song lyric corpus, and a list with the artist name.

    """
    #LOOP FOR ADDING LYRIC FILES INTO A LIST
    list = os.listdir(directory)
    list_size = len(LABEL)  #original size

    for i in list:
        title = list[i]
        LABEL.append(artist_name)

        with open(directory + title, 'r') as reader:
            doc = reader.read()
            doc.lower()
            doc.split()
            CORPUS.append(doc)


    print(artist_name, (len(LABEL) - list_size))
    print('Do we have as many song lyrics as artist indices?: ' + str(len(CORPUS) == len(LABEL)))
