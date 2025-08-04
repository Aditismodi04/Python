def palindrom(s):
    s = s.lower()
    new_s = ""
    for ch in s:
        if ch.isalpha():
            new_s += ch
    return new_s == new_s[::-1]
print(palindrom("abc"))
print(palindrom("yoy"))