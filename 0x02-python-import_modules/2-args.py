#!/usr/bin/python3
import sys
argc = len(sys.argv)

if argc == 1:
    print(argc - 1, "arguments.")
elif argc == 2:
    print(argc - 1, "argument:")
    print("1:", sys.argv[1])
else:
    print(argc - 1, "arguments:")
    for i in range(1, argc):
        print(i, end=": ")
        print(sys.argv[i])
