class Solution:
    def partition(self, str):
        palindromes = []  #정답 담을 배열
        partitions = []  #가지치기를 진행하며 팰린드롬
        #str이 빈 문자열이면 빈 배열 리턴
        if not str:
            return []

        def backtrack(start, partitions):
            ## start가 str의 길이와 같게된다는건 아래 for문에서 각 가지치기를 진행하며 끝까지 팰린드롬을 만족했다는 뜻
            if start == len(str):
                palindromes.append(partitions[:])
            for i in range(start + 1, len(str) + 1):
                tmp_str = str[start:i]
                if tmp_str == tmp_str[::-1]:
                    partitions.append(tmp_str)
                    backtrack(i, partitions)
                    partitions.pop()

        backtrack(0, partitions)
        return palindromes



