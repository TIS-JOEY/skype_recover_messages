dst = '/Users/apple/Desktop/Backup/'

import os
from subprocess import call
import os


command = 'pythonw /anaconda3/envs/py2/lib/python2.7/site-packages/skyperious/main.py merge "/Users/apple/Library/Application Support/Skype/live#3ad22769750/main.db" '

for file_name in os.listdir(dst):
	if file_name=='main.db':
		os.rename(dst+'main.db',dst+'main_old.db')
		file_name = 'main_old.db'
	if not file_name.startswith('.'):
		command+=('"'+dst+file_name+'" ')

command+='-o "'+dst+"main.db"+'"'


os.system("source activate py2 && "+command)


for file_name in os.listdir(dst):
	if file_name!='main.db':
		os.remove(dst+file_name)

