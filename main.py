import cv2
import numpy as np

cap = cv2.VideoCapture("Fumefx colored smoke.mp4")

while True:
    _, frame = cap.read()

    # hsv: Hue, Saturation, Value
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)



    lower_green = np.array([100, 79, 0])
    upper_green = np.array([1135, 255, 255])

    # Converts color to an HSV color
    # dark_yellow = np.unit8([[[12,22,121]]])
    # dark_yellow = cv2.cvtColor(dark_yellow,cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_green, upper_green)
    # cv2.bitwise_and: If the mask is in the range of lower to upper then its the bit value of 1, All 1's are shown as the color from the frame

    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Shows the frame
    cv2.imshow("frame", frame)
    # Mask shows unneeded objects black while highlighting what you need white
    cv2.imshow("mask", mask)
    # Mask shows unneeded objects black while highlighting what you need white
    cv2.imshow("res", res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()  # ends camera/video use even in the background