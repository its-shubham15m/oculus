from ultralytics import YOLO
import time
import streamlit as st
import cv2
from pytube import YouTube
import numpy as np

import settings


def load_model(model_path):
    """
    Loads a YOLO object detection model from the specified model_path.

    Parameters:
        model_path (str): The path to the YOLO model file.

    Returns:
        A YOLO object detection model.
    """
    model = YOLO(model_path)
    return model


def display_tracker_options():
    display_tracker = st.radio("Display Tracker", ('Yes', 'No'))
    is_display_tracker = True if display_tracker == 'Yes' else False
    if is_display_tracker:
        tracker_type = st.radio("Tracker", ("bytetrack.yaml", "botsort.yaml"))
        return is_display_tracker, tracker_type
    return is_display_tracker, None


def _display_detected_frames(conf, model, st_frame, image, is_display_tracking=None, tracker=None):
    """
    Display the detected objects on a video frame using the YOLOv8 model.

    Args:
    - conf (float): Confidence threshold for object detection.
    - model (YoloV8): A YOLOv8 object detection model.
    - st_frame (Streamlit object): A Streamlit object to display the detected video.
    - image (numpy array): A numpy array representing the video frame.
    - is_display_tracking (bool): A flag indicating whether to display object tracking (default=None).

    Returns:
    None
    """

    # Resize the image to a standard size
    image = cv2.resize(image, (720, int(720 * (9 / 16))))

    # Display object tracking, if specified
    if is_display_tracking:
        res = model.track(image, conf=conf, persist=True, tracker=tracker)
    else:
        # Predict the objects in the image using the YOLOv8 model
        res = model.predict(image, conf=conf)

    # # Plot the detected objects on the video frame
    res_plotted = res[0].plot()
    st_frame.image(res_plotted,
                   caption='Detected Video',
                   channels="BGR",
                   use_column_width=True
                   )


def play_youtube_video(conf, model):
    """
    Plays a webcam stream. Detects Objects in real-time using the YOLOv8 object detection model.

    Parameters:
        conf: Confidence of YOLOv8 model.
        model: An instance of the `YOLOv8` class containing the YOLOv8 model.

    Returns:
        None

    Raises:
        None
    """
    source_youtube = st.sidebar.text_input("YouTube Video url")

    is_display_tracker, tracker = display_tracker_options()

    if st.sidebar.button('Detect Objects'):
        try:
            yt = YouTube(source_youtube)
            stream = yt.streams.filter(file_extension="mp4", res=720).first()
            vid_cap = cv2.VideoCapture(stream.url)

            st_frame = st.empty()
            while (vid_cap.isOpened()):
                success, image = vid_cap.read()
                if success:
                    _display_detected_frames(conf,
                                             model,
                                             st_frame,
                                             image,
                                             is_display_tracker,
                                             tracker,
                                             )
                else:
                    vid_cap.release()
                    break
        except Exception as e:
            st.sidebar.error("Error loading video: " + str(e))


def play_rtsp_stream(conf, model):
    """
    Plays an rtsp stream. Detects Objects in real-time using the YOLOv8 object detection model.

    Parameters:
        conf: Confidence of YOLOv8 model.
        model: An instance of the `YOLOv8` class containing the YOLOv8 model.

    Returns:
        None

    Raises:
        None
    """
    source_rtsp = st.sidebar.text_input("rtsp stream url:")
    st.sidebar.caption('Example URL: rtsp://admin:12345@192.168.1.210:554/Streaming/Channels/101')
    is_display_tracker, tracker = display_tracker_options()
    if st.sidebar.button('Detect Objects'):
        try:
            vid_cap = cv2.VideoCapture(source_rtsp)
            st_frame = st.empty()
            while (vid_cap.isOpened()):
                success, image = vid_cap.read()
                if success:
                    _display_detected_frames(conf,
                                             model,
                                             st_frame,
                                             image,
                                             is_display_tracker,
                                             tracker
                                             )
                else:
                    vid_cap.release()
                    # vid_cap = cv2.VideoCapture(source_rtsp)
                    # time.sleep(0.1)
                    # continue
                    break
        except Exception as e:
            vid_cap.release()
            st.sidebar.error("Error loading RTSP stream: " + str(e))


def single_display_detected_frames(conf, model, image, is_display_tracking=None, tracker=None):
    """
    Processes and displays a single image with object detection results.

    Args:
        conf: Confidence threshold for detection.
        model: Loaded object detection model.
        image: The image to be processed (OpenCV format).
        is_display_tracking (optional): Flag indicating if tracker should be displayed.
        tracker (optional): Tracker object if tracking is enabled.

    Returns:
        Processed image with detections.
    """
    if is_display_tracking:
        res = model.track(image, conf=conf, persist=True, tracker=tracker)
    else:
        res = model.predict(image, conf=conf)

    res_plotted = res[0].plot()
    return res_plotted  # Return the processed image with detections

def play_webcam(confidence, model):
    """
    Plays a webcam stream and performs object detection in real-time using the YOLOv8 object detection model.

    Parameters:
        confidence: Confidence threshold for object detection.
        model: An instance of the `YOLOv8` class containing the YOLOv8 model.

    Returns:
        None
    """

    # OpenCV capture object for webcam
    cap = cv2.VideoCapture(0)

    # Check if webcam opened successfully
    if not cap.isOpened():
        st.error("Failed to open webcam.")
        return

    # Create Streamlit columns for displaying webcam feed and object detection
    col1, col2 = st.columns(2)
    col1.title("Live Webcam Feed")
    col2.title("Object Detection")

    # Placeholder for displaying the live webcam feed
    st_frame = col1.empty()

    # Placeholder for displaying the detected objects
    st_objects = col2.empty()

    # Loop to capture frames from the webcam
    while True:
        ret, frame = cap.read()

        # Check if frame is valid
        if not ret:
            st.error("Failed to capture frame from webcam.")
            break

        # Mirror the frame horizontally
        mirrored_frame = cv2.flip(frame, 0)

        # Display the mirrored frame in the Streamlit app
        st_frame.image(mirrored_frame, channels="BGR")

        # Detect objects in the frame
        processed_frame = single_display_detected_frames(confidence, model, frame)

        # Display the processed frame with detections
        st_objects.image(processed_frame, channels="BGR", use_column_width=True)

        # Add a small delay to reduce CPU usage
        st.experimental_rerun()

    # Release the webcam
    cap.release()

def play_stored_video(conf, model):
    """
    Plays a stored video file. Tracks and detects objects in real-time using the YOLOv8 object detection model.

    Parameters:
        conf: Confidence of YOLOv8 model.
        model: An instance of the `YOLOv8` class containing the YOLOv8 model.

    Returns:
        None

    Raises:
        None
    """
    source_vid = st.sidebar.selectbox(
        "Choose a video...", settings.VIDEOS_DICT.keys())

    is_display_tracker, tracker = display_tracker_options()

    with open(settings.VIDEOS_DICT.get(source_vid), 'rb') as video_file:
        video_bytes = video_file.read()
    if video_bytes:
        st.video(video_bytes)

    if st.sidebar.button('Detect Video Objects'):
        try:
            vid_cap = cv2.VideoCapture(
                str(settings.VIDEOS_DICT.get(source_vid)))
            st_frame = st.empty()
            while (vid_cap.isOpened()):
                success, image = vid_cap.read()
                if success:
                    _display_detected_frames(conf,
                                             model,
                                             st_frame,
                                             image,
                                             is_display_tracker,
                                             tracker
                                             )
                else:
                    vid_cap.release()
                    break
        except Exception as e:
            st.sidebar.error("Error loading video: " + str(e))

def display_webcam():
    """
    Displays real-time video stream from the webcam with an option to toggle between normal and mirrored mode.
    """
    # OpenCV capture object for webcam
    cap = cv2.VideoCapture(0)

    # Check if webcam opened successfully
    if not cap.isOpened():
        st.error("Failed to open webcam.")
        return

    # Set the title for the Streamlit app
    st.title("Webcam Stream")

    # Checkbox to toggle between normal and mirrored mode
    mirror_mode = st.checkbox("Mirror Mode", value=False)

    frame_placeholder = st.empty()

    # Add a "Stop" button and store its state in a variable
    stop_button_pressed = st.button("Stop")

    # Loop to capture frames from the webcam
    while cap.isOpened() and not stop_button_pressed:
        ret, frame = cap.read()

        # Check if frame is valid
        if not ret:
            st.write("The video capture has ended.")
            break

        # Convert the frame from BGR to RGB format
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Check if mirror mode is enabled
        if mirror_mode:
            # Flip the frame horizontally (mirror mode)
            frame_rgb = cv2.flip(frame_rgb, 1)

        # Display the frame in the Streamlit app
        frame_placeholder.image(frame_rgb, channels="RGB", use_column_width=True)

        # Wait for a short duration to display the next frame
        time.sleep(0.01)

    # Release the webcam and close Streamlit app
    cap.release()