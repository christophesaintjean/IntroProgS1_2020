def palindrome(ch):
    for i in range(len(ch)//2):
        if ch[i] != ch[-1-i]:
            return False
    return True

def palindrome_rev(ch):
    return ch == ch[::-1]

def palindrome_rec(ch):
    if len(ch) < 2:
        return True
    if ch[0] != ch[-1]:
        return False
    return palindrome_rec(ch[1:-1])


palin , no_palin= "battab", "bartiutrab"

print(palindrome(palin))
print(palindrome_rev(palin))
print(palindrome_rec(palin))