import cv2
import numpy as np
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Range for lower red
    red_lower = np.array([0, 120, 70])
    red_upper = np.array([10, 255, 255])
    mask_red1 = cv2.inRange(hsv_frame, red_lower, red_upper)
    # Range for upper range
    red_lower = np.array([170, 120, 70])
    red_upper = np.array([180, 255, 255])
    mask_red2 = cv2.inRange(hsv_frame, red_lower, red_upper)
    # daha iyi renk tanıması için lower ve upper için iki ayrı mask tanımladık ve topladık

    mask_red = mask_red1 + mask_red2
    red_output = cv2.bitwise_and(frame, frame, mask=mask_red)


    # blue
    yellow_lower = np.array([20, 100, 100])
    yellow_upper = np.array([30, 255, 255])
    yellow_mask = cv2.inRange(hsv_frame, yellow_lower, yellow_upper)
    yellow = cv2.bitwise_and(frame, frame, mask = yellow_mask)


    cv2.imshow("Webcam", frame)
    # cv2.imshow("Green Mask", green_mask)
    cv2.imshow("Yellow", yellow)
    cv2.imshow("Red", red_output)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()