# Python In-built packages
from pathlib import Path
import PIL
import csv
import datetime
import pytz
import time

# External packages
import streamlit as st

# Local Modules
import settings
import helper
from Demo import app



logo = PIL.Image.open('images/pngwing.com (1).png')
logo = logo.resize((500, 500))
# Setting page layout
st.set_page_config(
    page_title="Detection using YOLOv8",
    page_icon=logo,
    layout="wide",
    initial_sidebar_state="auto"
)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
ms = st.session_state
if "themes" not in ms:
    ms.themes = {
        "current_theme": "light",
        "refreshed": True,
        "light": {
            "theme.base": "dark",
            "theme.backgroundColor": "black",
            "theme.primaryColor": "#c98bdb",
            "theme.secondaryBackgroundColor": "#14061E",
            "theme.textColor": "white",
            "button_face": "🌜"
        },
        "dark": {
            "theme.base": "light",
            "theme.backgroundColor": "white",
            "theme.primaryColor": "#5591f5",
            "theme.secondaryBackgroundColor": "#7bd5db",
            "theme.textColor": "#0a1464",
            "button_face": "🌞"
        }
    }





# Function to get holiday message for a given date
def get_message_of_the_day(date):
    with open('assets/holiday-data.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            holiday_date = datetime.datetime.strptime(row[0], '%d %B %Y').date()
            if holiday_date == date:
                month_name = date.strftime('%B')  # Get the month name from the date
                return row[1], row[2], month_name  # Return the holiday message, significance, and month name
    return None, None, None  # Return None if no holiday message found for the date

# Function to get the current time with time zone for Kolkata
def get_current_time_kolkata():
    # Get the current time in UTC
    current_time_utc = datetime.datetime.now(pytz.utc)
    # Convert the current time to Kolkata time zone
    kolkata_time = current_time_utc.astimezone(pytz.timezone('Asia/Kolkata'))
    return kolkata_time.strftime('%H:%M:%S %Z')





def change_theme():
    ms.sidebar_selection = True  # Initialize sidebar_selection when anything is selected in the sidebar
    previous_theme = ms.themes["current_theme"]
    tdict = ms.themes["light"] if ms.themes["current_theme"] == "light" else ms.themes["dark"]
    for vkey, vval in tdict.items():
        if vkey.startswith("theme"):
            st._config.set_option(vkey, vval)

    ms.themes["refreshed"] = False
    if previous_theme == "dark":
        ms.themes["current_theme"] = "light"
    elif previous_theme == "light":
        ms.themes["current_theme"] = "dark"


# Button face based on current theme
btn_face = ms.themes["light"]["button_face"] if ms.themes["current_theme"] == "light" else ms.themes["dark"][
    "button_face"]

# Button to change theme
st.button(btn_face, on_click=change_theme)

# Check if theme needs to be refreshed
if not ms.themes["refreshed"]:
    ms.themes["refreshed"] = True





# Initialize session state attribute for sidebar selection
if "sidebar_selection" not in ms:
    ms.sidebar_selection = False

# Main page heading
st.title("Detection using YOLOv8")
st.markdown()
st.warning('👈 Select your model')

# Sidebar
st.sidebar.header("Features")

# Model Options
model_type = st.sidebar.radio(
    "Select Task", ['Detection', 'Segmentation'])

confidence = float(st.sidebar.slider(
    "Select Confidence", 25, 100, 40)) / 100

# Selecting Detection Or Segmentation
if model_type == 'Detection':
    model_path = Path(settings.DETECTION_MODEL)
elif model_type == 'Segmentation':
    model_path = Path(settings.SEGMENTATION_MODEL)

# Load Pre-trained ML Model
try:
    model = helper.load_model(model_path)
except Exception as ex:
    st.error(f"Unable to load model. Check the specified path: {model_path}")
    st.error(ex)





st.sidebar.header("Image/Video Config")
source_radio = st.sidebar.radio(
    "Select Source", settings.SOURCES_LIST)

# If image is selected
if source_radio == settings.IMAGE:
    source_img = st.sidebar.file_uploader(
        "Choose an image...", type=("jpg", "jpeg", "png", 'bmp', 'webp'))

    # Display date, holiday, significance, and holiday message if it's a holiday
    today_date = datetime.date.today()
    holiday_message, significance, month_name = get_message_of_the_day(today_date)
    # Display the month name in the subheader
    st.markdown(f"<h1 style='text-align: center; font-size: 35px; font-family: Lato, sans-serif;'>{month_name} Highlight</h1>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        try:
            if source_img is None:
                default_image_path = str(settings.DEFAULT_IMAGE)
                default_image = PIL.Image.open(default_image_path)
                st.image(default_image_path, caption="Default Image",
                         use_column_width=True)
            else:
                uploaded_image = PIL.Image.open(source_img)
                st.image(source_img, caption="Uploaded Image",
                         use_column_width=True)
        except Exception as ex:
            st.error("Error occurred while opening the image.")
            st.error(ex)

    with col2:
        if source_img is None:
            default_detected_image_path = str(settings.DEFAULT_DETECT_IMAGE)
            default_detected_image = PIL.Image.open(
                default_detected_image_path)
            st.image(default_detected_image_path, caption='Detected Image',
                     use_column_width=True)
        else:
            if st.sidebar.button('Detect Objects'):
                res = model.predict(uploaded_image,
                                    conf=confidence
                                    )
                boxes = res[0].boxes
                res_plotted = res[0].plot()[:, :, ::-1]
                st.image(res_plotted, caption='Detected Image',
                         use_column_width=True)
                try:
                    with st.expander("Detection Results"):
                        for box in boxes:
                            st.write(box.data)
                except Exception as ex:
                    # st.write(ex)
                    st.write("No image is uploaded yet!")

elif source_radio == settings.VIDEO:
    helper.play_stored_video(confidence, model)

elif source_radio == settings.WEBCAM:
    helper.play_webcam(confidence, model)

elif source_radio == settings.RTSP:
    helper.play_rtsp_stream(confidence, model)

elif source_radio == settings.YOUTUBE:
    helper.play_youtube_video(confidence, model)

elif source_radio == settings.WEBCAMLIVE:
    helper.display_webcam()

else:
    st.error("Please select a valid source type!")





if source_radio == settings.IMAGE:
    # Create Streamlit columns for displaying holiday info and current time
    col1, col2 = st.columns(2)

    with col1:
        if holiday_message:
            st.write(f"<span style='font-family: Arial; font-size: 16px; font-style: sans-serif;'>Date: {today_date}</span>", unsafe_allow_html=True)
            st.write(f"<span style='font-family: Arial; font-size: 16px; font-style: sans-serif;'>Holiday: {holiday_message}</span>", unsafe_allow_html=True)
            st.write(f"<span style='font-family: Arial; font-size: 16px; font-style: sans-serif;'>Significance: {significance}</span>", unsafe_allow_html=True)

    with col2:
        if holiday_message:
            # Display the current time with time zone for Kolkata in the Streamlit app
            st.write("<span style='font-family: Arial; font-size: 16px; font-style: sans-serif;'>Current Time (Kolkata Time Zone):</span>", unsafe_allow_html=True)
            # Placeholder for displaying the current time
            time_placeholder = st.empty()

            # Update the displayed time continuously
            while True:
                # Get the current time in Kolkata time zone
                current_time_kolkata = get_current_time_kolkata()
                # Update the displayed time
                time_placeholder.write(f"<span style='font-family: Arial; font-size: 16px; font-style: sans-serif;'>{current_time_kolkata}</span>", unsafe_allow_html=True)
                # Wait for a short duration before updating again
                time.sleep(1)
