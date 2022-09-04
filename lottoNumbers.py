import random
count = 1
lottoNumbers = []

while count <= 6:
    k = random.randint(1, 49)
    if k not in lottoNumbers:  # 若沒有重複的數字則填入
        lottoNumbers.append(k)
        count += 1

for j in lottoNumbers:
    print(j, end=' ')
