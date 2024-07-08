import cv2
import dir_to_bytes
import base64

global collected_data
global last_index
collected_data = dict()
last_index = -1


def add_data(qr_data):
    global last_index
    global collected_data
    if len(qr_data) < 2:
        return False
    code_index = int(qr_data[0])
    code_length = int(qr_data[1])
    size = 8
    if code_length!=0:
        size = code_length

    data = qr_data[2:size+2]
    if (code_index in collected_data):
        return False
    else:
        print("Got QR number ", code_index)
        print(data)
        collected_data[code_index] = data
    
    if code_length != 0:
        last_index = code_index
        print("Finished pass, missing data: ", get_missing_data())
    if last_index != -1 and len(get_missing_data()) == 0:
        return True
    

def get_missing_data():
    return [x for x in range(0, last_index) if x not in collected_data.keys()]

# if code_length != 254:
#     return True


def process_data():
    global collected_data
    global last_index
    data = bytearray()
    print(collected_data)
    for i in range(0, last_index+1):
        data.extend(collected_data[i])
    print(data)
    decoded_data = base64.b64decode(data)
    print(decoded_data)
    dir_to_bytes.bytes_to_folder(decoded_data, 'TestFolder')
