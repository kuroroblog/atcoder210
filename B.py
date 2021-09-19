# 標準入力を受け付ける。
N = int(input())
# 文字列Sをリスト型にする。
s = list(input())

for i in range(0, len(s)):
    # 初めてSi(iは0から始める)の値が`1`の場合のみを考える。
    if s[i] == '1':
        # iの値が偶数の場合`Takahashi`, 奇数の場合`Aoki`を出力する。
        if i % 2 == 0:
            print('Takahashi')
        else:
            print('Aoki')
        break
