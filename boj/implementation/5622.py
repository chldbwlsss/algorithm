### 다이얼 ###
alpha = ['ABC','DEF','GHI', 'JKL','MNO','PQRS','TUV','WXYZ']
a = input()
time = 0

for i in range(len(a)):
    for j in alpha:
        if a[i] in j:
            time += alpha.index(j) + 3

print(time)

