def infix_to_postfix(exprsn):
    stack=[]
    output=[]
    precedence={
        '+':1,'-':1,'*':2,'/':2
    }
    for ch in exprsn:
        if ch.isalnum():
            output.append(ch)
        elif ch=='(':
            stack.append(ch)
        elif ch==')':
            while stack and stack[-1]!='(':
                output.append(stack.pop())
            stack.pop()
        else:
            while (stack and
                   stack[-1] != '(' and
                   precedence[stack[-1]] >= precedence[ch]):
                output.append(stack.pop())
            stack.append(ch)
    while stack:
        output.append(stack.pop())

    return ''.join(output)

print(infix_to_postfix("A+B*C"))
print(infix_to_postfix("(A+B)*C"))
print(infix_to_postfix("A*B+C"))

        