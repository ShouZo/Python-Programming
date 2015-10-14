import json		# 載入 json

## 1. 讀取"camera.json"，並把它轉成"object"
open_file = open('camera.json', 'r', encoding = 'utf-8')	# 將讀取編碼設為"utf-8"
tmp_files = open_file.read()	
input_data = json.loads(tmp_files)	# 把 json 檔案改成 object
open_file.close()	# 關閉檔案


## 2. 提示使用者輸入欲查詢的路名(要用中文)
# 讓使用者輸入資料
user_input = input('Please use chinese to enter road name in Kaohsiung : ')
# 過濾資料
user_input = user_input.replace('路', '')


## 3. 在查詢結果前，在螢幕上顯示"項目意義"
print('行政區\t測照方向\t測照地點')	
print('*' * 50)		# 用來產生分隔線


## 4. 查詢輸入的資料
for data in input_data:		# 依照資料的筆數("input_data")進行迴圈
# 判斷資料裡面是否有我們要找的東西
	if user_input in data['測照地點']:
		print('%s\t%s\t\t%s' % (data['行政區'], data['測照方向'], data['測照地點']))


