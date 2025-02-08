
def Helper(s,b,e):
    if b>=e:
        return True
    if s[b]!=s[e]:
        return False
    else:
        return Helper(s,b+1,e-1)

def isPalindrome(s):
    return Helper(s,0,len(s)-1)



s=input()
print(isPalindrome(s))