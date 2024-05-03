'''
2 May 2024
been a while since the last update to this. I needed a break from what I was working on though.

This is supposed to loop through the files of a specified directory and add the filenames to a tuple.
This will be the "master tuple" from which everything references and revolves around.

Well really this is for testing. In an imaginary complete version of this script the list would just be the entirety of the 
2600 library and would be permanent and only editable via manually (to add thing like homebrew games).

This version is for testing purposes while things are worked out.
-----------------------------------------------------------------------------

3 May 2024

upon re-thinking this I don't actually need this script for this purpose. All I need is a "masterlist" of rom names. 
Then loop through the usrs list of roms
so i can operate on what or may not be the same list.

This may a lot more sense when I was thinking about it the last 9 or 10 months. 

Anyway, I'm changing this to do the following:
assuming it's found, open the 'romlist.txt' file that contains all the [ntsc/non-prototype] rom names, on game per line. Load this list into a big
either list or tuple for easy reference. 



'''

import os

def createMasterTuple() -> tuple:



    return master_tuple

createMasterTuple()

#    file_extension = ".bin"
#    directory_path = "./roms"
#    master_tuple = []
#    for filename in os.listdir(directory_path):
##        print(filename)
#
#        if filename.lower().endswith(file_extension.lower()):
##            input_file_path = os.path.join(directory_path, filename)
##            output_file_path = os.path.splitext(input_file_path)[0] + file_extension
#            #print(filename)
#            master_tuple.append(filename)    
##    print(f"file type of filename is {type(filename)}")
#    master_tuple = tuple(master_tuple)
#    print(master_tuple)




