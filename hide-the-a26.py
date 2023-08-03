# https://www.youtube.com/watch?v=r-7d3w5xerY
# png info starts at 7:12

# this video is by the same channel (neuralnine) but the title mentions png specifically:
# https://www.youtube.com/watch?v=_DhqDYLS8oY

# this is just side track/diversion to see if I can embed a 2600 rom into a PNG file
# or this case i'll embed adventure.a26 into the box art of adventre - adventure.png
# this PNG can then be posted and saved (the PNG file opens the same as before)
# yes, it's called Steganography 

# I'm just following along with this video as best I can. I can mostly understand it

# now i'm on to this one
# https://www.youtube.com/watch?v=_DhqDYLS8oY
















'''
with open('Adventure (USA).png', 'ab') as f:
    pass #f.write(b"hello world") # append the text to the end of the png file

with open('Adventure (USA).png', 'rb') as o:
    content = o.read()
    offset = content.index(bytes.fromhex('FFD9'))
    
    o.seek(offset + 2)
    print(f.read())
'''
##########################################################
# following this video specifically
# https://www.youtube.com/watch?v=r-7d3w5xerY

# starting around 7:50
# pip install pillow
#import PIL.Image
#import io

#  10:35
# this opens the jpg and extracts the binary data from the jpg
# then save that value to a new file with a PNG file extension
# the reverse of the above appending the PNG into the JPG, in other words.
'''
with open('test.jpg', 'rb') as f:
    content = f.read()
    offset = content.index(bytes.fromhex('FFD9')) # I believe FFD9 is the ending/footer of jpg files - e.g. offset is equal to the ending of the JPG data
    
    # seek to 2 bytes after that offset. e.g. Find FFD9 and jump forward 2 bytes. 
    # I guess this is just a command to move the "cursor" to that position inside the jpg and it stays there(?)
    f.seek(offset + 2) 
    
    
    # if my above assumption is correct, this starts reading at that FFD9 position and stores it in the 
    # new_image variable
    new_img = PIL.Image.open(io.BytesIO(f.read())) 
    
    # then save that data to a file ending in PNG
    new_img.save("new_image.png")
    
'''


# his example puts a PNG file "into" a JPG file
'''
img = PIL.Image.open('someimage.jpg')
byte_arr = io.BytesIO()
img.save(byte_arr, format='PNG')

with open('someimage.jpg', 'ab') as f:
    f.write(byte_arr.getvalue())
'''
# this is it. Thisi s appending png into a jpg
# probably need second function get the original back out
