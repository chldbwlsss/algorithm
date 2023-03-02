### 나머지 ###
## 결과(나머지)를 다 넣을생각 하지말고, 걸러서 넣자
arr = []

for i in range(10):
    a = int(input())
    if a % 42 not in arr:
        arr.append(a % 42)

print(len(arr))
