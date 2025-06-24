'''Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.'''

s="([{}])"
stack=[]
for i in s:
    if i in "{[(":
        stack.append(i)
    elif i in ")":
        if stack.pop()!="(":
            print("false")
    elif i in "}":
        if stack.pop()!="{":
            print("false")
    elif i in "]":
        if stack.pop()!="[":
            print("false")
if stack!=[]:
    print("false")
print("true")
    