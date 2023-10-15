import cv2 as cv

def recale(frame , scale = 0.75):
    w = int(frame.shape[1] * scale)
    h = int(frame.shape[0] * scale)

    dime = (w,h)


    return cv.resize(frame , dime , interpolation=cv.INTER_AREA)
# reading photo

# img = cv.imread('photo/1.jpg')
# imgr  = recale(img,0.2)

# cv.imshow('cat' , img)
# cv.imshow('1 1 ' , imgr)

# reading video


# capture = cv.VideoCapture(0)

# while True:
#     isTrue , frame = capture.read()
#     framere = recale(frame , 2)
#     cv.imshow('video', frame)
#     cv.imshow('video frame', framere)


#     if cv.waitKey(20) &  0XFF == ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()

cv.waitKey(0)