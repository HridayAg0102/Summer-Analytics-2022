import os

# to get the current working directory.
current_dir = os.getcwd()
print(current_dir) 

# to change directory.
os.chdir('/home/siddhivinayak/Desktop')
print(os.getcwd())


# Creating a new file at the current working 
# directory in write mode ('w')
# NOTE: The cwd was changed by prevous command 
# i.e. to Desktop

with open('test.txt','w') as f:
	f.write('This is a test file.')

# to get the list of all files and folders.
print(os.listdir())

# to get the subdirectories and files
# of a particular subdirectory of CWD.
print(os.listdir('Github'))

# create a directory
os.mkdir('test folder')

# to create a directory in a subdirectory of CWD
os.mkdir('Github/test folder in path')

# to Rename any directory of file
os.rename('transfer_tester','transfer')

# to remove a file
os.remove('test.txt')
print(os.listdir())

# to remove a directory
os.rmdir('test folder')
