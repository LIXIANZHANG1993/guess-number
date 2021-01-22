#猜數字遊戲 練習
import random

start = input('請輸入隨機數字開始值:')
end = input('請輸入隨機數字結束值:')
start = int(start)
end = int(end)
number = random.randint(start, end)

count = 0
while True:
	count += 1 #就是count = count + 1的快寫法
	ans = input('請猜數字:')
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