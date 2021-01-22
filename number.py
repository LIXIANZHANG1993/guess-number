#猜數字遊戲 練習
import random
number = random.randint(1, 100)
ans = input('猜出正確數字，請輸入1到100的數字:')
ans = int(ans)
i = 100
while i > 0:
	i = i - 1
	if number == ans:
		print('恭喜你答對了')
		break
	elif number >= ans:
		print('再小一點')
	else:
		print('再大一點')