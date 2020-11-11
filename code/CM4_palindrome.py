palin , no_palin= "battab", "bartiutrab"

def palindrome(ch):
    for i in range(len(ch) // 2):
        if ch[i] != ch[-1-i]:
            return False
    return True

def palindrome_rec(ch):
    if len(ch) < 2:
        return True
    if ch[0] != ch[-1]:
        return False
    else:
        return palindrome_rec(ch[1:-1])



print(palindrome(no_palin))
print(palindrome_rec(no_palin))