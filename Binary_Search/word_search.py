'''
## pay attention more at time limit ...

from bisect import bisect_left, bisect_right
import sys 
read = sys.stdin.readline

def show_idx(words_length, query):
    target = len(query)
    left_idx = bisect_left(words_length, target)
    right_idx = bisect_right(words_length, target)
    
    return [left_idx, right_idx]    
    
def correct_check(word ,query):
    word = list(word)
    query = list(query)
    
    for i in range(len(word)):
        if query[i] == '?':
            continue
        
        if query[i] != word[i]:
            return False
    
    return True

def solution(words, queries):
    
    words = sorted(words, key = len)
    words_length = [len(i) for i in words]
    answer = []
    
    for q in queries:
        cnt = 0
        left_idx, right_idx = show_idx(words_length, q)
        if right_idx == 0:
            answer.append(0)
            continue
            
        for i in range(left_idx, right_idx):
            if correct_check(words[i], q):
                cnt += 1
        answer.append(cnt)
    
    return answer
'''
# https://programmers.co.kr/learn/courses/30/lessons/60060

from bisect import bisect_left, bisect_right
import sys 
read = sys.stdin.readline

def cnt_check(left_value, right_value, array):
    
    left_idx = bisect_left(array, left_value)
    right_idx = bisect_right(array, right_value)
    
    return right_idx - left_idx

def solution(words, queries):
    
    words_split= [[[],[]] for _ in range(10001)]
    for i in words:
        words_split[len(i)][0].append(i)
        words_split[len(i)][1].append(i[::-1])
    
    for i in range(10001):
        words_split[i][0].sort()
        words_split[i][1].sort()
        
    answer = []
    
    for q in queries:
        
        if q[-1] == '?':
            array = words_split[len(q)][0]
            left_value = q.replace('?', 'a')
            right_value = q.replace('?', 'z')
            
        elif q[0] == '?':
            array = words_split[len(q)][1]
            left_value = q[::-1].replace('?', 'a')
            right_value = q[::-1].replace('?', 'z')
                 
        answer.append(cnt_check(left_value, right_value, array))    
    
    return answer

if __name__ == "__main__":
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
    print(solution(words, queries))
    
            

