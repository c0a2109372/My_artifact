import crypt
import datetime

now1 = datetime.datetime.now()
pas = input() #判明しているハッシュ値を入力

passchar_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#'#使用する文字列

#8桁のパスワードをハック
for a in range(len(passchar_list)):
	for b in range(len(passchar_list)):
		for c in range(len(passchar_list)):
			for d in range(len(passchar_list)):
				for e in range(len(passchar_list)):
					for f in range(len(passchar_list)):
						for g in range(len(passchar_list)):
							now = datetime.datetime.now()
							print(now)
							for h in range(len(passchar_list)):
								#print(passchar_list[a] + passchar_list[b] + passchar_list[c] + passchar_list[d] + passchar_list[e] + passchar_list[f] + passchar_list[g] + passchar_list[h])
								if crypt.crypt(passchar_list[a] + passchar_list[b] + passchar_list[c] + passchar_list[d] + passchar_list[e] + passchar_list[f] + passchar_list[g] + passchar_list[h], '$1$j9Tmphtq$') == pas:
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
				else:
					continue
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
