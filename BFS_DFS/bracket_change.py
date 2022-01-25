def correct_check(p):
    left=0
    right=0

    for i in p:
        if i == "(":
            left+=1
        elif i == ")":
            if left>0:
                left-=1
            else:
                right+=1
    if left == 0 and rignt == 0:
        return True
    else: 
        return False

    
def split(p):
    if p =='':
        return p
    left = 0
    right = 0
    
    cnt = 0
    for i in p:
        cnt += 1
        if i == "(":
            left += 1           
        elif i == ")":
            right += 1
                   
        if left == right:
            return (p[:cnt], p[cnt:])

result = ''
def recursive(w):
    global result
    if correct_check(w):
        return w
    if w == '':
        return w
    
    u,v = split(w)
    if correct_check(u):
        recursive(v)
    else:       
        u = ''.join(['(' if u[i] == ')' else ')' for i in range(1,len(u)-1)])
        STR = '(' + recursive(v) + ')'+ u
        STR = STR.replace(" ","")
        result+=STR
        
    return u + result


            
if __name__ == "__main__":
    p1="(()())()"
    p2= ")("
    p3= "()))((()"
    print(recursive(p1))
