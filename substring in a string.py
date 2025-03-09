import re

def count_substring(string, sub_string):
    # Using regex finditer to count overlapping occurrences
    matches = [m.start() for m in re.finditer(f"(?={re.escape(sub_string)})", string)]
    return len(matches) 

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
