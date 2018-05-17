# Classifying-furniture-pictures
Classifying furniture pictures using Convolutional Neural Networks.

This project uses Convolutional Neural Networks to classify the furniture pictures. It can also be used to classify other sets of images.

# Model.py:

The images of different classes should be placed in different folders. Training data and validation data should be be placed in the same folder. Image parameters and model parameters can be changed in the code. Image shape is assumed as 128 by 128 by 3. We used a three convolutional layers with two dense layers. We used fit generator to run the model.

# Run.py:

It takes the model saved in model.py as the input. The function loop takes the path of the test set as the parameter, resizes each image, shows each image along with it's class number.
