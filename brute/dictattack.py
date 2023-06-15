import crypt
import datetime

now1 = datetime.datetime.now()
pas = input() #テスト用パスワードを入力
pas = crypt.crypt(pas, '$1$j9Tmphtq$') #パスワードをハッシュ化

#パスワードの辞書の読み込み
f = open('dictpasswd.txt', 'r')
dictpasswds = f.readlines()
f.close()

#辞書内のパスワードをハッシュ化し総当たりで試行
for i in range(len(dictpasswds)):
	print(dictpasswds[i])
	if pas == crypt.crypt(dictpasswds[i].rstrip('\n'), '$1$j9Tmphtq$'):
		print("yes")
		break

#ハックに掛かる時間を表示
now2 = datetime.datetime.now()
print(now1)
print(now2)
