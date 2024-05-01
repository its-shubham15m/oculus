import streamlit as st
import project_description
import coding
import live_demo
import about

# Set the title and favicon
st.set_page_config(page_title="Project Demo", page_icon="demo/browser.png")

st.title("Project Demo")
st.markdown("""<hr style="height:3px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

option = st.sidebar.radio("Choose an option", ("Project Description", "Coding Demo", "Live Demo", "About"))

if option == "Project Description":
    project_description.show_project_description()

elif option == "Coding Demo":
    coding.show_coding_demo()

elif option == "Live Demo":
    live_demo.show_live_demo()

elif option == "About":
    st.sidebar.subheader("Contact us")
    st.sidebar.markdown("""
        <p>For inquiries and feedback, please contact:</p>
        <a href='mailto:shubhamgupta15m@gmail.com' class='button'>Shubham Gupta</a>\n
        <a href='mailto:deepchakraborty0810@gmail.com' class='button'>Deep Chakraborty</a>
    """, unsafe_allow_html=True)
    about.show_about()
