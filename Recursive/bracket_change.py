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
    if left == 0 and right == 0:
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

def solution(w):

    result = ''
    if correct_check(w):
        return w
    if w == '':
        return w
    
    u,v = split(w)
    if correct_check(u):
        result = u + solution(v)
    else:       
        u = ''.join(['(' if u[i] == ')' else ')' for i in range(1,len(u)-1)])
        STR = '(' + solution(v) + ')'+ u
        STR = STR.replace(" ","")
        result+=STR
        
    return result


