import pyautogui as auto
import numpy as np
import cv2 as cv
import win32gui, win32ui, win32con

def windowCapture(x, y):

    w = x
    h = y

    # hwnd = win32gui.FindWindow(None, windowName)
    hwnd = None
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0), (w, h), dcObj, (0, 0), win32con.SRCCOPY)

    signedIntArray = dataBitMap.GetBitmapBits(True)
    img = np.fromstring(signedIntArray, dtype='uint8')
    img.shape = (h, w, 4)

    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())

    img = img[...,:3]
    img = np.ascontiguousarray(img)

    return img


