# Load Atari 2600 ROMs by UID
Development of support scripts for an Atari 2600 project I'm working on.

Perhaps I should describe how I imagine the final product will look that work my way backwards the steps needed in my attempt to accomplish this vision.

The goal is to use an x86 Atom SoC in combination with an Arduino to read an arbitrary 32 bytes of the ROM stored in an Atari 2600 cartridge, stored a hexadecimal string. This unique identifier would then be used to identify the matching ROM file and launch into an emulator such as Stella. 

That's the best summary I can come up with.

I've started to break down the steps to accomplish this goal already with a series of python scripts. I started developing the script without the aid of git so I ended up with different file names for prior versions. Amature hour version tracking ftw.

The current version of the python script, bin2hex-hex2bin-combined, will (in summary) take a directory as input and loop through the ROM files it finds capturing the 32 bytes and writing the file names and hex strings a single log file, tab-separated.  

If someone wanted to run the script for some reason, here is an example usage:

**``` .\bin2hex-hex2bin-combined-v8.py -allbin .a26 -b2h  .\roms\ -s 524 ```**

> **-allbin** - supposed to tell it to go through all binaries

> **.a26** - files with a26 extensions 

> **-b2h** - would like to do binary to hex conversion

> **.\roms\\** - path to directory - in this case relative path to "roms" directory. Can also take full paths or use the current directory with a period **.**

> **-s 524** - number of bytes into the binary file to start reading. 

I should probably mention there's a bit of functionality left over from debugging: when the script is run it creates a text file for each binary file it encountered and writes the hex string to it. In other words if you run this against 250 ROM files you'll have 250 txt files (plus the log file). This doesn't take much storage space, just possibly annoying. I'll take that out eventually.

The number of bytes to read is set to 32 in the script. This can just be changed arbirarily in the python script itself.

The 524 is actually an arbirary number I chose after seeing a ROM file with a 512 byte header. I wanted to skip over that header to avoid duplicate strings.

The script actually won't take a single file on the command line. That functionality got lost some where along the way. You can always use a txt file with the ROM name or put the ROM in a directory by itself. I don't know if it's worth adding arbirary single file pass-in or not.

## What's the use of this script? What's the point?

Firstly I needed a single text file associating unique hex strings to ROM file names, one per line. Which I've accomplished.

Secondly to find out if this approach is probably viable by finding little inconveniences like most ROMs not having a header while some ROMs at random actually do. So I'm glad I went through this little exercise because I definitely would not have otherwise known.

The log file produced by the script - creatively called **conversion_log-set to skip 524 bytes.txt** - was the real goal the script: This log file can be used as the input for my next script: test the viability by loading the data of the log file then sending the script random 32 byte strings from the same offset to make sure the hex string produced a match. I mean why wouldn't it - I just need a proof-of-concept.

With *that* script up and working, at least in concept I'll be able to put more emphasis on working with the Arduino and reading physical carts. That'll be a whole other thing, I'm sure.

I'm actually considering making the standard start point 640 bytes. This will skip over any headers and also it's hilarious. 