import pickle
from collections import namedtuple

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

import numpy as np

from util import read, write

Record = namedtuple('Record', ['features', 'labels'])


def main():
    train = read("train.rd")
    develop = read("develop.rd")

    text_clf = Pipeline([('vect', CountVectorizer()),
                         ('tfidf', TfidfTransformer()),
                         ('clf', SVC())
    ])

    text_clf = text_clf.fit(train.features[0], train.labels)

    write("model.rd", text_clf)

    predicted = text_clf.predict(develop.features[0])

    print np.mean(predicted == develop.labels)



if __name__ == '__main__':
    main()