def reverse_string(s:str) -> str :
    s = list(s)
    left = 0
    right = len(s)-1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return"".join(s)
a="hello"
print(reverse_string(a))
