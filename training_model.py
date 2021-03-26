import numpy as np

NUM_OF_TRAINING_DOCS = 700
NUM_OF_TOKENS = 2500

train_data = np.zeros((NUM_OF_TRAINING_DOCS, NUM_OF_TOKENS))
with open("train-features.txt", "r") as train_data_file:
    for i,line in enumerate(train_data_file):
        l = line.split()
        row = int(l[0])
        col = int(l[1])
        val = int(l[2])
        train_data[row-1][col-1] = val

train_labels = []
with open("train-labels.txt", "r") as train_labels_file:
    for i,line in enumerate(train_labels_file):
        l = line.split()
        train_labels.append(l)
train_labels = np.array(train_labels, dtype=int)

spam_indexes = np.argwhere(train_labels != 0)
nonspam_indexes = np.argwhere(train_labels == 0)

length_of_emails = np.sum(train_data, axis=1)

spam_word_count = sum(length_of_emails[spam_indexes[:,0]])
nonspam_word_count = sum(length_of_emails[nonspam_indexes[:,0]])

spam_probability = (np.sum(train_data[spam_indexes[:,0]],axis=0)+1) / (spam_word_count + NUM_OF_TOKENS)
nonspam_probability = (np.sum(train_data[nonspam_indexes[:,0]],axis=0)+1) / (nonspam_word_count + NUM_OF_TOKENS)
