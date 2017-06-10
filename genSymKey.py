import os

file = open("Key", "w")
file.write(os.urandom(8).hex())
file.close()