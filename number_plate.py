import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

cascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")

state_names = {
    "AP": "Andhra Pradesh",
    "AR": "Arunachal Pradesh",
    "AS": "Assam",
    "BR": "Bihar",
    "BH": "Bharat",
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
    "WB": "West Bengal",
    "BH": "Bharat"
}

district_codes = {
    "HR": {
        "01": "Ambala North",
        "02": "JAGADHRI",
        "03": "Panchkula",
        "04": "Naraingarh",
        "05": "Karnal",
        "06": "Panipat",
        "07": "Thanesar",
        "08": "Kaithal",
        "09": "Guhla",
        "10": "Sonipat",
        "11": "Gohana",
        "12": "Rohtak",
        "13": "Bahadurgarh",
        "14": "Jhajjar",
        "15": "Meham",
        "16": "Bhiwani",
        "17": "Siwani",
        "18": "Loharu",
        "19": "Charkhi Dadri",
        "20": "Hisar",
        "21": "Hansi",
        "22": "Fatehabad",
        "23": "Tohana, Jakhal Mandi",
        "24": "Sirsa",
        "25": "Mandi Dabwali",
        "26": "Gurugram",
        "27": "Nuh",
        "28": "Ferozepur Jhirka",
        "29": "Ballabgarh (Faridabad South)",
        "30": "Palwal",
        "31": "Jind",
        "32": "Narwana",
        "33": "Safidon",
        "34": "Mahendragarh",
        "35": "Narnaul",
        "36": "Rewari",
        "37": "Ambala",
        "38": "Faridabad",
        "39": "Hisar",
        "40": "Assandh",
        "41": "Pehowa",
        "42": "Ganaur",
        "43": "Kosli",
        "44": "Ellenabad",
        "45": "Karnal",
        "46": "Rohtak",
        "47": "Rewari",
        "48": "Tosham",
        "49": "Kalka",
        "50": "Hodal",
        "51": "Faridabad (Faridabad North)",
        "52": "Hathin",
        "53": "Adampur",
        "54": "Barara",
        "55": "Gurugram",
        "56": "Jind",
        "57": "Sirsa",
        "58": "Yamunanagar",
        "59": "Ratia",
        "60": "Samalkha",
        "61": "Bhiwani",
        "62": "Fatehabad",
        "63": "Jhajjar",
        "64": "Kaithal",
        "65": "Kurukshetra",
        "66": "Narnaul",
        "67": "Panipat",
        "68": "Panchkula",
        "69": "Sonipat",
        "70": "Chandigarh",
        "71": "Bilaspur",
        "72": "Gurugram",
        "73": "Palwal",
        "74": "Nuh",
        "75": "Indri",
        "76": "Pataudi",
        "77": "Beri",
        "78": "Shahabad Markanda",
        "79": "Kharkhoda",
        "80": "Barwala",
        "81": "Bawal",
        "82": "KANINA",
        "83": "Kalayat",
        "84": "Charkhi Dadri",
        "85": "Ambala CANTT South",
        "86": "Narnaund",
        "87": "Badkhal (Faridabad West)",
        "88": "Badhra",
        "89": "Badli",
        "90": "Uchana",
        "91": "Gharaunda",
        "92": "Radaur",
        "93": "Punhana",
        "94": "Kalanwali",
        "95": "Sampla",
        "96": "Tauru",
        "97": "Ladwa",
        "98": "Badshahpur",
        "99": "Haryana"
    },
    "MH": {
        "01": "Mumbai (South)",
        "02": "Mumbai (West)",
        "03": "Mumbai (East)",
        "04": "Thane",
        "05": "Kalyan",
        "06": "Pen (Raigad)",
        "07": "Sindhudurg",
        "08": "Ratnagiri",
        "09": "Kolhapur",
        "10": "Sangli",
        "11": "Satara",
        "12": "Pune",
        "13": "Solapur",
        "14": "Pimpri-Chinchwad",
        "15": "Nashik",
        "16": "Ahilyanagar",
        "17": "Shrirampur",
        "18": "Dhule",
        "19": "Jalgaon",
        "20": "Chhatrapati Sambhajinagar",
        "21": "Jalna",
        "22": "Parbhani",
        "23": "Beed",
        "24": "Latur",
        "25": "Osmanabad",
        "26": "Nanded",
        "27": "Amravati",
        "28": "Buldhana",
        "29": "Yavatmal",
        "30": "Akola",
        "31": "Nagpur (City)",
        "32": "Wardha",
        "33": "Gadchiroli",
        "34": "Chandrapur",
        "35": "Gondia",
        "36": "Bhandara",
        "37": "Washim",
        "38": "Hingoli",
        "39": "Nandurbar",
        "40": "Nagpur (Rural)",
        "41": "Malegaon",
        "42": "Baramati",
        "43": "Vashi (Navi Mumbai)",
        "44": "Ambajogai",
        "45": "Akluji",
        "46": "Panvel",
        "47": "Borivali",
        "48": "Vasai",
        "49": "Nagpur (East)",
        "50": "Karad",
        "51": "Nashik (Rural)",
        "52": "Parbhani (Rural)",
        "53": "Pune (South)",
        "54": "Pune (North)",
        "55": "Mumbai (Central)",
        "56": "Thane (Rural)"
    }
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
        district_code = read[2:4]

        try:
            print("Car Belongs TO:", state_names[stat])
            print("District:", district_codes[stat][district_code])
        except KeyError:
            print("State or district not recognized!!!")
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
