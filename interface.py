import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

model=tf.keras.models.load_model('model.h5')

st.title("Pareekshan")
st.image('./image.png', width=800)
st.subheader("Please answer the following questions:")
st.sidebar.subheader("Common Symptoms of Corona Virus")
st.sidebar.write("1. Cough")
st.sidebar.write("2. Fever")
st.sidebar.write("3. Sore throat")
st.sidebar.write("4. Shortness of breath")
st.sidebar.write("5. Headache")
st.sidebar.subheader("Covid Appropriate Behavior")
st.sidebar.write("1. Always wear a mask")
st.sidebar.write("2. Sanitise your hands")
st.sidebar.write("3. Maintain 6-feet distance")
st.sidebar.write("4. Avoid crowded places")
st.sidebar.write("5. Get yourself Vaccinated")


cough=st.radio("Do you have cough?", ('Yes','No'))

fever=st.radio("Do you have fever?", ('Yes','No'))

sore_throat=st.radio("Do you have sore throat?", ('Yes','No'))

short_breath=st.radio("Do you feel shortness of breath?", ('Yes','No'))

headache=st.radio("Do you have headache?", ('Yes','No'))

age_60_above=st.radio("Are you aged 60 or above?",('Yes','No'))

gender=st.radio("You identify yourself as: ",('Male','Female'))

test_indication=st.radio("Reason to undergo test?",('Contact with confirmed','International Travel','Others'))



if cough=='Yes':
    cough=1
else:
    cough=0

if fever=='Yes':
    fever=1
else:
    fever=0

if sore_throat=='Yes':
    sore_throat=1
else:
    sore_throat=0

if short_breath=='Yes':
    short_breath=1
else:
    short_breath=0

if headache=='Yes':
    headache=1
else:
    headache=0

if age_60_above=='Yes':
    age_60_above=1
else:
    age_60_above=0

if gender=='Male':
    gender=1
else:
    gender=0

if test_indication=='Contact with confirmed':
    test_indication=1
else:
    if test_indication=='International Travel':
        test_indication=0
    else:
        test_indication=2
   

X=np.array([cough,fever,sore_throat,short_breath,headache,age_60_above,gender,test_indication])

inputX=X.reshape(1,8)



if st.button('Check'):
    output=model.predict(inputX)
   
    result=np.argmax(output,axis=-1)
   
    if result==2:
        st.header("Results: Positive")
        percentage=np.max(output)*100
        st.write("Please get yourself checked")
        st.write("You have ",percentage,"% chances of being positive")
    else:
        if result==1:
            st.header("Results: Others")
            percentage=np.max(output)*100
            st.write("Please get yourself checked, we are not able to predict your case")
            st.write("You have ",percentage,"% chances of being positive")
        else:
            st.header("Results: Negative")
            percentage=np.max(output)*100
            st.write("For precautions, please get yourself checked")
            st.write("You have ",percentage,"% chances of being negative")
           
    