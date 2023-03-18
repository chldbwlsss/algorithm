### 팰린드롬인지 확인하기 ###
word = list(input())
word_reverse = list(reversed(word))

# print(''.join(word)) # list to String
# print(''.join(word_reverse))

if ''.join(word) == ''.join(word_reverse):
    print(1)
else:
    print(0)