import os
file_name = input('input file name:')

if os.path.isfile(file_name):
    old_file = open(file_namem,encoding='utf8')

    t = file_name.rpartition('.')
    new_file =t[0] + '.bak.' + t[2]
    new_file = open(new_file,'w',encoding= 'utf8')

    new_file.write(old_file.read())
    new_file.close()
    old_file.close()
else:
    print('文件不存在')
