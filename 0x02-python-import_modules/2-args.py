#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv) - 1

    print("{} argument".format(args), end='')

    if args == 0:
        print("s.")
    elif args == 1:
        print(":")
    else:
        print("s:")

    for i in range(args):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
