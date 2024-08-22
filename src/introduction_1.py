# introduction_1.py
import streamlit as st

def introduction():    
    st.title('MY lesson plan for Intro to Streamlit Day :blue[1] :new_moon_with_face: ')
    st.subheader('_A_ :green[Lesson plan] for beginner python coders.:thinking_face: ')
    st.header(':blue[1] . Introduction:male-technologist:')
    st.write('Streamlit is a Python library that makes it easy to create web apps.')
    if st.button('Click me =)'):
        st.code('''
import streamlit as st

st.title("Hello, Streamlit!")
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}!")

''')
