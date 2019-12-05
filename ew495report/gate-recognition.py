cap=cv2.VideoCapture(0) #connect camera
cv2.createTrackbar #create trackbars to adjust HSV values

While True:
    cap.read() #read video feed from camera
    Hsv=cv2.cvtColor #convert RGB to HSV
    Mask = cv2.inRange #mask out everything but gate
    Edges=cv2.findContours #find number of edges
    area=cv2.contourArea #find area of objects
    if area &gt; 400:
        cv2.drawContours #draw edges on video feed
        If len(Edges) == 8: #find the gate
            Print("Gate found")

    cv2.imshow("Mask", mask) #show masked image
    cv2.imshow("Frame", frame) #show feed with edges
