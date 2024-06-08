# Room Light AI

This project is designed to control room lighting using hand gestures detected through AI and WebSocket communication. 
It is divided into several components, including backend processing, user interface, and ESP32 microcontroller setup.

# Components
## Backend
The backend component handles the AI processing for hand gesture detection. It consists of the following files:
- `handtrackpy`: Contains the hand tracking logic using `OpenCV` and `cvzone`.
- `server.py`: Sets up a server to handle WebSocket communication with the ESP32 Microcontroller.

## ESP32 (Room light)
The ESP32 microcontroller is programmed to control the room lights based on commands received via WebSocket.
The code is located in the `room-light` directory and includes the following:
- `platformio.ini`: Configuration file for PlatformIO.
- `src/main.cpp`: The main program file for the ESP32.
- `src/*.cpp`: The WebSockets files.

## User Interface
The user interface is designed to provide a web-based control panel for the room light system. 
The code for the user interface is located in the user-interface directory.

# Getting Started
## Prerequisities
- Python
- PlatformIO
- ESP32

## Installation
1. Clone the Repository:
   ```
   git clone https://github.com/Luffeee/hand-light-control.git
   cd hand-light-control
   ```
2. Setup the Backend:
   - Navigate to the `backend` directory and run:
     ```
     uvicorn server:app --reload
     ```
3. Program the ESP32:
   - Navigate to the `room-light` directory and upload the main.cpp code to the ESP32.

# Usage
Use hand gestures to control the room lights. The backend AI processes the gestures and sends commands to the ESP32, 
which then controls the lights. Access the web-based control panel to manually control the lights.
Open your hand to turn on the lights and close your hand to turn it off.
