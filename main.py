import streamlit as st

with st.sidebar:
    st.write('practice')

st.text('This website is for noobs the know how to use streamlit')
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
st.header(':blue[2] . Setup:man-boy:')
st.write('To install Streamlit, run this command in your terminal or command prompt: ')
st.code('pip install streamlit')
st.write('Then create a new Python file for your project.')

# Basic streamlit elements
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

# Interactive app
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

# Running app
st.header(':blue[5]. Running The App')
st.write('To run your Streamlit app:')
st.code('cd /Users/a20160102024/Desktop/streamlit_web')
st.write('Change the directory to the correct file path')
st.code('streamlit run Intro_to_streamlit_day_1.py')
st.write('Make sure you are in the correct folder or directory on the terminal.')

# Hands on new activity
st.header(':blue[6]. Hands On Activity')
st.write('Now it\'s your turn! Try creating a simple Streamlit app.')
st.write('Here is a template to get you started:')
st.code('''
import streamlit as st
import random

st.title('Guess the Number Game')

# Generate a random between 1 and 100
secret_number = random.randint(1, 100)

# Get the player's guess
user_guess = st.number_input('Please guess a number between 1 and 100.', min_value = 1, max_value = 100 )

if st.button('click me to check'):
    if user_guess == secret_number:
        st.success('You win')
        st.balloons()
    elif user_guess < secret_number:
        st.warning('The number is lower than the secret_number.')
    elif user_guess > secret_number:
        st.warning('The number is higher than the secret_number.')
''')
st.success('Challenge: Can you add a feature to count the number of guesses?')    
    
