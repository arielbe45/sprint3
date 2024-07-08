import struct
import ctypes

import segno
import os
import cv2 as cv
from screeninfo import get_monitors
import numpy as np


QR_SIZE = 8

bytes = (b'Your mom is very nice Your mom is very nice Your mom is very nice Your mom is very nice Your mom is very'
         b' nice Your mom is very nice Your mom is very nice Your mom is very nice Your mom is very nice Your mom is'
         b' very nice Your mom is very nice Your mom is very nice Your mom is very nice Your mom is very nice Your'
         b' mom is very nice')

def get_screen_height():
    # Get the height of the primary monitor
    for monitor in get_monitors():
        if monitor.is_primary:
            return monitor.height
    return None


def resize_to_square(image, target_size):
    height, width = image.shape[:2]
    # Calculate the scaling factor
    scale = target_size / max(height, width)
    # Resize the image
    resized_image = cv.resize(image, (int(width * scale), int(height * scale)))
    # Create a new square image of the target size
    square_image = np.zeros((target_size, target_size, 3), dtype=np.uint8)
    # Center the resized image on the square background
    x_offset = (target_size - resized_image.shape[1]) // 2
    y_offset = (target_size - resized_image.shape[0]) // 2
    square_image[y_offset:y_offset+resized_image.shape[0], x_offset:x_offset+resized_image.shape[1]] = resized_image
    return square_image


def split_bytes_into_chunks(byte_data, chunk_size):
    """Split a byte array into chunks of specified size."""
    for i in range(0, len(byte_data), chunk_size):
        yield byte_data[i:i + chunk_size]


def set_hidden(file_path):
    """
    Make a file hidden
    :param file_path:
    :return:
    """
    FILE_ATTRIBUTE_HIDDEN = 0x02
    ret = ctypes.windll.kernel32.SetFileAttributesW(file_path, FILE_ATTRIBUTE_HIDDEN)
    if not ret:
        raise ctypes.WinError()


def set_visible(file_path):
    """
    Make a file visible
    :param file_path:
    :return:
    """
    FILE_ATTRIBUTE_NORMAL = 0x80
    ret = ctypes.windll.kernel32.SetFileAttributesW(file_path, FILE_ATTRIBUTE_NORMAL)
    if not ret:
        raise ctypes.WinError()


def show_qr_sequence(data: bytes):
    chunk_size = QR_SIZE - 2
    chunks = list(split_bytes_into_chunks(data, chunk_size))
    try:
        set_visible('qr.png')
        os.remove('qr.png')
    except:
        pass
    for j in range(2):  # Run the QR codes multiple times
        for i, chunk in enumerate(chunks):
            size = len(chunk) if i == len(chunks) - 1 else 0
            size_1 = size // 128
            size_2 = size % 128
            split_data = struct.pack('B', size_1) + struct.pack('B', size_2) + struct.pack('B', size) + chunk + bytearray(chunk_size - len(chunk))
            print(split_data)
            qr = segno.make_qr(split_data, encoding='none')
            qr.save("qr.png", scale=10)
            set_hidden("qr.png")
            cv.namedWindow("BG", cv.WND_PROP_FULLSCREEN)
            cv.setWindowProperty("BG", cv.WND_PROP_FULLSCREEN, cv.WINDOW_AUTOSIZE)
            cv.imshow('BG', 255 * np.ones((100, 100, 3), np.uint8))
            screen_height = get_screen_height()
            if screen_height is None:
                cv.imshow('QR', cv.imread('qr.png'))
            else:
                square_barcode = resize_to_square(cv.imread('qr.png'), screen_height)
                cv.imshow('QR', square_barcode)
            cv.moveWindow('QR', screen_height // 2, -40)
            if i == j == 0:
                cv.waitKey(500)
            cv.waitKey(800)
            set_visible('qr.png')
            os.remove('qr.png')
