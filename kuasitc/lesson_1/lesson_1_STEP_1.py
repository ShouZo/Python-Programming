# STEP_1:計算平均值
# 我們在這裡以取得1~5數字的平均值為例:

#------------STEP_1:計算平均值(副程式START)------------
def calc_mean( numbers ):	# 取得平均值
	count_m = float( len(numbers) )
	total_m = 0
	for number in numbers:
		total_m = total_m + number
	mean = total_m/count_m
	return mean
#---------------END_STEP_1(副程式END)----------------

print( calc_mean( [1, 2, 3, 4, 5]) )	# 輸出計算結果
