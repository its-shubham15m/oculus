import streamlit as st

def show_live_demo():
    st.markdown("""
            <div style="font-family: Monteserrat, sans-serif;">
            <p>Checkout our Demo Web app 👇</p>
            <a href="https://attention-based-detection.streamlit.app/">Click Me!</a>
                <h2>Live Demo
                </h2>
        </div>
    """, unsafe_allow_html=True)


    # You can replace the video URL with your own video file URL
    video_url = 'Demo/demo-video.mp4'

    st.video(video_url)
