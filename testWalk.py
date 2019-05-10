import os
dirss="/home/fireworm/test/src"
for root,dirs,files in os.walk(dirss,topdown=False):
    for name in files:
        print("--"+os.path.join(root,name))
    for dirs in dirs:
        print("++"+os.path.join(root,dirs))