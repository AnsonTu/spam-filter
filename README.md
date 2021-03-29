# Spam Filtering

### Group 5
Anson Tu (100655482) 

Cassidy Linhares (100615025)

Cristina Chung (100711128)

Kaushik Ramani (100651855)

## Project Scope
As our world becomes more and more digitalized we receive more electronic mail than ever before, this advacement has also increased the amount of spam emails we get on a daily basis. The main purpose of this project was to create an AI agent that can determine if an email is spam or not by "reading" it. The program is able to do this by identifying the words that we can usually find in both, a spam and non-spam email. Words that are common in spam emails will usually appear with less frequency in regular emails, we can calculate this probability using Naives Bayesian model and train the program to be able to filtrate the email with a sufficient success rate. Using this program will allow the user to feel more secure, this program will also help clear up the user's main inbox page by automatically moving the emails detected as spam into a separate folder.

## Set Up 
- Please download and install Python v3 [here](https://www.python.org/downloads/).  
- Also add python to you Path so it can run in terminal.  
- After installing python install the numpy library by opening the terminal(Mac/Linux) or powershell(Windows) and running the command `pip3 install numpy`. If pip3 does not work then use `pip install numpy`.  
- Clone this repository. 

## How to use the Scripts and Functions
1. Download the folder
1. Navigate to the folder
2. Open the terminal/powershell in the folder

### `make_dictionary.py`
**`make_dictionary.py`**: gets a list of the most common words and their frequency (that aren't you, I, is, etc.) from the spam and non-spam training data sets and outputs it to a `.txt` file.  
**To Run**: In the terminal enter `python3 make_dictionary.py` or `python make_dictionary.py`.

### `get_dictionary_list.py`
**`get_dictionary_list.py`** contains a function that can be called by invoking `dictionaryList()`.  
**`dictionaryList() returns dict()`**: call to get the most common words and their frequency as a dictionary/hash map data structure.

### `generate_features.py`
**`generate_features.py`**: creates four `.txt` files. Two files pertain to the Training data set and the other 2 files pertain to the test data sets. Of the 2 files, the first file contains 3 integers separated by a space delimeter. The first number represents the email id, the 2nd number is the rank of the word from our dictionary, and the 3rd number is the number of occurences, that word appears in the email. The second file is the classification of whether the email is spam or non-spam. This is done for all test data set emails and all training data set emails. These files will help to make a Naive Bayesian model for training and then for testing.  
**To Run**: In the terminal enter `python3 generate_features.py` or `python generate_features.py`.

### `training_model.py`
**`training_model.py`**: is a script that creates a naive Bayesian model using the `train-features.txt` and `train-labels.txt`.  
**To Run**: In the terminal enter `python3 training_model.py` or `python training_model.py`.

### `test_model.py`
**`test_model.py`**: is a script that applies the naive Bayesian model from `training_model.py` to the test data set files, `test-features.txt` and confirms its accuracy with `test-labels.txt`.  
**To Run**: In the terminal enter `python3 test_model.py` or `python test_model.py`.
