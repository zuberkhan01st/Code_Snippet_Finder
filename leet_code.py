import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

# Load the datasets
df = pd.read_csv("leetcodeDATA.csv")
descriptions = pd.read_csv("leetcode_dataset.csv")

# Set page title and favicon
st.set_page_config(page_title='Code Snippet Finder', page_icon=":computer:")

# Sidebar option menu for selecting platform
selected = st.sidebar.selectbox('Select The Platform', ['Leetcode', 'GeeksForGeeks', 'Coding Ninjas', 'Codeforces'], index=0)

if selected == 'Leetcode':
    # Define the title and introduction
    st.title('Leetcode Code Snippet Finder')
    st.write("Welcome to the Leetcode Code Snippet Finder! Enter the question ID below to get the code snippet and details.")

    # Input field for question ID
    question_id = st.number_input('Enter the question ID:', min_value=1, max_value=len(df), value=1, step=1)

    # Adjust question ID to zero-based indexing
    question_index = question_id - 1

    if st.button('Get Code Snippet'):
        # Retrieve title
        title = descriptions.loc[descriptions['id'] == question_id, 'title'].iloc[0]
        st.header(title)

        # Retrieve Description
        description = descriptions.loc[descriptions['id'] == question_id, 'description'].iloc[0]
        st.header(description)

        # Retrieve code snippet
        code = df.loc[question_index, 'Answer']
        st.header("Code Snippet:")
        st.code(code, language='cpp')  # Assuming the code snippets are in C++

        # Retrieve companies
        companies = descriptions.loc[descriptions['id'] == question_id, 'companies'].iloc[0]
        st.title('Asked In:')
        st.write(companies)

        # Retrieve article link
        solution_link = descriptions.loc[descriptions['id'] == question_id, 'solution_link'].iloc[0]
        st.title('Article Link:')
        if st.button('Click to Visit Website'):
            st.markdown(f"[Click Here]({solution_link})")

        # Retrieve related topics
        related_topics = descriptions.loc[descriptions['id'] == question_id, 'related_topics'].iloc[0]
        st.title('Based On:')
        st.write(related_topics)

        # Add a footer with additional information or links
        st.markdown("---")
        st.markdown("Created with ❤ by Zuber, Harsh and Ayush")

elif selected == 'GeeksForGeeks':
    st.title('GeeksForGeeks Code Snippet Finder')
    st.write("Welcome to the GeeksForGeeks Code Snippet Finder!")
    st.title("In Progress")
    # Add a footer with additional information or links
    st.markdown("---")
    st.markdown("Created with ❤ by Zuber,Harsh and Ayush")

elif selected == 'Coding Ninjas':
    st.title('Coding Ninjas Code Snippet Finder')
    st.write("Welcome to the Coding Ninjas Code Snippet Finder!")
    st.title("In Progress")
    # Add a footer with additional information or links
    st.markdown("---")
    st.markdown("Created with ❤ by Zuber, Harsh and Ayush")

elif selected == 'Codeforces':
    st.title('Codeforces Code Snippet Finder')
    st.write("Welcome to the Codeforces Code Snippet Finder!")
    st.title("In Progress")
    # Add a footer with additional information or links
    st.markdown("---")
    st.markdown("Created with ❤ by Zuber, Harsh and Ayush")
