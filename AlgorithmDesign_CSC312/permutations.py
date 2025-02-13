from collections import deque

def permutations(theperms,s,n,p):
    if len(p)==n:
        theperms.append(p)
    else:
        for i in range(len(s)):
            c = s[i]
            otherchars= s[:i]+s[i+1:]
            permutations(theperms,otherchars,n,p+c)


def main():
    s = input('Enter a string: ')
    perms = deque()
    permutations(perms,s,len(s),'')
    print(perms)

main()