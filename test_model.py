import numpy as np
import math
from training_model import spam_indexes, spam_probability, nonspam_probability

# read test-features & test-labels and make into Nx3 array
features = []
labels = []
with open('test-features.txt') as feature_file:
    for i,line in enumerate(feature_file):
        ar = line.split()
        arr.append(ar)
        numFeatures = i+1

with open('test-labels.txt') as label_file:
    for i,line in enumerate(label_file):
        labels += line.split()

# make a np matrix
features = np.array(features, dtype=int)
labels = np.array(labels, dtype=int)

# get number of emails
num_test_emails = len(np.unique(matrix[:, 0]))

output = np.zeros(num_test_emails)

#probability that one email is spam = # of spam emails/# of all emails
prob_spam = len(spam_indexes)/num_test_emails

# get chance for spam and non-spam emails in the test set
log_spam = features * np.log(spam_probability.getH()) + math.log(prob_spam)
log_ham = features * np.log(nonspam_probability.getH()) + math.log(1-prob_spam)

output = log_spam > log_ham

# get the number of incorrectly predicted
wrong_labelled = np.sum(output != labels)
err = wrong_labelled/num_test_emails