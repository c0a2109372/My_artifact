import crypt
import datetime

now1 = datetime.datetime.now()
pas = input() #テスト用パスワードを入力
pas_cr = crypt.crypt(pas, '$1$j9Tmphtq$') #パスワードをハッシュ化
num = "0123456789" #使用する数列

#パスワードの辞書の読み込み
f = open('dictpasswd.txt', 'r')
dictpasswds = f.readlines()
f.close()

#パスワード辞書内のパスワードと３桁の数値の組み合わせを試行
for i in range(len(dictpasswds)):
	for a in range(len(num)):
		for b in range(len(num)):
			print(datetime.datetime.now())
			for c in range(len(num)):
				pas_num = dictpasswds[i].rstrip('\n') + num[a] + num[b] + num[c]
				#print(pas_num)
				if pas_cr == crypt.crypt(pas_num, '$1$j9Tmphtq$'):
					print("yes")
					break
			else:
				continue
			break
		else:
			continue
		break
	else:
		continue
	break

now2 = datetime.datetime.now()
print(now1)
print(now2)
