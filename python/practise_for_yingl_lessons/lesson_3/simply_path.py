# coding=utf-8
'''
简化路径。给定一个文档(Unix-style)的完全路径，请进行路径简化。
"/home/", => "/home“
"/a/./b/../../c/", => "/c“
'''
def simplyPath(path):
    if not path:
        return ""
    else:
        rtn = []
        dirs = path.split("/")
        for dir in dirs:
            if (dir == "..") and rtn:
                rtn.pop()
            elif (dir != "..") and (dir != ".") and dir:
                rtn.append(dir)
    return "/" + ("/".join(rtn))
'''
# for循环里原始的自己的code,可以进一步简化为上面的版本
            if dir == ".":
                continue
            else:
                if (dir != "..") and (dir != ".") and dir:
                    rtn.append(dir)
                elif rtn and dir == "..":
                        rtn.pop()
'''



dir1 = "/home/"
dir2 = "/a/./b/../../c/"
dir3 = "/./a/b/c"
print(simplyPath(dir1))
print(simplyPath(dir2))
print(simplyPath(dir3))
