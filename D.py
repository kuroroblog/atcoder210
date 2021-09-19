# 標準入力を受け付ける。
H, W, C = map(int, input().split())

A = []
m = 10 ** 20
result = 10 ** 20
for i in range(0, H):
    inp = list(map(int, input().split()))
    A.append(inp)

    # 駅を建設するための最小コストを求めておく。
    m = min(m, min(inp))

for i in range(0, H):
    for j in range(0, W):
        a = A[i][j]

        # 10の6乗なのは、H, Wの上限が1000であるため。
        # 駅から駅の距離を1ずつ拡張する。
        # aと最小コスト駅を選んだ場合のコストを演算して、最小値と比較する。
        for d in range(1, 10 ** 6):
            if a + m + C * d > result:
                break
            for k in range(0, d + 1):
                if i + k >= H:
                    break

                l = d - k

                if j + l < W:
                    result = min(result, a + A[i + k][j + l] + C * d)

                if j - l >= 0:
                    result = min(result, a + A[i + k][j - l] + C * d)

print(result)
