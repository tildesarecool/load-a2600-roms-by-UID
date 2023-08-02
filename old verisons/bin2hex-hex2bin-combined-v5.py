'''
v5 - I asked GPT to add taking a list of rom files - either directory or txt file - and grab first 32 bytes 
of each binary file
and log the entries in a text with tab separation, such as

Boxing_La_Boxe_1980.bin    78d8a2ff9ae88a9500e8d0fbe6dd20c6f34c6ff1a8b1a4851bb1a6852038a88a
Adventure (USA).a26    4ceff278d84c06f3852ba586a20020d2f0a588a20120d2f0a58ba20420d2f085

I ran this aginst the roms folder and it wrote the 250 line log file
with the rom name and the 32 bytes exactly as I asked
it also created one txt file per rom file that contains ONLY the the entire hex string

I (chatgpt)  wrote a separate scrpt to take in the log file and check for duplicates
it didn't quote work the way I wanted it to
but it did point out some of the ROMs started with a long repeating string such as
FFFFFFFFFFFFFFFFFFFFFFFF
or
000000000000000000000000

so what I'll probably do is see if I can get the script to start reading the rom that many bytes in
to get my unique string





note: the sha has isn't a bad idea but since I round an online emulator:
https://javatari.org/
(It's JS. Not in java.) I can load both the before binary and the after binary in it and there by confirm it's 
the same binary file so it's not "required"



############### upon putting this source into the script and tyring it i noted there were no txt files produced. I had to re-read the GPT sample output
i tried again and this worked:
..\bin2hex-hex2bin-combined-v3.py -allbin a26 -b2h .

so the usage is:
-allbin: specifiy all binary files it finds
a26 - the file extension to run the scirpt against 
-b2h convert the binary files found to txt files with the hex values (calling the bin2hex function)
. - i just used "current directory" as the file path input

This is the current usage diagram:
usage: bin2hex-hex2bin-combined-v3.py [-h] [-b2h] [-h2b] [-allbin EXTENSION] [-t TEXT_FILE_INPUT] input_path

I think I need to adjust that
I haven't tried the "-t textfileinput" option but I assume it works


I wasn't sure what the -h did so I asked gpt and it putointed it is short for --help
I tried this -h argument and got:


PS D:\a2600\romsampler> ..\bin2hex-hex2bin-combined-v3.py -h
usage: bin2hex-hex2bin-combined-v3.py [-h] [-b2h] [-h2b] [-allbin EXTENSION] [-t TEXT_FILE_INPUT] input_path

Convert binary to hexadecimal or hexadecimal to binary for multiple files.

positional arguments:
  input_path            Input file or directory path for conversion

options:
  -h, --help            show this help message and exit
  -b2h, --bin2hex       Convert binary to hexadecimal
  -h2b, --hex2bin       Convert hexadecimal to binary
  -allbin EXTENSION, --all_binary_files EXTENSION
                        Process all binary files with the specified extension
  -t TEXT_FILE_INPUT, --text_file_input TEXT_FILE_INPUT
                        Provide a text file with filenames (one per line) as input
                        
I asked GPT to add some examples to this help screen, 
I provided the first example and asked to add at one more

The new help screen:

usage: bin2hex-hex2bin-combined-v3.py [-h] [-b2h] [-h2b] [-allbin EXTENSION] [-t TEXT_FILE_INPUT] input_path

Convert binary to hexadecimal or hexadecimal to binary for multiple files.

positional arguments:
  input_path            Input file or directory path for conversion

optional arguments:
  -h, --help            show this help message and exit
  -b2h, --bin2hex       Convert binary to hexadecimal
  -h2b, --hex2bin       Convert hexadecimal to binary
  -allbin EXTENSION, --all_binary_files EXTENSION
                        Process all binary files with the specified extension
  -t TEXT_FILE_INPUT, --text_file_input TEXT_FILE_INPUT
                        Provide a text file with filenames (one per line) as input

Examples:
  Example 1: Convert all .a26 binary files in the current directory to hexadecimal.
  bin2hex-hex2bin-combined-v3.py -allbin a26 -b2h .

  Example 2: Convert binary files listed in 'input_files.txt' (with .a26 extension) to hexadecimal.
  bin2hex-hex2bin-combined-v3.py -allbin a26 -b2h -t input_files.txt

'''



import argparse # new for v2 - I actually had to pip import this (which was successful)
import os

def bin_to_hex(input_file, output_file):

    infile = open(input_file, 'br' ) 


    line_data = ""
    
    while True: # overly easy way to just-keep-reading the binary
        bytes_read = infile.read(32) # this is bytes at a time: changed this to 32 in v3
                
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
    
    # outfile.close() # probably not necessary
    
    # print('got to end of hex-to-bin function')


def process_files_in_directory(directory_path, file_extension, output_file_extension, text_file_input=None):
    # updated in v5
    log_data = []
    for filename in os.listdir(directory_path):
        if filename.lower().endswith(file_extension.lower()):
            input_file_path = os.path.join(directory_path, filename)
            output_file_path = os.path.splitext(input_file_path)[0] + output_file_extension

            if text_file_input:
                output_file_path = os.path.splitext(text_file_input)[0] + output_file_extension

            if args.bin2hex:
                bin_to_hex(input_file_path, output_file_path)
                print(f"Binary to hexadecimal conversion successful. Output saved in {output_file_path}")

                # Prepare log data
                with open(input_file_path, "rb") as infile:
                    bytes_to_read = 32
                    hex_string = ''.join(format(byte, '02x') for byte in infile.read(bytes_to_read))
                    log_data.append(f"{filename}\t{hex_string}")

            elif args.hex2bin:
                hex_to_bin(input_file_path, output_file_path)
                print(f"Hexadecimal to binary conversion successful. Output saved in {output_file_path}")

    # Write the log file
    if log_data:
        with open("conversion_log.txt", "w") as log_file:
            log_file.write('\n'.join(log_data))
    
    
    
if __name__ == "__main__":
# see v4 for what this used to look like

    examples = [
        "Example 1: Convert all .a26 binary files in the current directory to hexadecimal.",
        "bin2hex-hex2bin-combined-v3.py -allbin a26 -b2h .",
        "",
        "Example 2: Convert binary files listed in 'input_files.txt' (with .a26 extension) to hexadecimal.",
        "bin2hex-hex2bin-combined-v3.py -allbin a26 -b2h -t input_files.txt"
    ]

# updated in v5
    parser = argparse.ArgumentParser(
        description="Convert binary to hexadecimal or hexadecimal to binary for multiple files.\n\n" + "\n".join(examples),
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument("-b2h", "--bin2hex", action="store_true", help="Convert binary to hexadecimal")
    parser.add_argument("-h2b", "--hex2bin", action="store_true", help="Convert hexadecimal to binary")
    parser.add_argument("-allbin", "--all_binary_files", metavar="EXTENSION", help="Process all binary files with the specified extension")
    parser.add_argument("-t", "--text_file_input", help="Provide a text file with filenames (one per line) as input")
    parser.add_argument("input_path", help="Input file or directory path for conversion")
    args = parser.parse_args()
    
    
    
    if args.all_binary_files:
        if os.path.isdir(args.input_path):
            process_files_in_directory(args.input_path, args.all_binary_files, ".txt", args.text_file_input)
        elif os.path.isfile(args.input_path):
            with open(args.input_path, 'r') as file:
                filenames = file.read().splitlines()
                for filename in filenames:
                    process_files_in_directory(os.path.dirname(filename), args.all_binary_files, ".txt", filename)
        else:
            print("Invalid input path. Please specify a valid file or directory path.")
    else:
        if args.bin2hex:
            bin_to_hex(args.input_path, args.input_path + ".txt")
            print(f"Binary to hexadecimal conversion successful. Output saved in {args.input_path}.txt")

        elif args.hex2bin:
            hex_to_bin(args.input_path, args.input_path.replace(".txt", "_backtobin.bin"))
            print(f"Hexadecimal to binary conversion successful. Output saved in {args.input_path.replace('.txt', '_backtobin.bin')}")
    







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