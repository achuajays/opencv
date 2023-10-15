import cv2 as cv


# reading photo

# img = cv.imread('photo/1.jpg')

# cv.imshow('cat' , img)

# reading video


capture = cv.VideoCapture('video/1.mkv')

while True:
    isTrue , frame = capture.read()
    cv.imshow('video', frame)

    if cv.waitKey(20) &  0XFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()


cv.waitKey(0)