import cv2
import dir_to_bytes
import base64

global collected_data
global last_code_index
collected_data = bytearray()
last_code_index = -1


def add_data(qr_data):
    global last_code_index
    global collected_data
    print(qr_data)
    if len(qr_data) < 2:
        return False
    code_index = int(qr_data[0])
    code_length = int(qr_data[1])
    data = qr_data[2:code_length+2]
    if code_index == last_code_index:
        return False
    elif code_index == last_code_index + 1:
        print("Got QR number ", code_index)
        last_code_index = code_index
        collected_data.extend(data)
    elif code_index > last_code_index + 1:
        print("Missing QR code(s) in sequence")
    

    # if code_length != 254:
    #     return True


def process_data():
    decoded_data = base64.b64decode(collected_data)
    print(decoded_data)
    dir_to_bytes.bytes_to_folder(decoded_data, 'TestFolder')
