'''condition: open <closed
add open if open<n
add close if close<open
valid if open==closed==n'''
n=3
stack=[]
res=[]
def backtrack(openC,closedC):
    #base condition
    if openC==closedC==n:
        res.append("".join(stack))

    #left condition
    if openC<n:
        stack.append("(")
        backtrack(openC+1,closedC)
        stack.pop()#needed for clean up
    
    if closedC<openC:
        stack.append(")")
        backtrack(openC,closedC+1)
        stack.pop()
    
backtrack(0,0)
print(res)
    
