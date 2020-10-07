'''This program vectorizes the CORPUS lyrics list and creates a Dataframe with
    artist LABEL list as index. Then the model is trained on the dataframe.
'''

import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

import create_lyricscorpus as clc

def vectors_and_df(corpus, label):
    """creates vectors for songs and returns dataframe with songs as word vectors
    by all artists"""

    tf_vec = TfidfVectorizer(stop_words="english")
    tf_vec.fit(corpus)
    corpus_vecs = tf_vec.transform(corpus)

    return pd.DataFrame(corpus_vecs.todense(), index=label,
                        columns=tf_vec.get_feature_names()), tf_vec


def predict(new_text):

    """
    Takes the pre-trained model pipeline and predicts new artist based on unseen text.

    Parameters
    ----------
    model : Trained scikit-learn model pipeline.
    new_text : str

    Returns
    ---------
    prediction : str

    """
    df, cv = vectors_and_df(clc.CORPUS, clc.LABEL)
    X = df
    y = df.index

    model = MultinomialNB(alpha=0.005)
    model.fit(X, y)

    songlyrics = [new_text]
    # transform song into vector matrix
    new_song_vecs = cv.transform(songlyrics)
    ynew = new_song_vecs.todense()

    prediction = model.predict(ynew)
    print(f"This song belongs to {prediction}")

    return prediction[0]
