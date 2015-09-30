# STEP_4:計算結果後輸出
# 提供使用者輸入數字的功能；如果沒有輸入數字，就會顯示：Please input numbers

import sys		# 匯入"sys"模組(載入命令列)

#------------(副程式)計算標準差---------------
def calc_STEP_2(numbers):
	total_m = 0
	add = 0
	count = float(len(numbers))	# 取得陣列元素的數量

	for number in numbers:		# (1)算出平均值
		total_m = total_m + float(number)
	mean = total_m / count

	for number in numbers:		# (2)把每個數值和平均值相減，差值平方並累加
		add = add + (float(number) - mean) ** 2

	total = add / count			# (3)把累加的差值平方總和除以輸入的數字數量
	
	squart = total ** (0.5)		# (4)將結果開根號
	return squart
#---------------END_STEP_2----------------

#------------(主程式)處理命令列參數---------------
# 先判斷sys.argv[]是否有參數? (要排除"sys.argv[0]")
# 如果有，將該參數附加存入陣列內
array = list()
lenth = int(len(sys.argv))
# for 迴圈是以"tab"為縮排,
# 縮排內都是它的執行範圍
if lenth >= 2:
	for argv in sys.argv[1:]:	# 從"sys.argv[1]"開始
		array.append(argv)		# 有'Tab'縮排(迴圈範圍)

	print(calc_STEP_2(array))	# 無'Tab'縮排(非迴圈範圍)

else:
	print('Please input numbers')
#------------------------END-------------------------
