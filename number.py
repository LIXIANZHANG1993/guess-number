#猜數字遊戲 練習
import random
number = random.randint(1, 100)
count = 0
while True:
	count += 1 #就是count = count + 1的快寫法
	ans = input('猜數字，請輸入1到100的數字:')
	ans = int(ans)
	if number == ans:
		print('恭喜你答對了')
		print('這是你猜的第', count, '次')
		break
	elif number > ans:
		print('再大一點')
	else:
		print('再小一點')
	print('這是你猜的第', count, '次')