from math import*;r,z=range,int
def p(n):
 k=[1]*(n-2)
 for i in r(2,z(sqrt(n))+1):
  if k[i-2]==1:
   j=i*i
   while j<n:
    k[j-2]=0;j+=i
#  print([i+2 for i in r(n-2)if k[i]==1][-1],[i+2 for i in r(n-2)if k[i]==1][-2])
 return sum([i+2 for i in r(n-2)if k[i]==1])
a=p(z(input()))
print(a)

# a=454396537
