import pickle
def save_dictionary(dictionary, filepath):
    with open(filepath, 'wb') as file:
        pickle.dump(dictionary, file)
def load_dictionary(filepath):
    with open(filepath, 'rb') as file:
        return pickle.load(file)    