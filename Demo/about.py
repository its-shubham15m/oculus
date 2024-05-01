import streamlit as st

def show_about():
    st.subheader("About the Project")
    st.markdown("""
        <div style="font-family: Monteserrat, sans-serif;">
            <p>
                ACM Kolkata Chapter B.Tech Project Award 2024
                (India East & North-East) for Computing streams
            </p>
            <p><strong>Title of the Project:</strong> Development of innovative Smart Glass using metaheuristic based gradient free optimization technique</p>
            <p><strong>Name of the Student(s):</strong> Deep Chakraborty, Shubham Gupta</p>
            <p><strong>Name of the Institute:</strong> MCKV INSTITUTE OF ENGINEERING</p>
            <p><strong>Name of Supervisor:</strong> Dr. Debabrata Datta, Mr. Uddalok Sen</p>
            <p><strong>Abstract:</strong> Blind or visually impaired people who wear smart eyeglasses typically experience information overload. 
            It feels like you have a tour guide pointing out every little detail in the crowded cities. While these 
            glasses do a great job of identifying objects, they overwhelm users with irrelevant information, making 
            it hard to focus on important navigational cues. Through the development of an optimizer—a sophisticated 
            system that serves as a helpful aide for smart glasses users—our research aims to solve this issue. 
            Developing a real-time system using real time streaming protocol (RTSM) to aid these people using 
            state-of-the-art deep learning technologies You Only Look Once version 8 (YOLOv8) for object detection 
            and Large Language Model Meta AI (LLaMA) for natural language processing and speech-to-text conversion 
            to process pieces of information provided from cameras and sensors attached to glasses (Smart Glass). 
            The optimizer (Multi-objective PSO based) makes decisions by thoroughly examining the continually 
            recorded data, extracting useful features, and making judgments.
            </p>
        </div>
    """, unsafe_allow_html=True)
