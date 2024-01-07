## 정답풀이
# def solution(key, lock):
#     m = len(key)
#     n = len(lock)
#     keys = [[[0 for _ in range(m + 2 * n)] for _ in range(m + 2 * n)] for _ in range(4)]
#
#     for i in range(m):
#         for j in range(m):
#             keys[0][n + i][n + j] = key[i][j]
#             keys[1][n + j][m + n - 1 - i] = key[i][j]
#             keys[2][m + n - 1 - i][m + n - 1 - j] = key[i][j]
#             keys[3][m + n - 1 - j][n + i] = key[i][j]
#
#     for k in keys:
#         for i in range(m + n):
#             for j in range(m + n):
#                 flag = True
#                 for ii in range(n):
#                     for jj in range(n):
#                         if not lock[ii][jj] ^ k[i + ii][j + jj]:
#                             flag = False
#                 if flag:
#                     return True
#     return False

## 연습
def solution(key, lock):
    m = len(key)
    n = len(lock)
    #keys = 열쇠의 가능한 회전 경우의 수를 사전 저장할 배열
    keys = [[[0 for _ in range(m+2*n)] for _ in range(m+2*n)]for _ in range(4)]

    #keys를 시각적으로 보면 (문제와 같이 m=3, n=3일때)
    # keys = [
    #     [
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0]
    #     ],
    #     [
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0]
    #     ],
    #     [
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0]
    #     ],
    #     [
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0]
    #     ]
    # ]

    #keys[0] = 0도 회전된 열쇠
    #keys[1] = 90도 회전된 열쇠
    #keys[2] = 180도 회전된 열쇠
    #keys[3] = 270도 회전된 열쇠
    ## 위 4가지 경우를 keys에 담는 과정
    for i in range(m):
        for j in range(m):
            key[0][n+i][n+j] = key[i][j] #i+n, j+n을 해주는 이유는 key보다 더 크게 만든 정사각형 key[0] 배열에서 가운데에 key를 위치하게 하기 위함!
            key[1][n+j][n+m-i-1] = key[i][j]
            key[2][n+m-i-1][n+m-j-1] = key[i][j]
            key[3][n+m-j-1][n+i] = key[i][j]

    for k in keys:
        for i in range(n+m):  #n+m -> 굳이 마지막에 key와 겹치지 않는 부분을 볼 필요가 없다
            for j in range(n+m):
                is_locked = True #기본값 True 설정 -> "이 로직 아래에서 is_locked이 False가 되는 경우를 찾겠다" 라는 뜻
                #자물쇠와 키가 맞아지는 *자물쇠*를 순회
                for a in range(n):
                    for b in range(n):
                        if not lock[a][b] ^ k[i+a][j+b]:  #자물쇠와 키가 둘다 0과 0일때는 안됨
                            is_locked = False
                if is_locked:
                    return True
    return False


