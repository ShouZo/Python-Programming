import json

## 1. 讀取"camera.json"檔，設定讀取編碼為 : "utf-8"
f = open( 'camera.json ', 'r', encoding = 'utf-8' )		# 開啟檔案
s = f.read()	# 將讀取的內容存至"s"
f.close()	# 關閉檔案


## 2. 把"文字檔"轉換 json object
json_obj = json.loads( s )	# 將"s"的內容轉換成"json_obj"


## 3. 提供使用者查詢資料
# 讓使用者輸入內容
user_input = input( '高雄市區監視器分佈位置查詢(請輸入路名): ' )

# 如果使用者輸入的字串裡有'路'這個字，把它取代變成''
user_input = user_input.replace( '路', '' )


## 4. 利用迴圈查詢資料，並將結果輸出
# 標明輸出結果的意義，讓版面整齊排列
print( '行政區\t測照方向\t測照地點' )
print( '=' * 50 )

# 利用迴圈寫出查詢
for obj in json_obj:
	if user_input in obj[ '測照地點' ]:
			print( '%s\t%s\t\t%s' % (obj[ '行政區' ], obj[ '測照方向' ], obj[ '測照地點' ]) )
