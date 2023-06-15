import crypt
import datetime

passchar_list = 'aps01' #パスワードに使用される文字列
pas = "$2y$10$FH0AxXnSYlqccd3m.IezOeXaU9ZcG6Spq1mOxD31oTna.janNP.K." #判明しているハッシュ値

#6桁のパスワードを総当たりでハック
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
      
						#totalにcrypt()を使用しハッシュ化
						total = crypt.crypt(total,"$2y$10$FH0AxXnSYlqccd3m.IezOe")
						#表示する場合としない場合での実行時間の変化を確認
						#print(total)
      
						#totalとpas(判明しているハッシュ値)が同一であればループを終了
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
