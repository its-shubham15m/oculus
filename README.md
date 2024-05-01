# Innovative Smart Glass using Metaheuristic Based Gradient-Free Optimization technique

## Introduction:
Smart glasses offer great potential for aiding visually impaired individuals, but often overwhelm users with excessive information. Our research addresses this issue through the development of an optimizer—a sophisticated system integrated into smart glasses. By leveraging real-time streaming protocol (RTSM) and cutting-edge deep learning technologies like You Only Look Once version 8 (YOLOv8) for object detection and Large Language Model Meta AI (LLaMA) for natural language processing, our optimizer filters irrelevant information, prioritizing essential navigational cues for users.

## Problem Statement:
Visually impaired individuals often struggle with information overload when using smart glasses for navigation. Our aim is to develop a user-centered design that focuses on crucial cues while eliminating unnecessary information.

## Approach:
Our solution integrates a multi-objective Particle Swarm Optimization (PSO) based optimizer into smart glasses. The hardware configuration includes an Arduino Uno-based CPU, ESP8266 Wi-Fi module for real-time updates, and a CMOS OV7670 Camera Module for image capture. Additionally, an A9G Board with XIAO-ESP32 C3 facilitates emergency SOS functionality. YOLOv8 and LLaMA enhance object detection and natural language processing capabilities, respectively.

## Usage:
1. **Hardware Setup**: Connect components as per provided diagrams.
2. **Software Configuration**: Utilize Arduino IDE for coding modules and customize hyperparameters for YOLOv8.
3. **Integration**: Implement PSO-based optimizer and LLaMA for intelligent filtering and natural language understanding.
4. **Customization**: Users can adjust confidence levels to prioritize information according to individual preferences.
5. **Deployment**: Utilize TorchScript for mobile deployment and Django Rest Framework (DRF) for building WebAPIs.

## Key Features:
1. **Intelligent Filtering**: Prioritizes crucial navigational signals and objects in real-time.
2. **Enhanced Suggestions**: Utilizes databases and GPS data to provide intelligent suggestions on nearby points of interest.
3. **Customizable Priorities**: Users can adjust confidence levels to tailor information to their preferences.

## Conclusion:
Our Smart Glasses Optimizer represents a significant advancement in aiding visually impaired individuals, offering a streamlined and intelligent navigation experience. By combining cutting-edge technology with user-centric design, we strive to enhance accessibility and independence for all users.