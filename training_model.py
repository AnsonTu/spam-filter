import numpy as np
from scipy.sparse import csr_matrix

NUM_OF_TRAINING_DOCS = 100
NUM_OF_TOKENS = 2500

training_data_contents = open("training-data.txt", "r")
formatted_test_data = []
while 1:
    line = training_data_contents.readline()
    if not line:
        break
    line = line.split()
    formatted_test_data.append(line)
test_data_matrix = csr_matrix((formatted_test_data[:, 2], (formatted_test_data[:, 0], formatted_test_data[:, 1])), shape=(NUM_OF_TRAINING_DOCS, NUM_OF_TOKENS))

training_labels_contents = open("training-labels.txt", "r")
formatted_label_data = []
while 1:
    line = training_labels_contents.readline()
    if not line:
        break
    formatted_label_data.append(line)
spam_indexes = np.argwhere(training_labels_contents != 0)
non_spam_indexes = np.argwhere(training_labels_contents == 0)

length_of_emails = []
for i in test_data_matrix:
    length_of_emails.append(sum(test_data_matrix[i]))

spam_word_count = None
for i in spam_indexes
    spam_word_count += length_of_emails[i]
non_spam_word_count = None
for i in non_spam_indexes
    spam_word_count += length_of_emails[i]

token_spam = []

spam_probability = []
token_spam / (spam_word_count + NUM_OF_TOKENS)
token_non_spam = []

non_spam_probability = []
token_non_spam / (non_spam_word_count + NUM_OF_TOKENS)

training_data_contents.close()
training_labels_contents.close()