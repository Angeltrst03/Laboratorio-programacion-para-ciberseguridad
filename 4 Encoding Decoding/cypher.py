from cryptography.fernet import Fernet
def genwrite ():
    key= Fernet.generate_key()
    with open ("pass.key","wb") as key_file:
        key_file.write(key)


genwrite()


def call_key():
    return open ("pass.key", "rb").read()


key= call_key()
banner = "Mensaje para probar script de practica de laboratorio"
a = Fernet(key)
coded_banner =a.encrypt(b(banner))
print (coded_banner)



key = call_key()
b = Fernet(key)
decoded_banner =b.decrypt(coded_banner)
print (decoded_banner)
