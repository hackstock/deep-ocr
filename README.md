# About Deep OCR
Deep OCR is an example project that aims to show you how to to the following :
1. Train a digits classifier model using Keras(with Tensorflow backend) on the MNIST dataset
2. How to draw digits with your mouse (using OpenCV GUI) and let the model predict the digit

I was motivated to do this because most tutorials end after training a model without showing
you how make predictions on images outside the MINST dataset. Though this project makes 
predictions on images drawn with the mouse, you can equally adapt the code to make it predict
on images read from the camera using OpenCV.

## Setup
There are two ways to setup this project on your local machine. You can either use Anaconda or the default Python <= 3.6 version installed on your workstation. It is important to use Python 3.6 or less because Tensorflow (which is only used as a backend for Keras in this project) doesn't have a good support for Python 3.7 yet.

### Setting Up With Anaconda
1. Run "conda env create" from the root of this folder
2. Run "conda activate deepocr"
3. Run "python3 app.py", and have fun!

### Setting Up With Virtualenv (Python <= 3.6)
1. Run "python3 -m venv env" from the root of this folder
2. Run "source env/bin/activate"
3. Run "pip install -r requirements.txt"
4. Run "python3 app.py", and have fun!

## About Me
My name is Edward Pie, and I have almost an insatiable desire to learn everything about Deep Learning & Computer Vision. My specific areas of interest are applications of Deep Learning in agriculture, health, and industrial automation.

### Contact
- Email Address   : hackstockpie@gmail.com
- Youtube Channel : [Practical Computer Vision & Deep Learning With Python](https://www.youtube.com/watch?v=P1VwchTUM9Y&list=PL5MBdY0Scom2Vy0ljLWnLmMHBmatfVVbN)
- Phone Number    : +49 179 4491095
- Location        : Berlin, Germany