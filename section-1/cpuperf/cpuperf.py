import cv2
import numpy
import os


def calculate_histogram(photo_):
    bins = numpy.zeros(256, numpy.int32)

    for i in range(photo_.shape[0]):
        for j in range(photo_.shape[1]):
            bins[photo_[i][j]] += 1

    return bins


if __name__ == "__main__":
    photo_directory = os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", "downloaded")

    photo_list = [cv2.imread(x.path, cv2.IMREAD_GRAYSCALE) for x in os.scandir(photo_directory) if
                  x.path.endswith(".jpg")]
    for photo in photo_list:
        calculate_histogram(photo)
