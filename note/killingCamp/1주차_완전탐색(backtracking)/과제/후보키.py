# ## combinations
# def solution(relation):
#     col_len = len(relation[0])
#     row_len = len(relation)
#
#     candidate_keys = []
#
#     def gen_combinations(start, depth, max_depth, curr, result_combs):
#         if depth == max_depth:
#             result_combs.append(curr[:])
#             return
#         for i in range(start, col_len):
#             curr.append(i)
#             gen_combinations(i + 1, depth + 1, max_depth, curr, result_combs)
#             curr.pop()
#
#
#     for length in range(1, col_len+1):
#         combinations = []
#         gen_combinations(0, 0, length, [], combinations)
#
#         for cols in combinations:
#             minimality = True
#             row_set = set()
#
#             #최소성 검사
#             for key in candidate_keys:
#                 if set(key).issubset(set(cols)):  #key에 있는 요소 모두가 cols에 포함되어있으면 True
#                     minimality = False
#                     break
#             if not minimality:
#                 continue
#
#             #유일성
#             for r in relation:
#                 row_str = "".join(r[c] for c in cols)
#                 row_set.add(row_str)
#
#             if len(row_set) == row_len:
#                 candidate_keys.append(cols)
#
#         return len(candidate_keys)

## itertools
from itertools import chain, combinations
# 1. 모든 부분집합 구하기
#어떤 리스트가 들어왔을때 모든 부분집함(열의 쌍)을 구하는 함수
def get_all_subset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

# 2. 부분집합중 유일성 만족하는 부분집합 구하기
#부분집합 중에서 유일성을 만족하는 부분집합(열의 쌍)을 구하는 함수
def get_all_unique_subset(relation):
    #위에 만들어놓은 함수로 부분집합 구하기
    subset_list = get_all_subset(list(range(0, len(relation[0]))))
    unique_list = [] #유일성 만족하는 집합 리스트
    #유일성 만족 여부 체크
    for subset in subset_list:
        unique = True
        row_set = set()
        for i in range(len(relation)):
            row = ''
            for j in subset:
                row += relation[i][j] + '.'
            if row in row_set:
                unique = False
                break #반복문 깨기
            row_set.add(row)
        if unique:
            unique_list.append(subset)
    return unique_list

# 3. 유일성 만족하는 부분집합중에서 최소성을 만족하는 부분집합만 남기기
def solution(relation):
    unique_list = get_all_unique_subset(relation)
    #unique_list의 항목들을 그 길이에 따라 오름차순으로 정렬
    unique_list = sorted(unique_list, key=lambda x:len(x))
    # 부분집합중에서 최소성을 만족하는 부분집합(열의 쌍)을 구하기
    # 크기가 더 작은 부분집합이, 크기가 더 큰! 부분집합의 부분집합이 되는지 확인하자
    answer_list = []
    for subset in unique_list:
        subset = set(subset)  #리스트타입을 집합으로 변환
        minimality = True
        for j in answer_list:
            #지금 보려는 부분집합이 이미 answer_list에 들어있는지 확인
            if j.issubset(subset):
                #있으면 최소성 만족 못함
                minimality = False
        if minimality == True:
            answer_list.append(subset)
    return len(answer_list)












