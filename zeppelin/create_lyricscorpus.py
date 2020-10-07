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
    files_list = os.listdir(directory)

    for i in range(len(files_list)):
        title = files_list[i]
        LABEL.append(artist_name)

        with open(directory + title, 'r') as reader:
            doc = reader.read()
            doc.lower()
            doc.split()
            CORPUS.append(doc)


    assert len(CORPUS) == len(LABEL)
