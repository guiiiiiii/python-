import os

os.chdir(r'C:\Users\student\Desktop\Python\resume')

print(os.getcwd())
print(os.listdir())

for filename in os.listdir():
    os.rename(filename,filename.replace('samsume','MULTI'))