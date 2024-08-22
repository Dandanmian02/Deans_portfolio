import streamlit as st

from src.introduction_1 import introduction

from src.setup_2 import setup

# Basic streamlit elements
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

# Interactive app
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

# Running app
def running_app():
    st.header(':blue[5]. Running The App')
    st.write('To run your Streamlit app:')
    st.code('cd /Users/a20160102024/Desktop/streamlit_web')
    st.write('Change the directory to the correct file path')
    st.code('streamlit run Intro_to_streamlit_day_1.py')
    st.write('Make sure you are in the correct folder or directory on the terminal.')

# Hands on new activity
def hands_on_new_activity():
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


def main():
    with st.sidebar:
        st.write('lesson sections')
        sections = ['Home', 'Introduction','Setup', 'Basic streamlit elements', 'Interactive app', 'Running app', 'Hands on new activity',]
    select_section = st.sidebar.radio('choose a section', sections)
    if select_section == 'Home':
        introduction()
        setup()
        basic_streamlit_elements()
        interactive_app()
        running_app()
        hands_on_new_activity()
    elif select_section == 'Introduction':
        introduction()
    elif select_section == 'Setup':
        setup()
    elif select_section == 'Basic streamlit elements':
        basic_streamlit_elements()
    elif select_section == 'Interactive app':
        interactive_app()
    elif select_section == 'Running app':
        running_app()
    elif select_section == 'Hands on new activity':
        hands_on_new_activity()
    
if __name__ == '__main__':
    main()
    
  



        















        
