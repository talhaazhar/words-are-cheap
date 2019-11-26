import pickle
from util import read, write
from random import shuffle
import os.path


def main():    
    sub3 = None

    sub1 = read("sub1.raw")
    sub2 = read("sub2.raw")
    if(os.path.isfile("sub3.raw")):
        sub3 = read("sub3.raw")


    r1_training, r1_development, r1_tests = split(sub1)
    r2_training, r2_development, r2_tests = split(sub2)
    r3_training, r3_development, r3_tests = split(sub3)


    training = r1_training + r2_training + r3_training
    shuffle(training)
    
    development = r1_development + r2_development + r3_development
    shuffle(development)

    tests = r1_tests + r2_tests + r3_tests
    shuffle(tests)

    write("train.raw", training)
    write("develop.raw", development)
    write("test.raw", tests)


def split(data):
    n = len(data)

    training = data[:n/2]
    development = data[n/2:][:n/4]
    tests = data[n/2:][n/4:]

    return training, development, tests


if __name__ == '__main__':
    main()