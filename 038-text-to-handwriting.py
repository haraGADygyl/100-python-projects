import pywhatkit
import cv2

# pywhatkit.image_to_ascii_art("resources/4.jpg", "resources/4")

pywhatkit.text_to_handwriting("Test string to handwriting\nAnother string here\nAnd last line here",
                              save_to="resources/handwriting.png")


img = cv2.imread("resources/handwriting.png")

cv2.imshow("Text to handwriting", img)
cv2.waitKey()
cv2.destroyAllWindows()
