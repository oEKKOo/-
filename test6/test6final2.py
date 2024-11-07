import cv2
import numpy as np

# Capture video from the webcam
cap = cv2.VideoCapture(0)

while True:
    # Get each frame
    ret, frame = cap.read()
    
    # Convert frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define the blue color range in HSV
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    
    # Create a mask to detect blue objects
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    # Perform morphological operations to clean up the mask
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.dilate(mask, kernel, iterations=2)
    
    # Find contours to detect the shape of the object
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw a rectangle around the detected object
    if len(contours) > 0:
        # Find the largest contour
        max_contour = max(contours, key=cv2.contourArea)
        
        # Get the bounding rectangle for the largest contour
        x, y, w, h = cv2.boundingRect(max_contour)
        
        # Draw the rectangle around the blue object
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Display the original frame and the mask
    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', mask)
    
    # Press 'Esc' to exit
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# Release the video capture object and close windows
cap.release()
cv2.destroyAllWindows()

