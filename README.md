# Pareekshan

## Project Description

Pareekshan is a Web App, which predicts the chances of an individual being COVID-19 positive or negative on the basis of their symptoms.

Database used is taken from [Israel Government Medical Covid-19 Dataset](https://data.gov.il/dataset/covid-19/resource/d337959a-020a-4ed3-84f7-fca182292308).

After the collection and preprocessing of data.

A three layered neural network was constructed and trained over 80% data.

After testing it on remaining data, accuracy of 92.58% was received.

## Libraries used

1. tensorflow.keras
2. sklearn.preprocessing
3. streamlit



## To run

First run the python notebook ANN.ipynb in sequence to create the machine learning model

To run the application type the following command in terminal

```
streamlit run interface.py
```

## Some Sample Output

![SS1](Output-SS/1.png?raw=true "Output")
![SS2](Output-SS/2.png?raw=true "Output")
![SS3](Output-SS/3.png?raw=true "Output")

