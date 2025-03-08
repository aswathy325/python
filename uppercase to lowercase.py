def swap_case(s):
    #res=s.swapcase()
    outputstring=""
    for i in s:
        if i.isupper():
            o=i.lower()
        elif i.islower():
            o=i.upper()
        else:
            o=i
        outputstring+=o
    return outputstring

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
