# Interactive app

import streamlit as st

def interactive_app():
    st.header(':blue[4]. Simple Interactive App')
    st.write('Let\'s create a basic calculator:')
    num1 = st.number_input('Enter the first number', value = 0)
    num2 = st.number_input('Enter the second number', value = 0)
    operation = st.selectbox('Choose operation', ['+', '-', '*', '/'])
    if st.button('calculate'):
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                result = 'You can not type in 0 for num2'
            else:
                result = num1 / num2
             
        st.success(f'Your result is {result}.')
