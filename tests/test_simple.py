import pytest
from .context import preprocess

def test_tautology():
    assert True == True and False == False

def test_greyscale():
    from cv2 import imread, IMREAD_GRAYSCALE
    from numpy import allclose

    img = imread("res/test.png")
    img = preprocess.greyscale(img)
    greyscale = imread("res/greyscale.png", IMREAD_GRAYSCALE)

    assert allclose(img, greyscale)

def test_gblur():
    from cv2 import imread, IMREAD_GRAYSCALE
    from numpy import allclose

    img = imread("res/test.png")
    img = preprocess.gblur(img)
    gblur = imread("res/gblur.png")

    assert allclose(img, gblur)

def test_sobelxy():
    pass

def test_houghtransform():
    pass

