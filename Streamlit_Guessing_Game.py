#Streamlit_Guessing_Game

import streamlit as st
import random

st.title('Guess the number')

secret_number = random.randint(1, 100)
st.text(secret_number)

user_number = st.number_input('Please give a number between 1 and 100', min_value = 1, max_value = 100)


#a button is being pressed here
if st.button('click me to check'):
    if user_number == secret_number:
        st.success('You Won!')
        st.balloons()
    elif user_number < secret_number:
        st.warning('The number is less than the secret number.')
    elif user_number > secret_number:
        st.warning('The number is greater than the secret number.')

