# Coded GCD algorithm
# open(0): This approach allows the program to efficiently read the input data 
# provided by the Kattis platform without the need for explicit user input prompts.


def gcd(x,y):
    if y>x:x,y=y,x
    if x==0:return y
    if y==0:return x
    return gcd(y,x%y)
a=[*map(int,open(0).read().split())]
print(*[f'{a[1]//(l:=gcd(a[1],x))}/{x//l}'for x in a[2:]],sep='\n')