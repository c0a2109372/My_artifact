import crypt
import datetime

now1 = datetime.datetime.now()
pas = input() #テスト用パスワードを入力
pas = crypt.crypt(pas, '$1$j9Tmphtq$') #パスワードをハッシュ化

#パスワードの辞書の読み込み
f = open('passphrase.txt', 'r') #passphrase.txt:単語を羅列した辞書
dictpasswds = f.readlines()
f.close()

#passphrase.txt内の４単語の組み合わせを試行
for i in range(len(dictpasswds)):
	for j in range(len(dictpasswds)):
		for s in range(len(dictpasswds)):
			for t in range(len(dictpasswds)):
				d = dictpasswds[i].rstrip('\n') + dictpasswds[j].rstrip('\n') + dictpasswds[s].rstrip('\n') + dictpasswds[t].rstrip('\n')
				print(d.rstrip('\n'))
				if pas == crypt.crypt(d, '$1$j9Tmphtq$'):
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

#ハックに掛かる時間を表示
now2 = datetime.datetime.now()
print(now1)
print(now2)
