# 標準入力を受け付ける。
N, K = map(int, input().split())
C = list(map(int, input().split()))

# キャンディの種類数情報
kinds = {}
# 先頭から連続するK個を取得して、種類数を求める。
for i in range(0, K):
    # 参考 : https://note.nkmk.me/python-dict-get/
    if kinds.get(C[i]) is None:
        kinds[C[i]] = 1
    else:
        kinds[C[i]] += 1

# 要素数 = 種類数
ans = len(kinds)

# 連続するK個の探し方 = i番目の要素を削除し、K + i番目の要素の追加を繰り返すことを意味する。
for i in range(0, N - K):
    # 種類として外す処理
    # 参考 : https://note.nkmk.me/python-dict-clear-pop-popitem-del/
    kinds[C[i]] -= 1
    if kinds[C[i]] == 0:
        kinds.pop(C[i])

    # 種類として追加する処理
    if kinds.get(C[i + K]) is None:
        kinds[C[i + K]] = 1
    else:
        kinds[C[i + K]] += 1

    # 種類数の確認処理
    ans = max(ans, len(kinds))

print(ans)
