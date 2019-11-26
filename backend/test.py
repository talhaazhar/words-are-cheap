import pickle
import numpy as np
from util import read, write

from collections import namedtuple

Record = namedtuple('Record', ['features', 'labels'])


def main():
    test = read("test.rd")
    model = read("model.rd")

    predicted = model.predict(test.features[0])
    print np.mean(predicted == test.labels)



if __name__ == '__main__':
    main()
