import cv2
import serial

# Initialize the Arduino serial connection
arduino = serial.Serial(port = "COM4", baudrate=9600)  # Replace "COM3" with your Arduino's port

# Load the pre-trained Haarcascade for face detection
face_cascade = cv2.CascadeClassifier('C:\\Users\\nitis\\Desktop\\faceTest\\haarcascade_frontalface_default.xml')

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        # Calculate the center of the detected face
        face_center_x = x + w // 2
        face_center_y = y + h // 2

        # Send face position data to Arduino
        arduino.write(f'{face_center_x},{face_center_y}\n'.encode())

        # Draw a green rectangle around the detected face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Face Tracking', frame)
    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()
