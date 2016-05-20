# -*- coding:utf-8 -*-  
'''
# 程式流程：
1.先開啟並讀取".txt"檔裡面的內容。
2.將程式內各行的內容進行讀取，並使用變數儲存。
	(1)"奇數行"：檔案名稱
	(2)"偶數行"：網址
3.透過變數裡的內容下載網頁，並以對應的名稱儲存。
'''

import urllib					# 引入網頁下載所需的套件
linenum = 0						# 設定行號
file = open('xxx.txt', 'r')		# 設定欲讀取的檔案


for line in file.readlines():
	linenum += 1				
	
	if (linenum % 2) == 1:		# 若為"奇數行"，該行為"檔案名稱"
		line = line.strip('\n')	# 讀取該行內容後，去除最後面的換行字元('\n')
		filename = line			# 將"檔案名稱"存入變數內
		
				
	elif (linenum % 2) == 0:	# 若為"偶數行"，該行為"網址"
		file_url = line			# 將"網址"存入變數內
		
		urllib.urlretrieve( file_url, filename + ".html" )	# 下載網頁
		print ("Try to download：" + filename + "...done！")	# 在命令列中顯示訊息

file.close()