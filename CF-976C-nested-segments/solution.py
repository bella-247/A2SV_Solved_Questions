def nestedSegments(n, segments):
 
    mapp = {}
 
    for i, segment in enumerate(segments):
        if segment in mapp:
            return i + 1, mapp[segment]
 
        mapp[segment] = i + 1
 
    segments.sort(key=lambda x: (x[0], -x[1]))
 
    for i in range(1, n):
        curr_segment = segments[i]
        prev_segment = segments[i - 1]
        
        if curr_segment[1] <= prev_segment[1]:
            return mapp[curr_segment], mapp[prev_segment]
 
    return -1, -1
 
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
 
print(*nestedSegments(n, segments))