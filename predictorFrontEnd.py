import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('model.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))
# ['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax',
#        'ptratio', 'b', 'lstat']
st.title("House Price Predictor")

# Per capita crime rate by town.

crim = st.number_input('Crime Rate')

# Proportion of residential land zoned for lots over 25,000 square feet.
zn = st.number_input('Zone')


# Proportion of non-retail business acres per town.
indus = st.number_input('Indus')


# chas: Charles River dummy variable (1 if the tract bounds the river; 0 otherwise).
chas = st.selectbox('Chas', ['Yes', 'No'])



# Proportion of non-retail business acres per town.
NOX = st.number_input('NOX')


# Proportion of non-retail business acres per town.
rm = st.number_input('RM')





# Proportion of non-retail business acres per town.
age = st.number_input('Age')


# Proportion of non-retail business acres per town.
dis = st.number_input('dis')



rad = st.number_input('Radius')
tax = st.number_input('Tax')
ptratio = st.number_input('ptratio')


# Proportion of non-retail business acres per town.
b = st.number_input('Black')


lstat = st.number_input('lstat')




if st.button('Predict Price'):
    if chas == 'Yes':
         chas = 1
    else:
        chas = 0


    # inputArray = np.asarray(inputData)
    # inputReshaped = inputArray.reshape(1,-1)
    # prediction = model.predict(inputReshaped)
    query = np.array([crim, zn, indus, chas, NOX, rm, age, dis, rad, tax,ptratio, b, lstat])
    query = query.reshape(1,13)
    price = model.predict(query)
    st.title(price)

