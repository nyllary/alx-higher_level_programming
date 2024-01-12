#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

argc = len(argv)

if argc == 1:
    print(argc - 1, "arguments.")
elif argc == 2:
    print(argc - 1, "argument:")
    print("1:", argv[1])
else:
    print(argc - 1, "arguments:")
    for i in range(1, argc):
        print(i, end=": ")
        print(argv[i])
