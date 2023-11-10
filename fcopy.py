import sys
def fcopy(file1, file2):
    with open(file1, 'r') as file3:
        with open(file2, 'w') as file4:
            for i in file3:
                file4.write(i)
def main(arg1, arg2):
    if arg1 != None and arg2 != None:
        fcopy(arg1, arg2)
    else:
        raise ValueError("Usage: fcopy.py<src><dest>")
if __name__ == "__main__":
    main()