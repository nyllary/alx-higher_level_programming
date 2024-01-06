#!/usr/bin/python3
import sys

if len(sys.argv) == 1:
    print(len(sys.argv) - 1, "arguments.")

for i in range(1, len(sys.argv)):
    if len(sys.argv) > 2:
        print(len(sys.argv) - 1, "arguments:", i,\
                ":", sys.argv[i])
        # print(i, ":", sys.argv[i])
    elif len(sys.argv) == 2:
        print(len(sys.argv) - 1, "argument:")
        print(i, ":", sys.argv[i])
