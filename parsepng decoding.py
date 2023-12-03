# https://www.youtube.com/watch?v=_DhqDYLS8oY&list=TLPQMDMwODIwMjOwjDOF6EU55g&index=15
# alt approach - least significant bit encoding or LSB
# alter image slighntly but least signifcant 
# "embeding exe in image"

import numpy as np
import PIL.Image

image = PIL.Image.open('encoded.png', 'r')
#width, height = image.size
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
# print(byte_message)
# this prints the message i wrote in to the screen in binary
# 0111010001101000011010010111001100100000011010010111001100100000011011010111100100100000011100110110010101100011011100100110010101110100001000000110110101100101011100110111001101100001011001110110010100100100010011100100010101010101010100100100000101001100

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
