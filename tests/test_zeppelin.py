#!/usr/bin/env python

"""Tests for `zeppelin` package."""
import pytest
import os.path
from ZEPPELIN.zeppelin import scrape_lyrics
from ZEPPELIN.zeppelin import create_lyricscorpus
from ZEPPELIN.zeppelin import model

# decorators to get the links
@pytest.fixture
def link():
    url = 'https://www.lyrics.com/artist/Koffee/3491656'
    url, directory = scrape_lyrics.save_all_lyrics(url, 'Koffee')
    return directory


@pytest.fixture
def link_2():
    url = 'https://www.lyrics.com/artist/MF-Doom/300089'
    url, directory = scrape_lyrics.save_all_lyrics(url, 'MFDOOM')
    return directory

# test generating correct numbers of sub-directories
PASSING_CONDITIONS = ['https://www.lyrics.com/artist/Koffee/3491656',
 'https://www.lyrics.com/artist/MF-Doom/300089',
 'https://www.lyrics.com/artist/Danger-Doom/742954']

NAME = ['Koffee', 'MF DOOM', 'Danger Doom']

@pytest.mark.parametrize("url", PASSING_CONDITIONS, "name", PASSING_CONDITIONS2)
def test_save_all_lyrics(url, name):
    url, name = scrape_lyrics.save_all_lyrics(url, name)
    files_list = os.listdir('lyrics-files/')
    assert len(files_list) == 3

# test if the corpus lists have correct size
def test_create_corpuslist(name):
    create_lyricscorpus.create_corpuslist(NAME)
    assert len(CORPUS) == len(LABEL)

# test the possible outcomes of the predictions and the merge and train function
def test_model():
    df, vectorizer = model.vectors_and_df(CORPUS, LABEL)
    prediction = model.predict("ANY LYRICS")
    assert prediction == ['Koffee'] or prediction == ['MF DOOM']
