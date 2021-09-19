# 標準入力を受け付ける。
H, W, C = map(int, input().split())

A = []
m = 10 ** 20
result = 10 ** 20
for i in range(0, H):
    inp = list(map(int, input().split()))
    A.append(inp)

    # ひと駅を建設するための最小コストを求めておく。
    m = min(m, min(inp))

for i in range(0, H):
    for j in range(0, W):
        a = A[i][j]

        # 10の6乗なのは、H, Wの上限が1000であるため。
        # 駅から駅の距離を1ずつ拡張する。
        for d in range(1, 10 ** 6):
            # A[i][j]とひと駅を建設するための最小コスト、距離を元に、距離単位における最小の総コストを演算する。
            if a + m + C * d > result:
                break
            for k in range(0, d + 1):
                # 探索する際に配列外のindexを指定したらbreakする。
                if i + k >= H:
                    break

                l = d - k

                # 上記の演算により、距離単位における最小の総コストが演算できたので、それ以内の距離の場合に最小の総コストになる場合がないのか探索する。
                if j + l < W:
                    result = min(result, a + A[i + k][j + l] + C * d)

                # 上記の演算により、距離単位における最小の総コストが演算できたので、それ以内の距離の場合に最小の総コストになる場合がないのか探索する。
                if j - l >= 0:
                    result = min(result, a + A[i + k][j - l] + C * d)

print(result)
