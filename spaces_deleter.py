from os import rename
import os

dir = '/home/xenakrll/Documents/articles/new'
for filename in os.listdir(dir):
    new_filename = filename.replace(' ', '_')
    rename((os.path.join(dir)+'/'+filename), (os.path.join(dir)+'/'+new_filename))