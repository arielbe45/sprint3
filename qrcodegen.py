import struct

import segno
import os
import cv2 as cv
import time

QRSIZE = 256

bytes = (b'Your mom is very nice Your mom is very nice Your mom is very nice Your mom is very nice Your mom is very'
         b' nice Your mom is very nice Your mom is very nice Your mom is very nice Your mom is very nice Your mom is'
         b' very nice Your mom is very nice Your mom is very nice Your mom is very nice Your mom is very nice Your'
         b' mom is very nice')


def split_bytes_into_chunks(byte_data, chunk_size):
    """Split a byte array into chunks of specified size."""
    for i in range(0, len(byte_data), chunk_size):
        yield byte_data[i:i + chunk_size]


def show_qr_sequence(data: bytes, chunk_size=QRSIZE-2):
    chunks = list(split_bytes_into_chunks(data, chunk_size))
    for i, chunk in enumerate(chunks):
        split_data = struct.pack('i', i) + struct.pack('i', len(chunk)) + chunk + bytearray(QRSIZE - 2 - len(chunk))
        qr = segno.make_qr(split_data)
        qr.save("qr.png", scale=15)
        # cv.namedWindow("QR", cv.WND_PROP_FULLSCREEN)
        # cv.setWindowProperty("QR", cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)
        cv.imshow('QR', cv.imread('qr.png'))
        cv.moveWindow('QR', 10, 10)
        cv.waitKey(3000)
    os.remove('qr.png')


show_qr_sequence(bytes)
