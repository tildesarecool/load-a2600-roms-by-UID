'''
#############################
note: 
31 July 2023
since the two functions below can be successfully called and function as I wanted
I made a copy of this file with 'v2' in the file name
I would say don't bother with this one, just edit the new version
#############################

I wanted to combine the two scripts
and add the extra feature of taking a before and after sha2 has value
to confirm when i convert it back to a binary it is in fact the binary as before

I did ask GPT for a version of this but i'm going to write my own version of it loosely based on the GPT's version
rather than copy/paste

#import hashlib # note: apparently this isn't found by default (didn't install with pip) - 
# must fix before trying to use the hash functionality
# I don't think it's vital or  necessary, though

note: the sha has isn't a bad idea but since I round an online emulator:
https://javatari.org/
(It's JS. Not in java.) I can load both the before binary and the after binary in it and there by confirm it's 
the same binary file so it's not "required"


'''
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

############################# This is the working version - keep (30 july 2023) #############################
def hex_to_bin(input_file, output_file):
    with open(input_file, 'r') as infile:
        hex_data = infile.read()

    binary_data = bytes.fromhex(hex_data)

    with open(output_file, 'wb') as outfile:
        outfile.write(binary_data)
    
    #outfile.close() # probably not necessary
    
    print('got to end of hex-to-bin function')

############################# This is the working version - keep (30 july 2023) #############################

        #input_file.close() # have to remember to close the file when done

    #print(line_data)

    # I ask GPT to change the print line above to instead write the hex string to a txt file

    # Write the hex string to a text file named "Boxing_La_Boxe_1980_in_hex.txt"
    #with open('Boxing_La_Boxe_1980_in_hex.txt', 'w') as outfile:



'''
    hexfile = open(output_file, 'w')
    
    #with open(output_file, 'w') as outfile:
        #outfile.write(line_data)
    hexfile.write(line_data)
    

    hexfile.close()
'''        




if __name__ == "__main__":
    input_binary = 'Boxing_La_Boxe_1980.bin'
    output_hex = 'Boxing_La_Boxe_1980_in_hex.txt'
    output_binary = 'output_binary_backtobin.bin'

    # Perform bin2hex functionality, saving the hex string output to a text file
#    bin_to_hex(input_binary, output_binary)
    
    # bin_to_hex(input_binary, output_hex) # got this work finally
    # Perform hex2bin functionality, converting the text file back to a binary file

    hex_to_bin(output_hex, output_binary)

    print("successfully called functions(s).")






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