import subprocess
import itchat

sub = subprocess.Popen("dir",shell=True,stdout=subprocess.PIPE)
sub.wait()
print(type(sub.stdout.read()))
print(sub.stdout.read())

msg="cmd pwd"
txt = msg.lstrip(msg[0:4])
print(txt)