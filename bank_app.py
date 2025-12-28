import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image
pickle_in=open('classfier.pkl','rb')
model=pickle.load(pickle_in)

def welcome():
    return 'welcome all'

def predict_note_authentication(variance,skewness,curtosis,entropy):
    prediction=model.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction
def main():
    st.title('bank authenticator')
    html_temp="""
    <div style='background-color:tomato;padding:10px'>
    <h2 style='color:white;text-align:center;'>streamlit bank authentication ml app </h2>
    </div>
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    variance=st.text_input('variance','')
    skewness=st.text_input('skewness','')
    curtosis=st.text_input('curtosis','')
    entropy=st.text_input('entropy','')
    result=''
    if st.button('predict'):
        result=predict_note_authentication(variance,skewness,curtosis,entropy)
    st.success('the output is {}'.format(result))
    if st.button('about'):
        st.text('lets learn')
        st.text('bulit with stremlit')
        
if __name__=='__main__':
    main()
