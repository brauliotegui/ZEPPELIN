#!/usr/bin/env python

"""Tests for `zeppelin` package."""

import pytest
import os.path
from zeppelin.scrape_lyrics import save_all_lyrics
from zeppelin.create_lyricscorpus import create_corpuslist
from zeppelin.model import vectors_and_df
from zeppelin.model import predict

# decorators to get the links
@pytest.fixture
def link():
    url = 'https://www.lyrics.com/artist/Koffee/3491656'
    url, directory = save_all_lyrics(url, 'Koffee')
    return directory


@pytest.fixture
def link_2():
    url = 'https://www.lyrics.com/artist/MF-Doom/300089'
    url, directory = save_all_lyrics(url, 'MFDOOM')
    return directory

# test generating correct numbers of sub-directories
PASSING_CONDITIONS = ['https://www.lyrics.com/artist/Koffee/3491656',
 'https://www.lyrics.com/artist/MF-Doom/300089',
 'https://www.lyrics.com/artist/Danger-Doom/742954']

PASSING_CONDITIONS2 = ['Koffee', 'MF DOOM', 'Danger Doom']

@pytest.mark.parametrize("url", PASSING_CONDITIONS, "name", PASSING_CONDITIONS2)
def test_save_all_lyrics(url, name):
    url, name = save_all_lyrics(url, name)
    files_list = os.listdir('lyrics-files/')
    assert len(files_list) == 3

# test if the corpus lists have correct size
def test_create_corpuslist(name):
    assert len(CORPUS) == len(LABEL)

# test the possible outcomes of the predictions and the merge and train function
def test_model():
    df, vectorizer = vectors_and_df(CORPUS, LABEL)
    prediction = predict("ANY LYRICS")
    assert prediction == ['Koffee'] or prediction == ['MF DOOM']
