from config import *

from skpy import SkypeEventLoop, SkypeNewMessageEvent
from shutil import copy2
import os
import random


class SkypePing(SkypeEventLoop):
    def __init__(self):
        super(SkypePing, self).__init__(username, password)

    def onEvent(self, event):
        if isinstance(event, SkypeNewMessageEvent):
            file_name = self.getFileName()
            copy2(src, dst+file_name)

    def getFileName(self):
        file_list = os.listdir(dst)
        file_name = str(random.randint(1,1000))+".db"
        while file_name in file_list:
            file_name = str(random.randint(1,1000))+".db"
        return file_name



sk = SkypePing()
try:
    sk.loop()
except:
    sk.loop()
    

