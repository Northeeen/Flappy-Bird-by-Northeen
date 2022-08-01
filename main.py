import numpy as np
import random
import cv2
import time

class Bird:
    def __init__(self):
        self.vel = -1
        self.hgt = 400

    def flap(self):
        self.hgt += 10
        self.vel = -.8

    def grav(self):
        if self.vel < .4:
            self.vel += .01
        elif self.vel > .4 and self.vel < .8:
            self.vel += .015

        self.hgt -= self.vel

class Pipe:
    def __init__(self, low, high):
        self.hgt = random.randint(low + 100, high - 100)
        self.vel = .5
        self.dist = 1000

    def move(self):
        self.dist -= self.vel

cv2.namedWindow("FlappyBird By North")
while True:
    points = 0

    MyBird = Bird()
    MyPipe = Pipe(0, 500)

    while True:
        arr = np.zeros(
        (500,1000,3),
        "uint8"
        )

        if MyPipe.dist < 0:
            MyPipe = Pipe(0, 500)
            points += 2

        arr[0 : int(MyPipe.hgt * -1) - 40, int(MyPipe.dist) : int(MyPipe.dist) + 50] = [75, 0, 130]
        arr[int(MyPipe.hgt * -1) + 40 : -1, int(MyPipe.dist) : int(MyPipe.dist) + 50] = [220, 20, 60]

        arr[int(MyBird.hgt * -1) : int(MyBird.hgt * -1) + 25, 50 : 100] = [255, 255, 146]

        if [255, 255, 255] in arr[int(MyPipe.hgt * -1) + 40 : -1, int(MyPipe.dist) : int(MyPipe.dist) + 50]:
            time.sleep(.2)
            break
        elif [255, 255, 255] in arr[0 : int(MyPipe.hgt * -1) - 40, int(MyPipe.dist) : int(MyPipe.dist) + 50]:
            time.sleep(.2)
            break

        MyBird.grav()
        MyPipe.move()

        if MyBird.hgt - 10 > np.size(arr, axis = 0) or MyBird.hgt + 10 < 0:
            break

        cv2.putText(
            arr,
            f'Points: {points}',
            (10,30), # Bottom Left Corner Of Text
            cv2.FONT_HERSHEY_SIMPLEX,  # Font
            .75, # Font scale
            (55,155,255), # Font color
            1 # Line type
        )

        cv2.imshow("FlappyBird By North", arr)
        key = cv2.waitKey(1)

        if key == 27: # exit on ESC
            break
        elif key == 32:
            MyBird.flap()


    if key == 27: # exit on ESC
        break

cv2.destroyWindow("FlappyBird By North")
