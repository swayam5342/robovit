import cv2
import cv2.data
face_cas = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

def main() -> int:
    while True:
        ret,fram = cap.read()
        if(not ret):
            return -1
                


if __name__ == "__main__":
    main()
