from cryptography.fernet import Fernet
#Creating the key for the text file
key = Fernet.generate_key()
with open('mykey.key', 'wb') as mykey :
 mykey.write(key)
#Loading a key for the file
with open('mykey.key', 'rb') as mykey :
 key = mykey.read()
print(key)
#Encryption
f = Fernet(key)
with open('sample', 'rb') as original_file :
 original = original_file.read()
encrypted = f.encrypt(original)
with open('enc_sample', 'wb') as encrypted_file :
 encrypted_file.write(encrypted)
#Decryption
f = Fernet(key)
with open('enc_sample', 'rb') as encrypted_file :
 encrypted = encrypted_file.read()
decrypted = f.decrypt(encrypted)
with open('dec_sample', 'wb') as decrypted_file :
 decrypted_file.write(decrypted)
