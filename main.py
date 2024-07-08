import dir_to_bytes
import qrcodegen
import base64

input = dir_to_bytes.folder_to_bytes('C:\\Users\\TLP-001\\Desktop\\sprint3\\TheFolder')
print(input)
dir_to_bytes.bytes_to_folder(input,"testfolder")
input = base64.b64encode(input)
print(input)
qrcodegen.show_qr_sequence(input)