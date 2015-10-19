import time
from socket import *


#-------- IP、Port --------
# The Target IP:203.64.91.58，Port:8888/8889

TARGET = ('203.64.91.58', 8888)
sock = socket( AF_INET, SOCK_STREAM )
sock.connect(TARGET)	# 與目標電腦建立連線
#--------------------------------------

#-------- 猜數字的 Function--------
min_num = 1
max_num = 1024
guess_num = 512

def guess_number(recv):
	global min_num
	global max_num
	global guess_num
	recv_b = recv.decode('utf-8')
	
	print(recv_b)

	if 'big' in recv_b:	# 如果猜太大
		max_num = guess_num
		guess_num = int((min_num + max_num)/2)

	if 'small' in recv_b:	# 如果猜太小
		min_num = guess_num
		guess_num = int((min_num + max_num)/2)

	if 'Flag' in recv_b:	# 如果猜中了
		pass

	return guess_num
#----------- END ------------

#-------- 處理並過濾訊息的 Function --------
def bytes_to_str(recv):
	recv_b = recv.decode('utf-8')		# 將"bytes"解碼成"str"

	recv_b = recv_b.replace('\r', '')	# 過濾字串"\r"
	recv_b = recv_b.replace('\n', '')	# 過濾字串"\n"

	recv_b = bytes(str(recv_b).encode('utf-8'))	# 將"str"還原成"bytes"
	return recv_b	# 回傳處理後的訊息
#----------- END ------------

#-------- main_Function --------
def main_function(recv):

	time.sleep(0.5)
	tmp = str(guess_number(recv))	
	print(tmp)
	sock.send(bytes(str(tmp + '\n').encode('utf-8')))
	
	return ''
#----------- END ------------

if __name__ == '__main__':
	# STEP_1 : 先接收並過濾訊息
	recv = sock.recv(1024)
	recv = bytes_to_str(recv)
	print (recv)


	# STEP_2 : 送出 Enter 後，再重新接收並過濾訊息
	sock.send(bytes(str('\n').encode('utf-8')))
	recv = sock.recv(1024)
	recv = bytes_to_str(recv)


	# STEP_3 : 開始猜數字
	for i in range(10):		
		print(main_function(recv))
		recv = sock.recv(1024)
	
	print(recv)
#----------- END ------------
	sock.close()	# 與目標電腦關閉連線