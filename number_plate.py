import numpy as np
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

cascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")

state_names = {
    "AP": "Andhra Pradesh",
    "AR": "Arunachal Pradesh",
    "AS": "Assam",
    "BR": "Bihar",
    "BH":"Bharat",
    "CG": "Chhattisgarh",
    "GA": "Goa",
    "GJ": "Gujarat",
    "HR": "Haryana",
    "HP": "Himachal Pradesh",
    "JH": "Jharkhand",
    "KA": "Karnataka",
    "KL": "Kerala",
    "MP": "Madhya Pradesh",
    "MH": "Maharashtra",
    "MN": "Manipur",
    "ML": "Meghalaya",
    "MZ": "Mizoram",
    "NL": "Nagaland",
    "OD": "Odisha",
    "PB": "Punjab",
    "RJ": "Rajasthan",
    "SK": "Sikkim",
    "TN": "Tamil Nadu",
    "TG": "Telangana",
    "TR": "Tripura",
    "UP": "Uttar Pradesh",
    "UK": "Uttarakhand",
    "WB": "West Bengal"
}

def dectract_num(img_name):
    # reading the image 
    img = cv2.imread(img_name)
    # converting image into gray image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    nplate = cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in nplate:
        # croping the number plate from car image
        a, b = (int(0.02*img.shape[0]), int(0.025*img.shape[1]))
        plate = img[y+a:y+h-a, x+b:x+w-b, :]

        # image processing
        plate_gray = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)
        _, plate = cv2.threshold(plate_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        # image to string 
        read = pytesseract.image_to_string(plate)
        read = "".join(e for e in read if e.isalnum())
        stat = read[0:2]
        try:
            print("Car Belongs TO:", state_names[stat])
        except KeyError:
            print("State not recognized!!!")
        print(read)

        cv2.rectangle(img, (x, y), (x+w, y+h), (51, 51, 255), 2)
        cv2.rectangle(img, (x, y-40), (x+w, y), (51, 51, 255), -1)
        cv2.putText(img, read, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        cv2.imshow("Plate", plate)

    cv2.imshow("result", img)
    cv2.imwrite("result.jpeg", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

dectract_num("hr.jpeg")
