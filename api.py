import face_recognition
from PIL import Image, ImageTk
import os
import cv2 as cv
import time

BASE_DIR = os.getcwd()
dir_path = os.path.join(BASE_DIR, 'test_image')


def crop_image(dir_image):
    image = face_recognition.load_image_file(dir_image)
    face_locations = face_recognition.face_locations(image)
    print(face_locations)

    print("I found {} face(s) in this photograph.".format(len(face_locations)))

    for face_location in face_locations:
        # Print the location of each face in this image
        top, right, bottom, left = face_location
        print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(
            top, left, bottom, right))

        # You can access the actual face itself like this:
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_image.show()

    return True


def read_file_from_folder(dir_path):
    files = os.listdir(dir_path)
    for file in files:
        img_path = os.path.join(dir_path, file)
        image = cv.imread(img_path, cv.IMREAD_GRAYSCALE)
        cv.imshow('image', image)
        cv.waitKey(3000)
    cv.destroyAllWindows()
    return True


def get_list_file_path_from_folder(dir_path):
    files = os.listdir(dir_path)
    list_file_path = []
    for file in files:
        img_path = os.path.join(dir_path, file)
        list_file_path.append(img_path)
    return list_file_path

# read_file_from_folder(dir_path)
# list_file_path = get_list_file_path_from_folder(dir_path)
# for file_path in list_file_path:
#     crop_image(file_path)
