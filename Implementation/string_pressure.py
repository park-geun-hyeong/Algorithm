import sys 
read  = sys.stdin.readline

def solution(S):
    
    length = len(S)
    short_len = [length] 
    
    for window in range(1, length // 2 + 1):
        start = 0
        new_string = ''
         
        for i in range(length - window+1):
            if i == start: 
                if len(S[i:]) < 2*window:
                    new_string += S[i:]
                    break
                    
                now_word = S[i:i+window]
                if now_word != S[i+window: i+2*window]:
                    new_string += now_word
                    start = i+window                
                    continue

                else:    
                    num = 1
                    for j in range(i+window, length - window+1, window):
                        next_word = S[j: j+window]
                        if now_word == next_word:
                            num += 1
                            start = j+window
                        else:
                            break


                    new_string += "{}{}".format(num, now_word)
                    continue
            
            else:
                continue
                
        short_len.append(len(new_string))       
        
    answer = min(short_len) 
    return answer
    
if __name__ == "__main__":
    S = input()
    print(solution(S))
