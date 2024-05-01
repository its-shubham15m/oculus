import streamlit as st

def show_project_description():
    st.header("Project Description")

    st.subheader("Problem Statement:")
    st.write("""
        Daily activities like working, traveling, and learning, etc., might become more difficult when one is visually impaired or blind. 
        While smart glasses can be useful for navigation, they frequently offer users too much information, which can be overwhelming 
        and make it difficult to concentrate on crucial signs. Smart glasses for the visually impaired need a user-centered design 
        that focuses on essential cues to eliminate unnecessary information.
        """)

    st.subheader("Approach:")
    st.write("""
        As previously mentioned, our suggestion takes care of the issue by integrating a multi-objective Particle Swarm Optimization (PSO) 
        based optimizer — a metaheuristic filtering mechanism integrated into smart glasses. The hardware configuration includes an Arduino 
        Uno-based CPU schematized as a system that handles data transmission, processing, and collection. It uses an ESP8266 Wi-Fi module 
        for real-time updates and cloud-based item identification. A CMOS OV7670 Camera Module provides images in a wide range of formats. 
        Two 10kΩ resistors are used for the I²C connection to the camera and one pair of 650Ω and 1kΩ resistors for the camera clock voltage 
        divider. Additionally, a round push button serves as an emergency SOS button.

        First, we connect the ESP8266 Wi-Fi module with Arduino Uno and then connect the camera module OV7670. The final diagram includes all 
        components connected, enabling real-time image transmission.
    """)

    st.subheader("System Architecture:")
    # Create columns for each image
    col1, col2, col3 = st.columns(3)

    images = ["demo/system_architecture.png", "demo/system_architecture2.png", "demo/system_architecture3.png"]
    for i, image in enumerate(images, start=1):
        if i == 1:
            col1.image(image, caption="System Architecture Diagram", use_column_width=True)
        elif i == 2:
            col2.image(image, caption="System Architecture Diagram", use_column_width=True)
        elif i == 3:
            col3.image(image, caption="System Architecture Diagram", use_column_width=True)

    st.write("""
        YOLOv8, a convolutional neural network, is utilized for object detection in real-time. The architecture consists of multiple convolutional 
        layers followed by fully connected layers. We use a pre-trained dataset from ImageNet-2K and COCO for training YOLOv8. Finetuning common 
        hyperparameters like learning rate and batch size is essential for real-time object detection.

        Adam is used as the default optimizer in train.py due to its convergence properties. We also experiment with other optimizers like AdamW, 
        NAdam, RAdam, and RMSProp. Additionally, we integrate PSO-based optimization to filter out irrelevant objects and emphasize navigational 
        cues. The optimizer also integrates natural language processing capabilities through LLaMA version 2, enhancing the Oculus's responsiveness 
        and intelligence.

        Our system offers three key functionalities to enhance navigation for the visually impaired:
        1. Swift recognition and emphasis on navigational signals and primary objects in real-time.
        2. Providing better suggestions on nearby points of interest using databases and GPS position data.
        3. Allowing users to customize their priorities by adjusting confidence level.

        During deployment on mobile devices, TorchScript is used to reduce model size and improve performance. We also implement a Django Rest 
        Framework (DRF) toolkit for building WebAPIs to implement our model platform independently.
        """)

