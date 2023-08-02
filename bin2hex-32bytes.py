'''
I created this script - of GPT did - 
to sample out put of the first 32bytes of the binary rom files 
to give to GPT as sample output for a log file i wanted it to write for 
bin2hex-hex2bin-combined-v4 or v5 probably
I assume if i wanted this to be stand a lone i could do that


'''
infile = open('Adventure (USA).a26', 'br' ) 

line_data = ""
bytes_to_read = 32

while bytes_to_read > 0: # overly easy way to just-keep-reading the binary
    bytes_read = infile.read(32) # i'm actually not sure what the 16 is for. 16 bytes at time?
    if not bytes_read: # dumb way saying "until end of file"
        break # breaks out of the while true infinite loop
    for byte in bytes_read: # loop through the data captured in the byte_read variable
        byte_hex = format(byte, '02x') # apparently format it as "02 hex" which means hex expresssed only as 2 characters, e.g. FF is the highest
        line_data += byte_hex # use this variable to consilate this new hex value one value at a time
        bytes_to_read -= 1
infile.close() # have to remember to close the file when done

print(line_data)


#Boxing_La_Boxe_1980.bin    78d8a2ff9ae88a9500e8d0fbe6dd20c6f34c6ff1a8b1a4851bb1a6852038a88a

#with open('Boxing_La_Boxe_1980_in_hex.txt', 'w') as outfile:
#    outfile.write(line_data)

#Boxing_La_Boxe_1980.bin    78d8a2ff9ae88a9500e8d0fbe6dd20c6f34c6ff1a8b1a4851bb1a6852038a88a
#Adventure (USA).a26    4ceff278d84c06f3852ba586a20020d2f0a588a20120d2f0a58ba20420d2f085