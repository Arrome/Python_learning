import os
#
# for dirpath,dirnames,filenames in os.walk("/home/fireworm/docker"):
#     for filename in dirnames:
#         print(filename)
for path in os.path.split("/home/fireworm/docker"):
    print(path)