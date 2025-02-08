def fib(n,memo={0:0,1:1}):
    if n in memo:
        return memo[n]
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
    # for i in range(100):
    #     a.append(a[b]+a[b-1])
    #     b+=1
    # return (a[n])
# def fib(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     return fib(n-1)+fib(n-2)

for i in range(20000):
    print(fib(i))