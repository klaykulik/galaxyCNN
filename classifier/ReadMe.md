Current status
=====================
1. ./data directory contains all the image data we are going to use
2. Each subdirectory in ./data is a class contains the images of that class
3. classifier.ipynb contains a simple multi-class classifier that reads all the data from ./data directory
4. The classifier will split the data into training data and validation data
5. Since we don't have test data yet, the final test is currently using the validation data

ToDo
=====================
1. Currently all the data would be augmented, we only need to augment the classes with less data
2. Find more data for testing or split the current data to train+vali and test
3. Try more models, optimizers and loss functions.
