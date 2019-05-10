
import datetime
import os
import shutil

def back(file):
    if os.path.exists(file):
        # os.mkdir("/home/fireworm/hehe/heihei")
        path = "/home/fireworm/hehe/heihei/hhh/dd"
        os.makedirs(path)
        shutil.copy(file,path+'file.'+date)

date = datetime.datetime.now().strftime('%Y%m%d')
back("/home/fireworm/docker/simple/Dockerfile")