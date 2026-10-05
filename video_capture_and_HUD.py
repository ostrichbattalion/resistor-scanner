import numpy
import cv2 as cv
import json


line_color_dict = {}
cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()


def line_color_to_file(line_color_dict):
    
    with open('line_of_color.json','w',) as f:
        json.dump(line_color_dict,f)
        

while True:
    ret, frame_raw = cap.read()
    frameHUD = frame_raw.copy()

    if not ret:
        print("Can't receive frame_raw (stream end?). Exiting ...")
        break


    height, width = frame_raw.shape[:2]
    center_y = height // 2
    line_length = 200

    start_x = (width // 2) - (line_length // 2)
    end_x = (width // 2) + (line_length // 2)

    # Draw the horizontal line and define view portal
    HUD = cv.line(frameHUD, (start_x, center_y), (end_x, center_y), (51, 255, 51), 1)


    key = cv.waitKey(1)
    if key == ord('p'):
    
        for x in range(start_x, end_x):# Iterate over the pixels along the line to get BGR color values

            b, g, r = frame_raw[center_y, x]  # Access BGR values at row=center_y, col=x
            """store the pixles color data and use that to interpret the risitor value"""
            #print(f"Pixel at ({x}, {center_y}): B={b}, G={g}, R={r}")
            line_color_dict.update({x:(int(b),int(g),int(r))})
        
        cv.imwrite("C:/dev/projects/Resistor_scanner/images/testimg_raw.png", img=frame_raw)
        cv.imwrite("C:/dev/projects/Resistor_scanner/images/testimgHUD.png", img=frameHUD)
        line_color_to_file(line_color_dict)
    
    if key == ord('q'):
        line_color_to_file(line_color_dict)
        break

    # Display the frame with the line
    cv.imshow('Camera name', HUD)



cap.release()
cv.destroyAllWindows()






 