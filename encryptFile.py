import pyAesCrypt

buffer = 64 * 1024
encrypt = input("Encrypt or Decrypt: E/D")
password = input("password for Encryption: ")

if encrypt:
    pyAesCrypt.encryptFile("adminDoc.txt", "adminDoc.txt.aes", password, buffer)

else:
    pyAesCrypt.decryptFile("adminDoc.txt.aes", "adminDoc.txt", password, buffer)
