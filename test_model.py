import numpy as np
import math

# read test-features & test-labels and make into Nx3 array
arr = []
labels = []
numFeatures = 0
with open('test-features.txt') as feat:
    for i,line in enumerate(feat):
        ar = line.split()
        arr.append(ar)
        numFeatures = i+1

with open('test-labels.txt') as l:
    for i,line in enumerate(l):
        labels += line.split()

# make a np matrix
matrix = np.array(arr, dtype=int)
label = np.array(labels, dtype=int)

# get number of emails
numTestEmails = len(np.unique(matrix[:, 0]))

output = np.zeros(numTestEmails)

#probability that one email is spam = # of spam emails/# of all emails
chanceOfSpam = 1/numTestEmails #len(spam_indicies)/numTestEmails

# get chance for spam and non-spam emails in the test set
log_spam = matrix * np.log(probFeatSpam.getH()) + math.log(chanceOfSpam)
log_ham = matrix * np.log(probFeatHam.getH()) + math.log(1-chanceOfSpam)

output = log_spam > log_ham

# get the number of incorrectly predicted
wrongLabelled = np.sum(output != label)
err = wrongLabelled/numTestEmails