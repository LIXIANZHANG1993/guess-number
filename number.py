#猜數字遊戲 練習
import random
number = random.randint(1, 100)

while True:
	ans = input('猜數字，請輸入1到100的數字:')
	ans = int(ans)
	if number == ans:
		print('恭喜你答對了')
		break
	elif number > ans:
		print('再大一點')
	elif number < ans:
		print('再小一點')