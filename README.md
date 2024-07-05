# Automatic License Plate Recognition System

## Overview

This project is an Automatic License Plate Recognition (ALPR) system that uses computer vision and the EasyOCR library to detect and read license plate numbers from video footage, and then saves the results into a CSV file. The system consists of four main files:

- `main.py`
- `utils.py`
- `add_missing_data.py`
- `visualize.py`

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
