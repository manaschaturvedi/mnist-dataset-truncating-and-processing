import gzip
import pickle
import csv


# unpickling the .pkl file
with open('mnist.pkl', 'rb') as f:
    data = pickle.load(f)

# dissecting the original dataset into three different datasets
training_set = data[0]
validation_set = data[1]
testing_set = data[2]

dataset_size = 50  # setting the truncated dataset size (max = 50000)

''' 
    Generating CSV files for truncated training, cross validation and testing sets
    First column: label
    Remaining columns: features
    Each individual row represents an image's pixel values (features) along with its digit (label) 
'''

# generating a CSV file for training set
with open('training_set.csv','wb') as out:
    csv_out = csv.writer(out)
    for i in range(dataset_size):
    	current_row = [training_set[1][i]] + list(training_set[0][i])
    	csv_out.writerow(current_row)

# generating a CSV file for cross validation set
with open('validation_set.csv','wb') as out:
    csv_out = csv.writer(out)
    for i in range(dataset_size):
    	current_row = [validation_set[1][i]] + list(validation_set[0][i])
    	csv_out.writerow(current_row)

# generating a CSV file for testing set
with open('testing_set.csv','wb') as out:
    csv_out = csv.writer(out)
    for i in range(dataset_size):
    	current_row = [testing_set[1][i]] + list(testing_set[0][i])
    	csv_out.writerow(current_row)
