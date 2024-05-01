import streamlit as st
import project_description
import coding
import live_demo

st.title("Project Demo")
st.markdown("""<hr style="height:3px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

# Sidebar with radio buttons
option = st.sidebar.radio("Choose an option", ("Project Description", "Coding Demo", "Live Demo", "About"))

if option == "Project Description":
    project_description.show_project_description()

elif option == "Coding Demo":
    coding.show_coding_demo()

elif option == "Live Demo":
    live_demo.show_live_demo()

elif option == "About":
    st.sidebar.subheader("About the Project")
    st.sidebar.write("""
        This project aims to [provide a brief description of the project here].
        Feel free to explore the different options in the sidebar to learn more.
    """)

    st.sidebar.subheader("Contact Us")
    st.sidebar.write("""
        For inquiries and feedback, please contact us at [email@example.com].
    """)
