# https://www.youtube.com/watch?v=_DhqDYLS8oY&list=TLPQMDMwODIwMjOwjDOF6EU55g&index=15
# alt approach - least significant bit encoding or LSB
# alter image slighntly but least signifcant 
# "embeding secret message in a PNG file"
# this is the decoding one
# as of the 26:18 min mark
# obviously this paired with the encoding script
# parsepng.py

import numpy as np
import PIL.Image

image = PIL.Image.open('encoded.png', 'r')
#width, height = image.size
img_arr = np.array(list(image.getdata()))

# for decoding this can be assumed as true because it would have to be 
# in order for the encoding part to work
# so there is no reason to have this here
if image.mode == "P":
    print("Not supported")
    exit()

channels = 4 if image.mode == "RGBA" else 3



# need to know where to stop, where is the message
pixels = img_arr.size // channels

secret_bits = [bin(img_arr[i][j])[-1] for i in range(pixels) for j in range(0,3) ] 
secret_bits = ''.join(secret_bits)
secret_bits = [secret_bits[i:i+8] for i in range(0, len(secret_bits), 8)]

print(secret_bits)

secret_message = [chr(int(secret_bits[i], 2)) for i in range(len(secret_bits)) ]

secret_message = ''.join(secret_message)

stop_indicator = "$NEURAL"

if stop_indicator in secret_message:
    print(secret_message[:secret_message.index(stop_indicator)])
else:
    print("Couldn't find secret message")
    