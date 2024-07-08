import cv2
from pyzbar import pyzbar
from qr_data_to_bytearray import *


def decode_qr_codes(frame):
    # Decode the QR codes in the frame
    qr_codes = pyzbar.decode(frame)
    bytes_data = b''
    for qr_code in qr_codes:
        # Extract the bounding box location of the QR code and draw a rectangle around it
        (x, y, w, h) = qr_code.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # The data is a bytes object so if we want to draw it on our output image
        # we need to convert it to a string first
        bytes_data = qr_code.data
        qr_code_data = qr_code.data.decode("utf-8")
        qr_code_type = qr_code.type

        # Draw the QR code data and type on the frame
        text = f"{qr_code_data} ({qr_code_type})"
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return frame, bytes_data


def main():
    Message = ""
    # Open a connection to the webcam (0 is usually the default camera)
    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        # Decode QR codes in the frame
        frame, data = decode_qr_codes(frame)
        if add_data(data):
            break

        # Display the resulting frame
        cv2.imshow('QR Code Scanner', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print(Message)
            break

    # Release the capture and close the window
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
    process_data()
