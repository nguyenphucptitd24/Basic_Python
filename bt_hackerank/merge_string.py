def merge_the_tools(string, k):
    substrings = [string[i:i+k] for i in range(0, len(string), k)]
    for sub in substrings:
        seen = set()
        result_list = []
        for char in sub:
            if char not in seen:
                seen.add(char)
                result_list.append(char)
        print(''.join(result_list))

string, k = input(), int(input())
merge_the_tools(string, k)