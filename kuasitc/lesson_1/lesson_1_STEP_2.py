# STEP_2:計算標準差
# 我們在這裡以取得1~5數字的標準差為例:

#----<全域變數區域>----
mean = 0	# 平均值
add = 0		# 差值平方的累加
total = 0	# 差值平方總和除以數字數量
squart = 0	# 開根號後的結果
#------------計算平均值START------------
def calc_mean( numbers ):	# 取得平均值
	global mean
	count_m = float( len(numbers) )
	total_m = 0
	for number in numbers:
		total_m = total_m + number

	mean = total_m/count_m
	return mean
#---------------END----------------


#------------STEP_2:計算標準差---------------
# 利用平均值來計算標準差
# (1)把每個數值和平均值相減，差值平方並累加
def calc_add( numbers ):
	global add
	global mean
	for number in numbers:
		add = add + (number - mean)**2
	return add
# (2)把累加的差值平方總和除以輸入的數字數量
def calc_total( numbers ):
	global total
	total = add/float(len(numbers))
	return total
# (3)將結果開根號
def calc_squart():
	global squart
	squart = total**(0.5)
	return squart
#---------------END_STEP_2----------------
calc_mean( [1, 2, 3, 4, 5] )
calc_add( [1, 2, 3, 4, 5] )
calc_total( [1, 2, 3, 4, 5] )

print(calc_squart())
