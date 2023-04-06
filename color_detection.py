
import cv2,math
import pandas as pd
from playsound import playsound 
import numpy as np 
import matplotlib.pyplot as plt


img = cv2.imread('color.png')
sound = {'Red':'red.mp3','Green':'green.mp3','Blue':'blue.mp3','Yellow':'yellow.mp3','Black':'black.mp3','White':'white.mp3','Pink':'pink.mp3',}

plt.imshow(img)
plt.title('input')
plt.show()

kernel = np.ones((5,5),np.float32)/25
filterdimg = cv2.filter2D(img,-1,kernel)

plt.imshow(filterdimg)
plt.title('filtered image')
plt.show()

# declaring global variables (are used later on)
clicked = False
r = g = b = x_pos = y_pos = 0

# Reading csv file with pandas and giving names to each column
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv("C:/Users/user/projects/progaming/Color-Detection-OpenCV/colors.csv", names=index)

# function to calculate minimum distance from all colors and get the most matching color
def get_color_name(R, G, B):
    distance = math.inf
    for i in range(len(csv)):
        cur_distance = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if cur_distance <= distance:
            distance = cur_distance
            cname = csv.loc[i, "color_name"]
    
    return cname


# function to get x,y coordinates of mouse double click
def draw_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global b, g, r, x_pos, y_pos, clicked
        clicked = True
        x_pos = x
        y_pos = y
        b, g, r = filterdimg[y, x]
        b = int(b)
        g = int(g)
        r = int(r)


cv2.namedWindow('Detact any color on this image by clicking on it',cv2.WINDOW_AUTOSIZE)
cv2.setMouseCallback('Detact any color on this image by clicking on it', draw_function)

while True:

    cv2.imshow("Detact any color on this image by clicking on it", filterdimg)
    if clicked:

        # cv2.rectangle(image, start point, endpoint, color, thickness)-1 fills entire rectangle
        cv2.rectangle(filterdimg, (20, 20), (700, 60), (b, g, r), -1)

        # Creating text string to display( Color name and RGB values )
        text = get_color_name(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
        # cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(filterdimg, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
        # For very light colours we will display text in black colour
        if r + g + b >= 600:
            cv2.putText(filterdimg, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        clicked = False
        adress = ''
        listText = text.split()
        for i in range(len(listText)):
            if listText[i] in sound:
                adress = sound[listText[i]]
                break
        if len(adress)>0:
            playsound(adress)
    # Break the loop when user hits 'esc' key
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()