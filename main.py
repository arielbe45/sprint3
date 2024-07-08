import sys

sys.path.append('.venv/Lib/site-packages/')

import dir_to_bytes
import qrcodegen
import base64


input = dir_to_bytes.folder_to_bytes(r"C:\Users\Public\Documents\top_secret")
print(input)
# dir_to_bytes.bytes_to_folder(input,"testfolder")
input = base64.b64encode(input)
print(input)
qrcodegen.show_qr_sequence(input)