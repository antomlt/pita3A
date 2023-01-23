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
cv2.imshow("Gray", gray)

# Apply Gaussian blur to the image
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
cv2.imshow("Blurred", blurred)

# Use the Canny edge detection algorithm to detect edges in the image
edges = cv2.Canny(blurred, 50, 150)
cv2.imshow("Edges", edges)

# Define the lower and upper bounds of the black color in the HSV color space
lower_black = np.array([0, 0, 0])
upper_black = np.array([180, 255, 30])

# Convert the image to the HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Create a mask that only selects pixels that fall within the lower and upper bounds of the black color
mask = cv2.inRange(hsv, lower_black, upper_black)
cv2.imshow("Mask", mask)

# Use the HoughLinesP function to detect lines in the image
lines = cv2.HoughLinesP(mask, 1, np.pi/180, 100, minLineLength=5, maxLineGap=0.2)

# Iterate over the lines and draw only the big lines on the result image in red
for line in lines:
    x1, y1, x2, y2 = line[0]
    lenght = np.sqrt((x2-x1)**2+(y2-y1)**2)
    if lenght >= 100:
        cv2.line(result, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Show the result image with the big lines drawn on it
cv2.imshow("Big Lines", result)
cv2.imshow("Result on image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
