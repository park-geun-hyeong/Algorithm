import sys
read = sys.stdin.readline


def solution(S):
    length = len(S)
    if length == 1:
        return 1
    elif list(S).count(S[0]) == len(S):
        return len("{}{}".format(len(S), S[0]))

    answer = length

    for window in range(1, length // 2 + 1):
        new_string = ''
        now_word = S[0:window]
        cnt = 1
        for i in range(window, length, window):
            next_word = S[i:i + window]
            if now_word == next_word:
                cnt += 1
                continue
            else:
                new_string += "{}{}".format(cnt, now_word) if cnt != 1 else "{}".format(now_word)
                cnt = 1
                now_word = next_word

        new_string += "{}{}".format(cnt, now_word) if cnt != 1 else "{}".format(now_word)
        answer = min(answer, len(new_string))

    return answer


if __name__ == "__main__":
    S = input()
    print(solution(S))