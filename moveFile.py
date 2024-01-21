import os
import shutil

from_dir = 'Downloads'
to_dir = 'Document_Files'

list_of_files = os.listdir(from_dir)
for i in list_of_files:
    name,extension = os.path.splitext(i)
    if(extension==''):
        continue
    if(extension in ['.doc','.pdf','.txt','.docx']):
        path1 = from_dir+'/'+i
        path2 = to_dir+'/'+'Docs'
        path3 = to_dir+'/'+'Docs'+'/'+i
        if(os.path.exists(path2)):
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            shutil.move(path1,path2)
