import cv2
import numpy as np

# check if mouse button is pressed or not
pressed = False

def draw_mask(mouse, x, y, flags, param):

    """
    With the help of this function, user can draw a specialized mask
    for every picture he/she would like to mask.

    :param mouse: detects mouse's behaviors (such as button is down or up)
    :param x: x coordinate of the pixel that user clicked
    :param y: y coordinate of the pixel that user clicked
    :param flags: flags argument
    :param param: parameter argument
    :return: returns the mask
    """

    global pressed

    # if clicked
    if mouse == cv2.EVENT_LBUTTONDOWN:
        pressed = True

    elif mouse == cv2.EVENT_MOUSEMOVE or mouse == cv2.EVENT_LBUTTONUP:

        if pressed:
            # draw circles to create mask with the color white
            cv2.circle(img, (x, y), 10, (255, 255, 255), -1)

        # if not clicked
        if mouse == cv2.EVENT_LBUTTONUP:
            pressed = False


# create the size of mask
img = np.zeros((408, 612, 3), np.uint8)

# create the window to draw the mask
cv2.namedWindow('image')

# Warning! Press any character to see the result of the mask
# You can press any character in keyboard while you are drawing
cv2.setMouseCallback('image', draw_mask)

while True:

    cv2.imshow('image', img)
    k = cv2.waitKey(0) & 0xFF

    # press 'esc' to finish
    if k == 27:
        break

# save the mask
cv2.imwrite("mask.jpg", img)
cv2.destroyAllWindows()
