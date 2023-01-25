import cv2
import numpy as np

# Load the image
image = cv2.imread("Test_picture/Porte_2_test.png")
if image is None:
    print("Error: Image not found.")
    exit()

# Create a blank image with the same dimensions as the original image
result = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Gray", gray)

# Apply Gaussian blur to the image
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
#cv2.imshow("Blurred", blurred)

# Use the Canny edge detection algorithm to detect edges in the image
edges = cv2.Canny(blurred, 50, 150)
#cv2.imshow("Edges", edges)

# Define the lower and upper bounds of the WINDOW COLOR in the HSV color space  --> actual window color: Black
lower_black = np.array([0, 0, 0])
upper_black = np.array([180, 255, 30])

# Convert the image to the HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Create a mask that only selects pixels that fall within the lower and upper bounds of the black color
mask = cv2.inRange(hsv, lower_black, upper_black)
#cv2.imshow("Mask", mask)

# Find contours in the mask
contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Iterate over the contours and draw a rectangle around any contour that is a window-like shape
for contour in contours:
    # Get the bounding rectangle of the contour
    x, y, w, h = cv2.boundingRect(contour)
    aspectRatio = float(w)/h
    # Check if the aspect ratio of the contour is close to 1.5, indicating it is window-like shape
    if 1.2 <= aspectRatio <= 2:
        cv2.rectangle(image, (x, y), (x + w, y + h), (330, 0, 0), 2)
        if h>100:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

# Show the image with the windows drawn on it
cv2.imshow("Windows", image)
cv2.waitKey(0)
cv2.destroyAllWindows()