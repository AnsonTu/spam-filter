import numpy as np

NUM_OF_TRAINING_DOCS = 700
NUM_OF_TOKENS = 2500

train_data = []
train_data_file = open("train-features.txt", "r")
while 1:
    line = train_data_file.readline().split()
    if not line:
        break
    train_data.append(line)
train_data = np.array(train_data, dtype=int)

formatted_train_data = np.zeros((NUM_OF_TRAINING_DOCS, NUM_OF_TOKENS))
for i in range(len(train_data)):
    row = train_data[i][0] - 1
    column = train_data[i][1] - 1
    data = train_data[i][2]
    formatted_train_data[row][column] = data

train_labels_file = open("train-labels.txt", "r")
train_labels = []
while 1:
    line = train_labels_file.readline().split()
    if not line:
        break
    train_labels.append(int(line[0]))
train_labels = np.array(train_labels)

spam_indexes = np.argwhere(train_labels != 0)
nonspam_indexes = np.argwhere(train_labels == 0)

length_of_emails = np.sum(formatted_train_data, axis=1)

spam_word_count = sum(length_of_emails[spam_indexes])
nonspam_word_count = sum(length_of_emails[nonspam_indexes])

spam_probability = (np.sum(formatted_train_data[spam_indexes]) + 1) / (spam_word_count + NUM_OF_TOKENS)
nonspam_probability = (np.sum(formatted_train_data[nonspam_indexes]) + 1) / (nonspam_word_count + NUM_OF_TOKENS)

train_data_file.close()
train_labels_file.close()

