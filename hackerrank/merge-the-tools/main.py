def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substr = string[i:i+k]
        d = {c: 1 for c in substr}
        print(''.join(list(d.keys())))

if __name__ == '__main__':
    string, k = 'AABCAAADA', 3
    merge_the_tools(string, k)