### 과제 안 내신 분..? ###
## 일단 다 준비해놓고 삭제하는 방식
student = [i for i in range(1, 31)]

for _ in range(28):
    num = int(input())
    student.remove(num)

print(min(student))
print(max(student))

