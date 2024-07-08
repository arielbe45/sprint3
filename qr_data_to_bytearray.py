import cv2
import dir_to_bytes


global collected_data
global last_code_index
collected_data = bytearray()
last_code_index = -1


def add_data(qr_data):
    global last_code_index
    global collected_data

    
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
    
    # print(code_index, code_length, data)

    # if code_length != 254:
    #     return True


def process_data():
    print(collected_data)
