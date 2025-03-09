import math



def valof(expression):
    stack=[]
    for c in expression:
        if c.isdigit():
            stack.append(int(c))
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            if c == '-':
                stack.append(-op1+op2)
            if c == '*':
                stack.append(op1*op2)
            if c == '+':
                stack.append(op1+op2)
        print(stack)
    return stack[0]


    # return eval(expression)

while True:
    expression = input("Enter a valid RPN expression: ")
    print(valof(expression))