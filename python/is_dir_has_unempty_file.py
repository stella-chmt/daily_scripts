import sys, urllib, os, shutil, re

def is_dir_has_unempty_file(dir):
    unempty_file_exists = False
    for filename in os.listdir(dir):
        if os.stat(os.path.join(dir, filename)).st_size != 0:
            unempty_file_exists = True
            break
    return unempty_file_exists

print is_dir_has_unempty_file("../search-shop-bizer/arts")
