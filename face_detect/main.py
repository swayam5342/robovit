from typing import Literal
import cv2
import cv2.data

face_cas = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

def main() -> None | Literal[-1]:
    while True:
        ret, fram = cap.read()
        if not ret:
            return -1
        gray = cv2.cvtColor(fram, cv2.COLOR_BGR2GRAY)
        face = face_cas.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        for (x, y, w, h) in face:
            cv2.rectangle(fram, (x, y), (x + w, y + h), (0, 0, 0), 2)
        cv2.imshow('fac', fram)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
