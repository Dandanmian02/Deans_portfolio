import streamlit as st

from src.introduction_1 import introduction
from src.setup_2 import setup
from src.basic_streamlit_elements_3 import basic_streamlit_elements
from src.interactive_app_4 import interactive_app


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
    
  



        















        
