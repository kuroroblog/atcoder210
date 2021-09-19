# 標準入力を受け付ける。
N, A, x, y = map(int, input().split())

# N - Aを実行してY円で購入するキャベツの数を洗い出す。
nokori = N - A

# N - A > 0の時、A個のキャベツをX円で買い、A + 1以降のキャベツをY円で買う。
if nokori > 0:
    print(nokori * y + A * x)
# N - A <= 0の時、全てのキャベツをX円で買う。
else:
    print(N * x)
