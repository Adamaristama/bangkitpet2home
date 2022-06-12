# Pet2Home - C22-PS110 (Machine Learning)
## Capstone Project Team
- Adam Aristama (M2211F1958) 
- Devany Putri Mirasati (M7211F1957) 
- Dinda Fathihah Sari (C7211F1960) 
- Dimas Bayu Anjasmara (C7266F2290)
- Ferdian Arjutama Narwan (A2183G1774) 
- Indra Purnomo Aji (A7299F2590) 

## About The Project

Pet2Home is an application intended to raise awareness of abandoned animals, especially cats and dogs, and also to help potential adopters to find their pets. Aside from adopting animals, users also can use a Pet2Lens feature that can make it easier to find out the breeds of dogs or cats they found. This project expects to help improve the welfare of abandoned animals and reduce the level of animal violence to illegal trade in animals, especially dogs and cats.


This app is able to identify 5 breed of dog and 5 breed of cat and determine its quality with a Machine Learning model. And then it will insert the data into a database, which will save all the breed info which is saved into it. Currently the classifications are limited to:

- Abyssinian
- Beagle
- Bombay
- British Shorthair
- Chihuahua
- Persian
- Pomeranian
- Pug
- Shiba Inu
- Siamese

# Cloud Api Architecture for this app
![ML Architecture drawio](https://user-images.githubusercontent.com/22671679/173228471-882fb376-6d03-4375-bae4-64739c70f2c2.png)

# Machine Learning Model Architecture used for this app

- Transfer Learning Xception Architecure

![image](https://user-images.githubusercontent.com/53483448/173228123-68ef06e1-39d0-4202-b151-d55991800be2.png)

- model 

![modelplot](https://user-images.githubusercontent.com/53483448/173228156-761de12c-2d64-4f11-b731-b9ce514407f0.png)


# Dataset
link dataset https://www.kaggle.com/datasets/zippyz/cats-and-dogs-breeds-classification-oxford-dataset


# Steps 
- Model Building
  - Mount your Google Drive to colab and download the dataset
  - Or using kaggle API to download directly to google colab
  - Unzip dataset after that shuffle and split data into train and validation
  - Make sure that all categories are listed as a directory in the dataset folder
  - Create ImageDataGenerator for train, validation 
  - Build the model architecture, and set callbacks
  - Fit the model, and evaluate it
  - Visualize the result, and convert model into SavedModel, TFLite format or model.h5



# How to run this Flask app
- Create Compute Engine Instances and connect Instances via ssh
- Clone this repo `git clone https://github.com/Adamaristama/bangkitpet2home.git`
- Type `python3 -m venv .venv` and hit enter
- And then, type `source .venv/bin/activate`
- Type `pip install -r requirements.txt`
- Start this Server With command `python3 main.py`
- It will run on `http://127.0.0.1:5000` and can connect into it via GCE instances Public IP
- Machine Learning model deployed


