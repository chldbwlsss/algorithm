import string
def solution(new_id):
    answer = ''
    accept_case = list(string.ascii_lowercase)
    accept_case = accept_case + list(map(str, range(10)))
    accept_case.append('-')
    accept_case.append('_')
    accept_case.append('.')
    # 1단계
    answer = new_id.lower()
    # 2단계
    temp = ''
    for char in answer:
        if char in accept_case:
            temp += char
    answer = temp

    # 3단계
    prev = ''
    temp = ''
    for char in answer:
        if char == '.':
            if prev == '.':
                pass
            else:
                temp += char
        else:
            temp += char
        prev = char
    answer = temp

    # 4
    if answer != '' and answer[0] == '.':
        answer = answer[1:]
    if answer != '' and answer[-1] == '.':
        answer = answer[:-1]

    # 5
    if answer == '':
        answer += 'a'

    # 6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    # 7
    if len(answer) <= 2:
        back = answer[-1]
        while len(answer) < 3:
            answer += back

    return answer