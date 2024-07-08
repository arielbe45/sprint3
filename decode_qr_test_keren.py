import cv2
import pyzxing

# Initialize the zxing decoder
reader = pyzxing.BarCodeReader()

def decode_barcode(image_path):
    result = reader.decode(image_path)
    return result

def main():
    # Open a connection to the webcam (0 is usually the built-in webcam)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Failed to grab frame.")
            break

        # Display the resulting frame
        cv2.imshow('Webcam', frame)

        # Save the frame as a temporary image
        temp_image_path = 'temp_frame.png'
        cv2.imwrite(temp_image_path, frame)

        # Decode the barcode from the image
        barcode_data = decode_barcode(temp_image_path)
        if barcode_data:
            add_data(barcode_data[0])
            # print("1Decoded Data: ", barcode_data)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    cap.release()
    cv2.destroyAllWindows()

collected_data = bytearray()
last_code_index = 0


def add_data(qr_data):
    if 'raw' not in qr_data:
        return
    
    data_from_qr = qr_data['raw']
    code_index = int(data_from_qr[0])
    code_length = int(data_from_qr[1])
    data = data_from_qr[2:code_length]
    if code_index == last_code_index:
        return
    elif code_index == last_code_index + 1:
        last_code_index = code_index
        collected_data.extend(data)
    elif code_index > last_code_index + 1:
        print("Missing QR code(s) in sequence")

    print(code_index, code_length, data)


main()
