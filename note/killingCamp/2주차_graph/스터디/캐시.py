from collections import deque
def solution(cacheSize, cities):
    time = 0
    cache = deque([])   #캐시 교체 알고리즘이 LRU(Least Recently Used)를 사용한다고 명시되어있기때문에 queue 사용
    for city in cities:
        if city.upper() in cache:   #새로 들어올 도시가 캐시에 있으면 시간 1
            time += 1
            cache.remove(city.upper())  #이미 있는거는 삭제하고 아래에서 다시 넣어줌
        else:   #새로 들어올 도시가 캐시에 없으면 시간 5
            time += 5

        if cacheSize > 0: #캐시가 0이면 아래 로직 필요없음
            if len(cache) < cacheSize: #아직 캐시 공간이 남았으면
                cache.append(city.upper())
            else:   #캐시 공간이 다 찼으면 가장 오래된 도시를 빼고 새로운 도시 넣어줌
                cache.popleft()
                cache.append(city.upper())

    return time


