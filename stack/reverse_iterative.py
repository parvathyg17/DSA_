def reverse_stack(stack):
    temp = []

    while stack:
        temp.append(stack.pop())

    while temp:
        stack.append(temp.pop())

stack = [10, 20, 30]

reverse_stack(stack)

print(stack)