# License-plate-recognition-system
Introduction:
This is a Python implementation of a license plate recognition system using OpenCV and Tesseract OCR. The system is designed to detect license plates in images and extract the alphanumeric characters from them. Additionally, it tries to determine the state associated with the license plate number based on predefined state codes.

Requirements:
- Python 3.x
- OpenCV (cv2)
- Tesseract OCR
- pytesseract
- Haar cascade classifier for license plate detection (e.g., haarcascade_russian_plate_number.xml)
- Image containing one or more vehicles with visible license plates

Installation:
1. Install Python 3.x from python.org.
2. Use "pip install opencv-python" to install OpenCV.
3. Install Tesseract OCR from tesseract-ocr.
4. Use "pip install pytesseract" to install pytesseract.
5. Download the Haar cascade classifier XML file for license plate detection and place it in the project directory.

Usage:
1. Clone or download this repository to your local machine.
2. Navigate to the project directory.
3. Make sure all the requirements are installed.
4. Run the "license_plate_recognition.py" script and provide the path to the image file containing the vehicle(s) with license plates.

Example:
number_plate.py hr.jpeg

Output:
The system will process the input image, detect license plates, and extract text from them.
For each detected license plate, the system will try to determine the corresponding state based on the license plate number and display the result.
The modified image, with highlighted license plate regions and overlaid extracted text, will be shown.
The modified image will also be saved as "result.jpeg" in the project directory.

Notes:
- Make sure the input image has clear and visible license plates for accurate detection and recognition.
- Performance may vary depending on image quality, lighting conditions, and vehicle angle.
- State identification is based on predefined state codes and may not always be precise.
- Adjust parameters and preprocessing techniques as needed to enhance detection and recognition.
