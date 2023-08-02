'''
# https://tildesare.cool/category/projects/pc-with-2600

v8 - i couldn't get whatever gpt gave me to work as v7
I tried over and over again
so i've derived this version from v6
just skip over 7

Since GPT seemed to be stuck in a loop of giving me invalid code, I decided to start a new chat
I pasted in the v6 version of the script
and told it i wanted to add that -s with the number of bytes
and I tried to be specific about starting that many bytes in, reading the 32 bytes
then saving the string and binary file name to the log file the same as the existing script

good news is it seems to be doing the skipping successfully
bad news is when it writes the whole rom file to text files as well one for each binary 
that also is just teh 32 bytes
i already have that whole binary worth of hex string saved multiple times over anyway
so it's not really that big of a deal
I don't think i even need that, actually

just random thought: make 640 bytes the starting/jump in point. esay to remember, a reference to the 640k ram of old PCs. Easer egg. etc.
hmmm.



v6 - to deal with roms that have long strings at the start of the file of same character
such as FFFFFFFFFFFFFF or 0000000000000000
i asked GPT if it were possible to jump some bytes into the binary file before reading the 32 bytes worth
hopefully THAT will produce the UID i'm looking for
GPT provided a new argument: 
-s 256
as example, to start reading at the 257th byte

after looking at the log files that contains the whole hex string of each file and then looking at the log file
that contains the first 32 bytes I came up with:
# notes:
# 515 characters comes out to 257 bytes
# and 32 bytes comes out to 65 characters...

i noticed the conversion_log.txt had the same values next to the a26 file names no matter what value i put in with -s
so i explained this to gpt as best i could
and it agreed and gave me a new version

so I think I want to jump at least 300 bytes(?) in before getting my 32 bytes

v6:
# i tried this by starting the byte reading after 300 bytes
# but it turns out games like tunnel runner have the repeating f's for 512 times
# so I'll try...524?
as it turns out the bin_to_hex function had changed and either i missed it or GPT forgot to display the changes
since the function was different when I tried below

here is how i worded the correction for gpt-
##################
i think their might be a logical bug in my code in how the log files work -
i want to make sure this code:
- opens the binary file for reading
- skips the specified number of bytes as defined by the -s
- reads 32 bytes in starting from the point specified from the -s
- then writes to the conversion_log.txt and the files with the same filename as the binary files except with the txt extension

i think the skipping bytes and log file writing might be happening in the wrong order
###################
i'll save putting in the new function versions for v7


chatgpt wrote me a separate script 
to calculate how many bytes into the rom/binary file
I start to start at to hopefully avoid these random roms with apparently header files

####################### utility script for counting bytes from the binary file ####################### 
hex_string = "ffffffffffffffffffffffffffffffffff"
byte_data = bytes.fromhex(hex_string)
print(len(byte_data))  # This will give you the number of bytes used in the binary file.
####################### utility script for counting bytes from the binary file ####################### 


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



import argparse
import os

def bin_to_hex(input_file, output_file, bytes_to_skip=0, bytes_to_read=32):
    with open(input_file, 'rb') as infile:
        infile.seek(bytes_to_skip)
        with open(output_file, 'w') as outfile:
            bytes_read = infile.read(bytes_to_read)
            hex_string = ''.join(format(byte, '02x') for byte in bytes_read)
            outfile.write(hex_string)

def hex_to_bin(input_file, output_file):
    with open(input_file, 'r') as infile:
        hex_data = infile.read()

    binary_data = bytes.fromhex(hex_data)

    with open(output_file, 'wb') as outfile:
        outfile.write(binary_data)
    
def process_files_in_directory(directory_path, file_extension, output_file_extension, text_file_input=None, bytes_to_skip=0):
    log_data = []
    for filename in os.listdir(directory_path):
        if filename.lower().endswith(file_extension.lower()):
            input_file_path = os.path.join(directory_path, filename)
            output_file_path = os.path.splitext(input_file_path)[0] + output_file_extension

            if text_file_input:
                output_file_path = os.path.splitext(text_file_input)[0] + output_file_extension

            if args.bin2hex:
                bin_to_hex(input_file_path, output_file_path, bytes_to_skip=bytes_to_skip)
                print(f"Binary to hexadecimal conversion successful. Output saved in {output_file_path}")

                # Prepare log data
                with open(input_file_path, "rb") as infile:
                    infile.seek(bytes_to_skip)
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
    examples = [
        "Example 1: Convert all .a26 binary files in the current directory to hexadecimal.",
        "bin2hex-hex2bin-combined-v3.py -allbin a26 -b2h .",
        "",
        "Example 2: Convert binary files listed in 'input_files.txt' (with .a26 extension) to hexadecimal.",
        "bin2hex-hex2bin-combined-v3.py -allbin a26 -b2h -t input_files.txt"
    ]
    parser = argparse.ArgumentParser(
        description="Convert binary to hexadecimal or hexadecimal to binary for multiple files.\n\n" + "\n".join(examples),
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("-b2h", "--bin2hex", action="store_true", help="Convert binary to hexadecimal")
    parser.add_argument("-h2b", "--hex2bin", action="store_true", help="Convert hexadecimal to binary")
    parser.add_argument("-allbin", "--all_binary_files", metavar="EXTENSION", help="Process all binary files with the specified extension")
    parser.add_argument("-t", "--text_file_input", help="Provide a text file with filenames (one per line) as input")
    parser.add_argument("input_path", help="Input file or directory path for conversion")
    parser.add_argument("-s", "--skip_bytes", type=int, default=0, help="Number of bytes to skip at the beginning of each binary file")
    args = parser.parse_args()

    if args.all_binary_files:
        if os.path.isdir(args.input_path):
            process_files_in_directory(args.input_path, args.all_binary_files, ".txt", args.text_file_input, bytes_to_skip=args.skip_bytes)
        elif os.path.isfile(args.input_path):
            with open(args.input_path, 'r') as file:
                filenames = file.read().splitlines()
                for filename in filenames:
                    process_files_in_directory(os.path.dirname(filename), args.all_binary_files, ".txt", filename, bytes_to_skip=args.skip_bytes)
        else:
            print("Invalid input path. Please specify a valid file or directory path.")
    else:
        if args.bin2hex:
            bin_to_hex(args.input_path, args.input_path + ".txt", bytes_to_skip=args.skip_bytes)
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