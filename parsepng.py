# https://www.youtube.com/watch?v=_DhqDYLS8oY&list=TLPQMDMwODIwMjOwjDOF6EU55g&index=15
# ---------- 8:40 min mark ----------

'''
# "byte stream"
end_hex = b"00\x00\x00\x00\x49\x45\x4E\x44\xAE\x42\x60\x82"

with open('image.png', 'rb') as f:
    conent = f.read()
    offset = conent.index(end_hex) # i think this means "12 bytes past the footer/end bytes" e.g. end_hex (6m 10s)
    f.seek(offset + len(end_hex))
#    print(f.read())
    



with open('image.png', 'ab') as e:
    f.write(e.read())
    
    

# ---------- 8:40 min mark ----------


with open('image.png', 'rb') as f:
    conent = f.read()
    offset = conent.index(end_hex)
    f.seek(offset + len(end_hex))
    
    with open('newexe.exe', 'wb') as e:
        e.write(f.read())
#    print(f.read())

'''
# ---------- 9:40 min mark ----------


# alt approach - least significant bit encoding or LSB

# alter image slighntly but least signifcant 
# "embeding exe in image"

import numpy as np
import PIL.Image

message_to_hide = "this is my secret message"

image = PIL.Image.open('image.png', 'r')
width, height = image.size
img_arr = np.array(list(image.getdata()))


# my particular png file didn't support this so that wasn't useful for displaying the binary
if image.mode == "P":
    print("Not supported")
    exit()

# i asked gpt about my above exempted "P" mode and it suggested this snippet as an alternative:
#if image.mode == "P":
#    print("Converting image to RGB mode...")
#    image = image.convert("RGB")
#    img_arr = np.array(list(image.getdata()))
# this ended up with a whole list of new errors so i am going to go back to the first thing and find a new PNG file that supports the mode i need


channels = 4 if image.mode == "RGBA" else 3

# need to know where to stop, where is the message
pixels = img_arr.size // channels

stop_indicator = "$NEURAL"
stop_indicator_length = len(stop_indicator)

message_to_hide += stop_indicator

# according to neuralnine, 08b "is just something you know" and 
byte_message = ''.join(f"{ord(c):08b}" for c in message_to_hide ) 
# print(byte_message)
# this prints the message i wrote in to the screen in binary
# 0111010001101000011010010111001100100000011010010111001100100000011011010111100100100000011100110110010101100011011100100110010101110100001000000110110101100101011100110111001101100001011001110110010100100100010011100100010101010101010100100100000101001100

# not finished yet

# ---------- 20 min 30s mark ----------


bits = len(byte_message)

if bits > pixels:
    print("Not enough space")
else:
    index = 0
    for i in range(pixels):
        for j in range(0,3):
            # "flip the last bit"
            if index < bits:
                # i think this is taking out the leading 0b and flip the last digit from 0 to 1 or 1 to 0 "remove first 2 and remove last digit"
                
                # this line came back with  error: IndexError: invalid index to scalar variable.                
                # img_arr[i][j] = int(bin(img_arr[i][j])[2:-1] + byte_message[index], 2)
                # i asked gpt and it came with this correct version - it just says [:-1] i think that's the only difference
                #img_arr[i][j] = int(bin(img_arr[i][j])[2:-1] + byte_message[index], 2)

                img_arr[i][j] = int(bin(img_arr[i][j])[:-1] + byte_message[index], 2)
                index += 1


img_arr = img_arr.reshape((height,  width, channels))                
result = PIL.Image.fromarray(img_arr.astype('uint8'), image.mode)
result.save('encoded.png')




# ------------------------------- working 16 min 30s mark to 20:30 min mark -------------------------------

# i thought i was clever by just commenting out that "not supported" snippet but i kept getting errors
# i finally tried a different png file that didn't come back as "no supported"
# so the below works but only with a supported PNG file, as that code would imply

'''
import numpy as np
import PIL.Image

message_to_hide = "this is my secret message"

image = PIL.Image.open('image.png', 'r')
width, height = image.size
img_arr = np.array(list(image.getdata()))

if image.mode == "P":
    print("Not supported")
    exit()

channels = 4 if image.mode == "RGBA" else 3

# need to know where to stop, where is the message
pixels = img_arr.size // channels

stop_indicator = "$NEURAL"
stop_indicator_length = len(stop_indicator)

message_to_hide += stop_indicator

# according to neuralnine, 08b "is just something you know" and 
byte_message = ''.join(f"{ord(c):08b}" for c in message_to_hide ) 


bits = len(byte_message)

if bits > pixels:
    print("Not enough space")
else:
    index = 0
    for i in range(pixels):
        for j in range(0,3):
            # "flip the last bit"
            if index < bits:
                img_arr[i][j] = int(bin(img_arr[i][j])[:-1] + byte_message[index], 2)
                index += 1

img_arr = img_arr.reshape((height,  width, channels))                
result = PIL.Image.fromarray(img_arr.astype('uint8'), image.mode)
result.save('encoded.png')


'''
# ------------------------------- working -------------------------------