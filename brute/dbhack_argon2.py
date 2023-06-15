import crypt
#アルゴリズムにargon2を使用できるようにする
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
import datetime

passchar_list = 'aps01'#パスワードに使用される文字列
ph = PasswordHasher()
target = "$argon2id$v=19$m=65536,t=4,p=1$dVo1THZ4WTU0NExTc2UvLg$lfpmKtz7Xoocyp5yi+gUE9V+6gzUsuYWAgho2tEQ53U"#判明しているハッシュ値

#パスワード6桁を総当たりでハック
for a in range(len(passchar_list)):
	for b in range(len(passchar_list)):
		for c in range(len(passchar_list)):
			for d in range(len(passchar_list)):
				for e in range(len(passchar_list)):
					print(datetime.datetime.now())
					for f in range(len(passchar_list)):
						#passchar_listの文字列をスライスして全パターンを試行
						#変数totalにすべての桁を結合し代入
						total = passchar_list[a] + passchar_list[b] + passchar_list[c] + passchar_list[d] + passchar_list[e] + passchar_list[f]
      
						flag = False#変数flagをfalseに初期化
						try:
          				#verify()は第一引数をハッシュ化した値と第二引数の値が等しい場合はTrueを返す。一致しない場合はエラーが出る
							flag = ph.verify(target, total)
						except VerifyMismatchError:#値が一致しない場合はpass
							pass
						#print(total)
						#print(flag)
						if flag:#値一致時はflagにはTrueが格納される
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
