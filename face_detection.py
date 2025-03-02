import cv2
import numpy as np

def detect_face_shape(image_path):
    # Load OpenCV's pre-trained face detection model
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face = image[y:y+h, x:x+w]
        gray_face = gray[y:y+h, x:x+w]

        edges = cv2.Canny(gray_face, 100, 200)
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            contour = max(contours, key=cv2.contourArea)
            perimeter = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)

            if len(approx) >= 8:
                return "Oval"
            elif len(approx) == 4:
                return "Square"
            elif len(approx) > 4 and len(approx) < 8:
                return "Round"
            else:
                return "Unknown"

    return "No face detected"
