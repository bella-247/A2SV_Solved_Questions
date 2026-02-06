n, k = list(map(int, input().split()))
scores = list(map(int, input().split()))
wanted_score = scores[k-1]

print(sum(1 for score in scores if 0 < score >= wanted_score))
