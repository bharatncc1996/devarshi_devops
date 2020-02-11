import os

name=raw_input('enter your name ')
filename=raw_input('enter your new file name')

os.system('touch {}'.format(filename))
print('hello {} good eveng how r u your file {} was created successfully '.format(name,filename))


