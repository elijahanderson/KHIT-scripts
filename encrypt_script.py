from cryptography.fernet import Fernet


def encrypt_script():
    key = Fernet.generate_key()
    with open("D:/key_bruns.key", "wb") as key_file:
        key_file.write(key)

    filename = "C:/Users/mingus/Documents/report_bruns.xlsx"

    f = Fernet(key)
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
        # encrypt data
        encrypted_data = f.encrypt(file_data)
        # write the encrypted file
        with open("C:/Users/mingus/Documents/(encrypted)report_bruns.xlsx", "wb") as file:
            file.write(encrypted_data)


encrypt_script()
