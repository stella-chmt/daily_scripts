# coding = utf-8
'''
目录树遍历（os.listdir获得文件列表，os.path.isdir判断是否目录）
'''
import os
import sys

def listDir(curdir, level):
    os.chdir(curdir)
    new_dirs = []
    dirs = os.listdir(curdir)
    for dir in dirs:
        fullpath = os.path.join(curdir, dir)
        if os.path.isdir(fullpath):
            new_dirs.append(dir)
        else:
            print("\t" * level + "-" + dir )

    for dir in new_dirs:
        print("\t" * level + "-#" + dir)
        fullpath = os.path.join(curdir, dir)
        listDir(fullpath, level +1)

#root=sys.argv[1]
root = "/Users/mengting.chen/Work/workspace/daily_scripts/python"
if root[0] != "/":
    root = os.path.join(os.getcwd(), root)
listDir(root, 0)
