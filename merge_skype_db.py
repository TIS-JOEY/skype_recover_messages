import config
import os
from subprocess import call
import os



command = 'pythonw '+ skyperious_main_path + ' merge "'+src+'" '
for file_name in os.listdir(dst):
	if file_name=='main.db':
		os.rename(dst+'main.db',dst+'main_old.db')
		file_name = 'main_old.db'
	if not file_name.startswith('.'):
		command+=('"'+dst+file_name+'" ')

command+='-o "'+dst+"main.db"+'"'


os.system("source activate "+ env_name +" && +command")


for file_name in os.listdir(dst):
	if file_name!='main.db':
		os.remove(dst+file_name)

