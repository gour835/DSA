from Stacks import Stack


def Balanced_Brackets(l):
    o = '{[('
    c = '}])'
    s = Stack()
    l1 = l
    for i in l:
        if i in o:
            s.push(i)
        elif i in c:
            # peek through the stack
            if i == ')' and s.peek() == '(':
                s.pop()
            elif i == ']' and s.peek() == '[':
                s.pop()
            elif i ==  '}'and s.peek() == '{':
                s.pop()
            else:
                return False

        l = l[1:]
    if len(l) == 0 and s.count() == 0:
        return True
    else:
        return False
    
            

s1 = "[{(a+b) + (a-b)}]"
s2 = "[{(a+b) + (a-b)]}"
s3 = '(a+b)('

print(
Balanced_Brackets(s3)
)
