import cv2
import numpy as np

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Convert the image to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to the image
    blurred =  cv2.GaussianBlur(gray,(5, 5), 0)

    # Create a binary thresholded image
    _, threshold = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY_INV)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate over the contours and draw a rectangle around any contour that is a rectangle
    for contour in contours:
        # Get the bounding rectangle of the contour
        x, y, w, h = cv2.boundingRect(contour) 
        aspectRatio = float(w)/h
        # Check if the aspect ratio of the contour is close to 1, indicating it is a rectangle
        if 0.95 <= aspectRatio <= 1.05:
            if h>50:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0,0,0), 2)

    # Show the webcam feed with the rectangles drawn on it
    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
