### 알파벳 찾기 ###
s = str(input())
alphabet = "abcdefghijklmnopqrstuvwxyz"

for item in alphabet:
    print(s.find(item), end=' ')