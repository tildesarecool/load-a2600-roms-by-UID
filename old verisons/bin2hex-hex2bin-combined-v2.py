'''
v2 - command line arguments

note: the sha has isn't a bad idea but since I round an online emulator:
https://javatari.org/
(It's JS. Not in java.) I can load both the before binary and the after binary in it and there by confirm it's 
the same binary file so it's not "required"

In this version I'm adding a way to take in the file name(s) from the command line

In fact it has the description
Convert binary to hexadecimal or hexadecimal to binary.

On a related note, i asked  GPT:
    If I only wanted to read the first 32 bytes of a the binary file input, could i just use 
    read(32) instead? 

and it came back with this answer:
    Yes, exactly! If you only want to read the first 32 bytes of the binary file input, you can use read(32) 
    instead of read(16). The number inside the read() method indicates the number of bytes you want to read 
    from the file.


Since I was just going to read in the first 32 bytes at some point anyway I think what I'll do is change that 16 to a 32 and 
and just encode the data 32bytes at a time. Because that would just be one read in when i switch to first 32 bytes only
it would just the one statement and done. Right?


'''



import argparse # new for v2 - I actually had to pip import this (which was successful)
import os

def bin_to_hex(input_file, output_file):

    infile = open(input_file, 'br' ) 


    line_data = ""
    
    while True: # overly easy way to just-keep-reading the binary
        bytes_read = infile.read(16) # i'm actually not sure what the 16 is for. 16 bytes at time?
                
        if not bytes_read: # dumb way saying "until end of file"
            break # breaks out of the while true infinite loop
        for byte in bytes_read: # loop through the data captured in the byte_read variable
            byte_hex = format(byte, '02x') # apparently format it as "02 hex" which means hex expresssed only as 2 characters, e.g. FF is the highest
            line_data += byte_hex # use this variable to consilate this new hex value one value at a time

    print('got to end of bin-to-hex function')
    #print('value of line data is \n', line_data  )
    with open(output_file, 'w') as hex_string:
        hex_string.write(line_data)

def hex_to_bin(input_file, output_file):
    with open(input_file, 'r') as infile:
        hex_data = infile.read()

    binary_data = bytes.fromhex(hex_data)

    with open(output_file, 'wb') as outfile:
        outfile.write(binary_data)
    
    #outfile.close() # probably not necessary
    
    print('got to end of hex-to-bin function')

def confirm_file_exist(input_file):
    # imput OS required
    # not sure if this really has to be a separate function or not. 
    # as I could just do this exact line in the actual main function and do the same thing
    checked_file = os.path.exists(input_file) # this should be a bool type
    return checked_file
    


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Convert binary to hexadecimal or hexadecimal to binary.")
    parser.add_argument("-b2h", "--bin2hex", action="store_true", help="Convert binary to hexadecimal")
    parser.add_argument("-h2b", "--hex2bin", action="store_true", help="Convert hexadecimal to binary")
    
    
    parser.add_argument("input_file", help="Input binary file for conversion")
    
    
    parser.add_argument("output_file", nargs="?", help="Output file for conversion (optional)")
    
    args = parser.parse_args()
    
    
    if args.bin2hex:
        output_file = args.output_file if args.output_file else args.input_file + ".txt"
        bin_to_hex(args.input_file, output_file)
        print(f"Binary to hexadecimal conversion successful. Output saved in {output_file}")

    elif args.hex2bin:
        output_file = args.output_file if args.output_file else args.input_file.replace(".txt", "_backtobin.bin")
        hex_to_bin(args.input_file, output_file)
        print(f"Hexadecimal to binary conversion successful. Output saved in {output_file}")

    else:
        print("Please specify either -b2h/--bin2hex or -h2b/--hex2bin option.")
    
    
    
'''
# wasn't sure i'd need this. turns out above lines fill it in anyway
    if (args):
        print("Now taking arguments")

'''
        
    

#    input_binary = 'Boxing_La_Boxe_1980.bin'
#    output_hex = 'Boxing_La_Boxe_1980_in_hex.txt'
#    output_binary = 'output_binary_backtobin.bin'

    # Perform bin2hex functionality, saving the hex string output to a text file
#    bin_to_hex(input_binary, output_binary)
    
    # bin_to_hex(input_binary, output_hex) # got this work finally
    # Perform hex2bin functionality, converting the text file back to a binary file

#    hex_to_bin(output_hex, output_binary)

#    print("successfully called functions(s).")






############################# write the created txt file data back to a binary file - this one works #############################
# ( hex string back to binary )

# I asked GPT to write the inverse of the below script:
# bring this txt file containing the hex string
# and convert it back into the original binary file
# I'm not sure about its output though, so I'm going to write a script loosely based on that it suggested

# this snippit simply 
# - opens the txt file for reading
# - assigns a variable to the contents of that txt file
# - uses the fromhex method to convert the hext back to a binary format
# - writes that newly formed binary data back to a bin file
# - latest version: write output to a txt file
# And that's it...
'''
with open('Boxing_La_Boxe_1980_in_hex.txt', 'r') as infile:
    hex_data = infile.read()

binary_data = bytes.fromhex(hex_data)

with open('Boxing_La_Boxe_1980_in_hex_output_binary.bin', 'wb') as outfile:
    outfile.write(binary_data)
'''

############################# write the created txt file data back to a binary file - this one works #############################


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




############################# This is the working version - keep (30 july 2023) #############################

'''
def bin_to_hex(input_file, output_file):

    infile = open(input_file, 'br' ) 


    line_data = ""
    
    while True: # overly easy way to just-keep-reading the binary
        bytes_read = infile.read(16) # i'm actually not sure what the 16 is for. 16 bytes at time?
                
        if not bytes_read: # dumb way saying "until end of file"
            break # breaks out of the while true infinite loop
        for byte in bytes_read: # loop through the data captured in the byte_read variable
            byte_hex = format(byte, '02x') # apparently format it as "02 hex" which means hex expresssed only as 2 characters, e.g. FF is the highest
            line_data += byte_hex # use this variable to consilate this new hex value one value at a time

    print('got to end of bin-to-hex function')
    #print('value of line data is \n', line_data  )
    with open(output_file, 'w') as hex_string:
        hex_string.write(line_data)
'''

############################# This is the working version - keep (30 july 2023) #############################



############################# This is the working version - keep (30 july 2023) #############################
'''
def hex_to_bin(input_file, output_file):
    with open(input_file, 'r') as infile:
        hex_data = infile.read()

    binary_data = bytes.fromhex(hex_data)

    with open(output_file, 'wb') as outfile:
        outfile.write(binary_data)
    
    #outfile.close() # probably not necessary
    
    print('got to end of hex-to-bin function')
'''
############################# This is the working version - keep (30 july 2023) #############################