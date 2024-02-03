import os
print("this will destroy your filesystem or make it unstable ")
a = input("type y to continue:")
if a=="y":
 while True:
    # Create a directory
     os.mkdir('...')
    
    # Change into the directory
     os.chdir('...')

