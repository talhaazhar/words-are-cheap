from collections import namedtuple
import pickle
from util import read, write

from nltk.corpus import wordnet 



Record = namedtuple('Record', ['features', 'labels'])


def main():
    train_raw = read("train.raw")
    develop_raw = read("develop.raw")
    test_raw = read("test.raw")

    train_data, train_labels = vectorize(train_raw)
    develop_data, develop_labels = vectorize(develop_raw)
    test_data, test_labels = vectorize(test_raw)

    train_recrod = Record(features(train_data), train_labels)
    develop_recrod = Record(features(develop_data), develop_labels)
    test_recrod = Record(features(test_data), test_labels)

    write("train.rd", train_recrod)
    write("develop.rd", develop_recrod)
    write("test.rd", test_recrod)



def vectorize(raw_data):
    data = [row[0] for row in raw_data]
    labels = [row[1] for row in raw_data]
    return data, labels

def features(data):
    f1 = list()
    for comment in data:
        f1.append(simplify(comment.body))
    return [f1,]


def simplify(string):
    string = ' '.join(string.split())
    string = ''.join([i if ord(i) < 128 else ' ' for i in string])
    string = string.lower()
    exclude = set(r".',-(){}[]`!")
    string = ''.join(ch for ch in string if ch not in exclude)
    string = string.encode('ascii', 'ignore')
    #string = ' '.join(syn(word) for word in string.split())
    return string

def syn(word):
    try:
        s = wordnet.synsets(word)[0].lemmas()[0].name()
        return s
    except:
        return word



if __name__ == '__main__':
    main()