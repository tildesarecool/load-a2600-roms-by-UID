#!/usr/bin/env python3

# this is actually a video on embedding different binary blobs into JPGs or PNG files
# https://www.youtube.com/watch?v=r-7d3w5xerY
# I thought I would use his example code to just directly open a 2600 rom file and output it as a txt file
# in a hex format. A "hex dump" in other words.

# the name of the rom this case is 
# Boxing_La_Boxe_1980.bin
# it should be in the same directory as the python script
# if i'm not using the "with" then no need for 'as f:'

# this "should" open the bin file in "binary/read mode"


############################# write the entirety of the bin file to a txt file #############################
'''
I'll just include the explanation of that bytes_to_read -= 1 line from gpt:

    In this script, the variable bytes_to_read is set to 32 initially, indicating the number of bytes you want to read from the file. The min(16, bytes_to_read) ensures that we 
    read either a maximum of 16 bytes at a time or the remaining bytes (if less than 16) to fulfill the requirement of reading only the first 32 bytes. The loop stops when 
    bytes_to_read becomes zero or when the end of the file is reached.
    This way, you'll read the first 32 bytes, convert them to hexadecimal format, and store the result in the line_data variable. The script then prints the contents of line_data.
(this script works)
'''

# this snippit simply 
# - opens the binary file for reading
# - loops through the whole file until the end
# - converts it to a byte/0x2 format in a variable
# - closes the binary file when the end of file is reached
# - latest version: write output to a txt file
# And that's it...
# Could I embed the entire hex output into the PNG file of the box art? Most likely, yes


infile = open('Boxing_La_Boxe_1980.bin', 'br' ) 

line_data = ""
while True: # overly easy way to just-keep-reading the binary
    bytes_read = infile.read(16) # i'm actually not sure what the 16 is for. 16 bytes at time?
    if not bytes_read: # dumb way saying "until end of file"
        break # breaks out of the while true infinite loop
    for byte in bytes_read: # loop through the data captured in the byte_read variable
        byte_hex = format(byte, '02x') # apparently format it as "02 hex" which means hex expresssed only as 2 characters, e.g. FF is the highest
        line_data += byte_hex # use this variable to consilate this new hex value one value at a time
infile.close() # have to remember to close the file when done

#print(line_data)

# I ask GPT to change the print line above to instead write the hex string to a txt file

# Write the hex string to a text file named "Boxing_La_Boxe_1980_in_hex.txt"
with open('Boxing_La_Boxe_1980_in_hex.txt', 'w') as outfile:
    outfile.write(line_data)

############################# write the entirety of the bin file to a txt file #############################

'''

# this is actually v2 that chatgpt produced. it doens't work.

import sys

if len(sys.argv) != 3:
    print("Usage: bin2hex.py <input_binary> <output_text>")
    sys.exit(1)

with open(sys.argv[1], 'rb') as infile:
    with open(sys.argv[2], 'w') as outfile:
        for address, chunk in enumerate(iter(lambda: infile.read(16), b'')):
            line_data = ''.join(format(byte, '02x') for byte in chunk)
            outfile.write(f"0x{address * 16:08x}\t{line_data}\n")
# This is v1 of what gpt gave me. it doesn't work.
if len(sys.argv) != 3:
    print("disassembly.py {input binary file} {output text}")
    sys.exit(1)

infile = open(sys.argv[1], 'rb')
outfile = open(sys.argv[2], 'w')

address = 0

while True:
    bytes_read = infile.read(16)
    if not bytes_read:
        break

    line_data = ""
    for byte in bytes_read:
        byte_hex = format(byte, '02x')
        line_data += byte_hex

    outfile.write(f"0x{address:08x}\t{line_data}\n")
    address += 16

infile.close()
outfile.close()
'''





############################# This very basic version at least works #############################
'''
# this snippit simply 
# - opens the binary file for reading
# - loops through the whole file until the end
# - converts it to a byte/0x2 format in a variable
# - closes the binary file when the end of file is reached
# And that's it...
# Could I embed the entire hex output into the PNG file of the box art? Most likely, yes


infile = open('Boxing_La_Boxe_1980.bin', 'br' ) 

line_data = ""
while True: # overly easy way to just-keep-reading the binary
    bytes_read = infile.read(16) # i'm actually not sure what the 16 is for. 16 bytes at time?
    if not bytes_read: # dumb way saying "until end of file"
        break # breaks out of the while true infinite loop
    for byte in bytes_read: # loop through the data captured in the byte_read variable
        byte_hex = format(byte, '02x') # apparently format it as "02 hex" which means hex expresssed only as 2 characters, e.g. FF is the highest
        line_data += byte_hex # use this variable to consilate this new hex value one value at a time
infile.close() # have to remember to close the file when done

print(line_data)

'''
############################# This very basic version at least works #############################


############################# just read those first 32 bytes and output to screen #############################


'''
I'll just include the explanation of that bytes_to_read -= 1 line from gpt:

    In this script, the variable bytes_to_read is set to 32 initially, indicating the number of bytes you want to read from the file. The min(16, bytes_to_read) ensures that we 
    read either a maximum of 16 bytes at a time or the remaining bytes (if less than 16) to fulfill the requirement of reading only the first 32 bytes. The loop stops when 
    bytes_to_read becomes zero or when the end of the file is reached.
    This way, you'll read the first 32 bytes, convert them to hexadecimal format, and store the result in the line_data variable. The script then prints the contents of line_data.
(this script works)
'''

'''
infile = open('Boxing_La_Boxe_1980.bin', 'br' ) 

    #f.read(b)
bytes_to_read = 32 # I said first 32 bytes
line_data = "" # this was just hold the string

while bytes_to_read > 0: # overly easy way to just-keep-reading the binary
    bytes_read = infile.read(min(16, bytes_to_read)) # modified slightly. be between 16 and value of bytes_to_read. which is 32
    if not bytes_read: # dumb way saying "until end of file"
        break # breaks out of the while true infinite loop
    for byte in bytes_read: # loop through the data captured in the byte_read variable
        byte_hex = format(byte, '02x') # apparently format it as "02 hex" which means hex expresssed only as 2 characters, e.g. FF is the highest
        line_data += byte_hex # use this variable to consilate this new hex value one value at a time
        bytes_to_read -= 1 

infile.close() # have to remember to close the file when done

print(line_data) # in the case of Boxing_La_Boxe_1980.bin, output: 78d8a2ff9ae88a9500e8d0fbe6dd20c6f34c6ff1a8b1a4851bb1a6852038a88a (which is the part of the whole thing)


# alternative output: Write (32bytes) the hex string to a text file named "output.txt"
with open('Boxing_La_Boxe_1980_in_hex.txt', 'w') as outfile:
    outfile.write(line_data)


'''

############################# just read those first 32 bytes and output to screen #############################





############################# write the entirety of the bin file to a txt file #############################
'''
I'll just include the explanation of that bytes_to_read -= 1 line from gpt:

    In this script, the variable bytes_to_read is set to 32 initially, indicating the number of bytes you want to read from the file. The min(16, bytes_to_read) ensures that we 
    read either a maximum of 16 bytes at a time or the remaining bytes (if less than 16) to fulfill the requirement of reading only the first 32 bytes. The loop stops when 
    bytes_to_read becomes zero or when the end of the file is reached.
    This way, you'll read the first 32 bytes, convert them to hexadecimal format, and store the result in the line_data variable. The script then prints the contents of line_data.
(this script works)
'''

# this snippit simply 
# - opens the binary file for reading
# - loops through the whole file until the end
# - converts it to a byte/0x2 format in a variable
# - closes the binary file when the end of file is reached
# - latest version: write output to a txt file
# And that's it...
# Could I embed the entire hex output into the PNG file of the box art? Most likely, yes

'''
infile = open('Boxing_La_Boxe_1980.bin', 'br' ) 

line_data = ""
while True: # overly easy way to just-keep-reading the binary
    bytes_read = infile.read(16) # i'm actually not sure what the 16 is for. 16 bytes at time?
    if not bytes_read: # dumb way saying "until end of file"
        break # breaks out of the while true infinite loop
    for byte in bytes_read: # loop through the data captured in the byte_read variable
        byte_hex = format(byte, '02x') # apparently format it as "02 hex" which means hex expresssed only as 2 characters, e.g. FF is the highest
        line_data += byte_hex # use this variable to consilate this new hex value one value at a time
infile.close() # have to remember to close the file when done

#print(line_data)

# I ask GPT to change the print line above to instead write the hex string to a txt file

# Write the hex string to a text file named "Boxing_La_Boxe_1980_in_hex.txt"
with open('Boxing_La_Boxe_1980_in_hex.txt', 'w') as outfile:
    outfile.write(line_data)
'''

############################# write the entirety of the bin file to a txt file #############################