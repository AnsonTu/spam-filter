from get_dictionary_list import *
import os

# Get dictionary.txt in form of a dictionary data structure
dict_list = dictionaryList()

feature = [0] * 3
label = [0] * 1


def read_folder(d, out_features, out_labels, docID):

    # Check if out file for features exists
    if os.path.exists(out_features):
        append_write = 'a'
    else:
        append_write = 'w'

    # Check if out file for labels exists
    if os.path.exists(out_labels):
        append_write = 'a'
    else:
        append_write = 'w'

    spam = 1

    # If reading from nonspam folder we set it to 0
    if "nonspam" in d:
        spam = 0

    # open output files accordingly
    f1 = open(out_features, append_write)
    f2 = open(out_labels, append_write)

    # iterate thru files in folder
    for root, dirs, files in os.walk(d):
        for filename in files:

            # Create path
            path = d + '/' + filename

            # Open file for reading
            file = open(path, "r")

            # read content in file
            data = file.read()

            f2.write(str(spam) + '\n')

            # look if email contains words in dictionary.txt
            for key, word in dict_list.items():
                occurrences = data.count(word)
                if occurrences > 0:

                    # Set number set [docID, word-key, occurrences]
                    feature[0] = docID
                    feature[1] = key
                    feature[2] = occurrences

                    # Format string by deleting brackets and commas
                    line = str(feature)[1:-1]
                    f1.write(line.replace(",","") + '\n')

            docID += 1

    # return docID in order to keep track of train files and test files
    return docID


if __name__ == "__main__":

    # Set doc ID to start at 1
    docID_train = 1

    # Set variables for reading files in nonspam-train
    d1 = r'data/nonspam-train'

    # Output files after reading
    f1 = "train-features.txt"
    f2 = "train-labels.txt"

    docID_train = read_folder(d1, f1, f2, docID_train)

    # Set variable to read spam-train folder
    d2 = r'data/spam-train'
    read_folder(d2, f1, f2,docID_train)

    # Set doc ID to start at 1
    docID_test = 1

    # Set variables to read nonspam-test folder
    d3 = r'data/nonspam-test'

    # Output file names after reading
    f3 = "test-features.txt"
    f4 = "test-labels.txt"
    docID_test = read_folder(d3, f3, f4, docID_test )

    # Set variables to read spam-test folder
    d4 = r'data/spam-test'
    read_folder(d4, f3, f4, docID_test )

