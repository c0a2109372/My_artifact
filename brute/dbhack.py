import crypt
import datetime

passchar_list = 'abcdefghijklmnopqrstuvwxyz0123456789' #パスワードに使用される文字列
pas = "$2y$10$ecRmAWY4n/jLa0tTzIaG7.SMhb1TfdROy3nXeG5aVZorUX1n6/WHO" #判明しているハッシュ値

#パスワード8桁を総当たりでハック
for a in range(len(passchar_list)):#左から１桁目
	for b in range(len(passchar_list)):#2桁目
		for c in range(len(passchar_list)):#3桁目
			for d in range(len(passchar_list)):#4桁目
				for e in range(len(passchar_list)):#5桁目
					for f in range(len(passchar_list)):#6桁目
						for g in range(len(passchar_list)):#7桁目
							print(datetime.datetime.now())#一桁目が回りきるまでの時間を表示
							for h in range(len(passchar_list)):#8桁目
           
								#passchar_listの文字列をスライスして全パターンを試行
								#変数totalにすべての桁を結合し代入
								total = passchar_list[a] + passchar_list[b] + passchar_list[c] + passchar_list[d] + passchar_list[e] + passchar_list[f] + passchar_list[g] + passchar_list[h]
								
        						#totalにcrypt()を使用しハッシュ化
								total = crypt.crypt(total,"$2y$10$ecRmAWY4n/jLa0tTzIaG7.")
        
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
		else:
			continue
		break
	else:
		continue
	break
