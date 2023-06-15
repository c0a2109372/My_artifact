import crypt
import datetime

passchar_list = 'abcdefghijklmnopqrstuvwxyz0123456789' #使用する文字列
pas = input()#テスト用パスワードを入力
pas = crypt.crypt(pas, crypt.METHOD_CRYPT)#パスワードをMETHOD_CRYPTアルゴリズムでハッシュ化

#パスワードを６桁と仮定してハック
for a in range(len(passchar_list)):
	for b in range(len(passchar_list)):
		for c in range(len(passchar_list)):
			for d in range(len(passchar_list)):
				for e in range(len(passchar_list)):
					print(datetime.datetime.now())
					for f in range(len(passchar_list)):	
						total = passchar_list[a] + passchar_list[b] + passchar_list[c] + passchar_list[d] + passchar_list[e] + passchar_list[f]
						total = crypt.crypt(total,crypt.METHOD_CRYPT)
						#print(total)
						if total == pas:
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
		else:
			continue
		break
	else:
		continue
	break
