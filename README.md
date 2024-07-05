# Automatic License Plate Recognition System

## Overview

This project is an Automatic License Plate Recognition (ALPR) system that uses computer vision and the EasyOCR library to detect and read license plate numbers from video footage, and then saves the results into a CSV file. The system consists of four main files:

- `main.py`
- `utils.py`
- `add_missing_data.py`
- `visualize.py`

# Dataset
The dataset used in this project is [here](https://universe.roboflow.com/roboflow-universe-projects/license-plate-recognition-rxg4e/dataset/4).

## Workflow

1. **Vehicle and License Plate Detection**: `main.py`
2. **Add Missing Data**: `add_missing_data.py`
3. **Visualize Results**: `visualize.py`

## File Descriptions

### main.py

This is the main file of the project. It detects vehicles and license plates in the input video, uses functions from `utils.py` for text extraction, and creates a CSV file with the results.

### utils.py

This file contains utility functions for the project, including functions for OCR (Optical Character Recognition) and license plate detection.

### add_missing_data.py

This file processes the initial CSV file created by `main.py` to add any missing data that might have been missed in the initial detection phase.

### visualize.py

This file processes the input video to create an output video with the detected license plates highlighted.

## Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/miteshgupta07/Automatic-Number-Plate-Recognition-System.git
   cd <repository-directory>

2. **Install the required libraries:**
   ```bash
   pip install -r requirements.txt

3. **Ensure you have the necessary video files in the correct directory.**

## How to Run

1. **Run the main script:** 
   ```bash
   python main.py
   
This will detect vehicles and license plates in the input video and create an initial CSV file with the results.

2. **Run the add_missing_data script:**
   ```bash
   python add_missing_data.py
   
This will process the initial CSV file to add any missing data.

3. **Run the visualize script:**

   ```bash
   python visualize.py

This will process the input video and create an output video with the detected license plates highlighted.

# Acknowledgements
This project was made possible by the use of a dataset from [Roboflow](https://roboflow.com/). Their comprehensive and high-quality dataset greatly facilitated the development and testing of the license plate recognition system.

# Contributing
Feel free to submit issues or pull requests if you have any suggestions or improvements.

# License
This project is licensed under the MIT License.
