# STEP_2:計算標準差
# 我們在這裡以取得1~5數字的標準差為例:

#------------STEP_2:計算標準差---------------
def calc_STEP_2( numbers ):
	total_m = 0
	add = 0
	count = float( len(numbers) )	# 取得陣列元素的數量

# (1)算出平均值
	for number in numbers:	
		total_m = total_m + number
	mean = total_m / count

# (2)把每個數值和平均值相減，差值平方並累加
	for number in numbers:	
		add = add + (number - mean)**2

# (3)把累加的差值平方總和除以輸入的數字數量
	total = add / count	

# (4)將結果開根號	
	squart = total**(0.5)	
	return squart
#---------------END_STEP_2----------------
print(calc_STEP_2( [1, 2, 3, 4, 5]) )
