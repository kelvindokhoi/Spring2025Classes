# kmp

def failure(pattern):
    len_ = 0
    m = len(pattern)
    f = [0 for _ in range(m)]
    i =1
    while i<m:
        if pattern[i] == pattern[len_]:
            len_ += 1
            f[i] = len_
            i += 1
        else:
            if len_ != 0:
                len_ = f[len_ -1]
            else:
                f[i] = 0
                i += 1
    return f

def kmp(text,pattern):
    fail = failure(pattern)
    i = 0
    j = 0
    m = len(pattern)
    while i < len(text):
        if pattern[j] == text[i]:
            if j == ~-m:return i-m+1
            i += 1
            j += 1
        elif j>0:
            j = fail[j-1]
        else:
            i+=1
    return ~0




text = 'catincaticacacccatinhaca'
text = 'barbarianbarbarbara'
pattern = 'barbara'
print(failure(pattern))
print(kmp(text,pattern))
