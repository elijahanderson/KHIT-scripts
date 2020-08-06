from tkinter import filedialog as fd
from cryptography.fernet import Fernet

filename = fd.askopenfilename(title="Select the report you want to decrypt")
keyfile = fd.askopenfilename(title="Select the appropriate keyfile you previously downloaded")
key = open(keyfile, "rb").read()
f = Fernet(key)

with open(filename, "rb") as file:
    decrypted_data = f.decrypt(file.read())

with open("decrypted_report.xlsx", "wb") as file:
    file.write(decrypted_data)

