#! python3
# -*- coding: utf-8 -*-
# http://python.su/forum/topic/15531/?page=1#post-93316
import sys
sys.path.append("../..")
sys.path.append("..\..")
sys.path.append(".")
sys.path.append("..")
sys.path.append("./term")
sys.path.append(r".\term")
from commands8 import *
import pyperclip

path_of_updates = Path.extend(Path.home(), "Desktop")

path_where_to_store = Path.extend(Path.working(), "pics_realty")

old_list = Dir.list_of_files(path_of_updates)

while True:
    time.sleep(0.1)
    new_list = Dir.list_of_files(path_of_updates)
    if old_list != new_list:
        for file in new_list:
            if file not in old_list:
                print("new file", file)
                if file[:1] != ".":
                    File.move(Path.extend(path_of_updates, file), Path.extend(path_where_to_store, file))
                    pyperclip.copy("pics_realty" + "/" + file)
                    #print(file, "moved")
                else:
                    pass#print("skip file, wait for full writing...")
        old_list = new_list
