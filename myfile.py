import pickle
import streamlit as st

model = pickle.load(open("house.pkl","rb"))

def myf1():
  st.title("!!House Price Prediction!!")
  area = st.number_input("Enter the area value:")
  bedrooms = st.number_input("Enter the number of bedrooms in the house:")
  age = st.number_input("Enter the age of the house:")
  pred = st.button("predict")
  if pred:
    op = model.predict([[area,bedrooms,age]])
    st.write("The predicted value of House will be: {:0.2f}.".format(op[0]))

myf1()