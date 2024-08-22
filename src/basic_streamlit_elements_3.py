# Basic streamlit elements
import streamlit as st

def basic_streamlit_elements():
    st.header(':blue[3] . Basic Streamlit Elements:man-boy-boy:')
    st.write('Let\'s explore some basic Streamlit elements:')
    st.code('''
    st.text('Fixed width text')
    st.markdown('_Markdown_') # see #*
    st.caption('Balloons. Hundreds of them...')
    st.latex(r""" e^{i\pi} + 1 = 0 """)
    st.write('Most objects') # df, err, func, keras!
    st.write(['st', 'is <', 3]) # see *
    st.title('My title')
    st.header('My header')
    st.subheader('My sub')
    st.code('for i in range(8): foo()')
    ''')
    st.subheader(':blue[3] . :red[2] Input Elements:man-girl-boy:')
    st.write("Streamlit provides various input elements:")
    name = st.text_input('Please enter your name')
    age = st.slider('Select your age', 10, 15)
    st.write(f'Hello :blue[{name}] you are :red[{age}] year old.')
    st.subheader('3.3 Display Image')
    st.write('You can display images like this.')
    st.image('https://pic1.zhimg.com/v2-a678cbd60508ae8907303154fb2340ac_r.jpg')
