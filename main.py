import re
import json

def ncreplace(p):
    pc = re.sub("[a-z]", 'c', p)
    pc = re.sub("[A-Z]", 'C', pc)
    pc = re.sub("[0-9]", 'n', pc)
    return pc
# converted to nnnn-nnn-Ccc format

def shift_table(m, n):
    if m < n:
        return -1
    shift = []
    for k in range(256):
        shift.append(m)
    for k in range(m - 1):
        shift[ord(s[k])] = m - k - 1
    shift = tuple(shift)  # shift table created
    return shift
# m = len of main string, n = len of pattern string
def bmh(m, n):
    k = n - 1
    while k < m:
        j = n - 1; i = k
        while j >= 0 and s[i] == p[j]:
            j -= 1; i -= 1
        if j == -1: 
            return i + 1
        k += skip[ord(s[k])]
    return -1

def write_json(new_data, filename = 'json_data.json'):
    with open(filename, 'r+') as f:
        file_data = json.load(f)
        file_data["PatternBMHTable"].append(new_data)
        f.seek(0)
        json.dump(file_data, f, indent=4)

if __name__ == "__main__":
    s = "The policy number is 5641-236-erk"
    m = len(s)
    p = "5"
    n = len(p)
    skip = shift_table(m, n)
    print(skip)
    new_data = {"Pattern": p, "BMH Shift table": skip}
    # write_json(new_data)
    t = bmh(m, n)
    if t > -1:
        print(t)
