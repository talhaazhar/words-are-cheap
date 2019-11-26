import pickle


def read(file_name):
    with open(file_name, "rb") as f:
        return pickle.load(f)


def write(file_name, data):
    with open(file_name, "wb") as f:
        pickle.dump(data, f)