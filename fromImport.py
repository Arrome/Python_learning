import os
import zipfile
print('aa/target/aaa.war'.rsplit('/'))
print('aa/target/aaa.war'.split('/'))
print('aa/target/aaa.war'.rsplit('/',1))
print('aa/target/aaa.war'.rsplit('/',1)[-1])
print('target/sss/aaa.war'.rsplit('/',1))
print('target/aaa.war'\
.rsplit('/',0))
print('target/aaa.war'.rsplit('/',1)[-1].rsplit('.',1)[0])

print(os.path.split("cps/dist/change.xml")[0])
print(os.path.split("target/change.xml")[0])