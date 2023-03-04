### 단어 공부 ###
w = input().lower()   # 입력 받기
w_list = list(set(w))  # set 함수 이용해서 중복 제거
cnt = []    # 중복 문자 개수 담을 리스트

for i in w_list:    # 중복제거한 리스트에서 하나씩 보면서
    count = w.count(i)  # count 함수를 이용해서 원래 리스트에 해당 문자가 몇개 있는지?
    cnt.append(count)   # 개수 cnt 리스트에 담아주기

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(w_list[(cnt.index(max(cnt)))].upper())    # cnt 리스트에서 max값 인덱스는 중복 제거한 리스트에서의 인덱스 값과 같다




