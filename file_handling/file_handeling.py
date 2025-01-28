import os

# os.mkdir("v")
os.chdir("v")
print(os.getcwd())
os.chdir("..")
print(os.getcwd())

os.rmdir("v")