import re


def longest_substring(lines):
    longest = ('', 0)
    for i, _ in enumerate(lines):
        line = lines.pop(0)
        chops = re.findall(r'\w+', line)
        for chop in chops:
            found = 0
            for nl in lines:
                found += len(re.findall(chop, nl))
        if found >= 2 and found > longest[1]:
            longest = (chop, found)
        lines.append(line)
    return longest[0]

