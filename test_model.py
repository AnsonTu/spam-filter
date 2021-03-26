import numpy as np
import math
from training_model import spam_indexes, spam_probability, nonspam_probability

# constants
NUM_TEST_EMAILS = 260 
NUM_TEST_SPAM = 130
NUM_WORDS = 2500

# read test-features and make into Nx3 array

# make a matrix of 260x2500 where each row is the email and each col is the word and its frequency
features = np.zeros((NUM_TEST_EMAILS, NUM_WORDS), dtype=int)
with open('test-features.txt') as feature_file:
    for i,line in enumerate(feature_file):
        l = line.split()
        row = int(l[0])
        col = int(l[1])
        val = int(l[2])
        features[row-1][col-1] += val

labels = []
with open('test-labels.txt') as label_file:
    for i,line in enumerate(label_file):
        labels += line.split()

# make a np matrix
labels = np.array(labels, dtype=int).reshape(NUM_TEST_EMAILS,1)
output = np.zeros([NUM_TEST_EMAILS,1])

# probability that one email is spam = # of spam emails/# of all emails
prob_spam = NUM_TEST_SPAM/NUM_TEST_EMAILS

# get chance for spam and non-spam emails in the test set

log_spam = np.dot(features, np.log(np.transpose(spam_probability))) + math.log(prob_spam)
log_ham = np.dot(features, np.log(np.transpose(nonspam_probability))) + math.log(1-prob_spam)

output = log_spam > log_ham
print(output)
# get the number of incorrectly predicted
wrong_labelled = np.sum(np.bitwise_xor(output, labels))
err = wrong_labelled/NUM_TEST_EMAILS
print(err)