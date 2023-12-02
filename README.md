# README for CTScanner MATLAB App

## Introduction
The CTScanner MATLAB app is designed to simulate a virtual CT (Computed Tomography) scanner. It allows users to generate various phantoms (models of objects to be scanned), operate a virtual scanner with different parameters, reconstruct images from the scanned data, and analyze these images.

## Preparing the Execution Environment

### Prerequisites
- **MATLAB**: The app is developed in MATLAB, so ensure you have MATLAB installed. This app was developed with MATLAB [R2023b], but it should be compatible with most recent versions.
- **Image Processing Toolbox**: This app utilizes MATLAB's Image Processing Toolbox. Ensure this toolbox is installed.

### Installation
1. **MATLAB Installation**: If MATLAB is not installed, download and install it from the [official MATLAB website](https://www.mathworks.com/products/matlab.html).
2. **Image Processing Toolbox**: To install the Image Processing Toolbox, use MATLAB's Add-On Explorer or install it during the MATLAB installation process.

## Running the Code
1. **Open MATLAB**: Start MATLAB and navigate to the directory where the CTScanner app code is saved.
2. **Open the App**: Open the `CTScanner.mlapp` file in MATLAB.
3. **Run the App**: Press the 'Run' button in MATLAB's editor to start the app. The CTScanner interface should appear.

## Using the App
1. **Phantom Generation**: Choose the type of phantom (Circular, Rectangular, Head Phantom) and adjust the Matrix Size, Structure Size, and Color as needed. Click 'Show Phantom' to display it.
2. **Scanner Controls**: Adjust scanner parameters like the Number of Detectors, Detector Density, Source Distance, Detector Array Type, and Rotation Step Angle. Click 'Run' to simulate scanning and reconstruct the image.
3. **Image Analysis**: Choose the type of analysis (SI and Contrast, Image Difference, SI Profiles) to perform on the generated or reconstructed images.

## Datasets and Database Repositories
This app does not require external datasets or database repositories as it generates phantoms internally for simulation.

## Additional Notes
- Ensure all prerequisites are met before running the app.
