#複数の条件があるSHA512のハック

import crypt

num = "0123456789"#使用する数列
a = "abcdefghijklmnopqrstuvwxyz"#使用するアルファベット小文字
A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"#使用するアルファベット大文字
kigou = "!"#使用する記号

pas = input()#判明しているハッシュ値を入力

res1 = "P"#１桁目はP

for i in range(len(num)):
	res2 = num[i]#２桁目は数字
	for j in range(len(a)):
		res3 = a[j]#３桁目はアルファベット小文字
		for t in range(len(a)):
			res4 = a[t]#4桁目はアルファベット小文字
			all_key = num + a + A + kigou #すべての文字を含んだ変数を定義
			for u in range(len(all_key)):
				res5 = all_key[u] #５桁目はすべての文字
				for s in range(len(all_key)):
					res6 = all_key[s]#６桁目はすべての文字
					#６桁目、７桁目はどちらかがk
					if res6 != "k":
						res7 = "k"
						A_kigou = A + kigou #アルファベット大文字と記号の文字列
						#パスワードのどこかに！が入る
						if (res1+res2+res3+res4+res5+res6+res7) not in "!": 
							res8 = "!"
							total = res1 + res2 + res3 + res4 + res5 + res6 + res7 + res8
							if crypt.crypt(pas, crypt.METHOD_SHA512) == crypt.crypt(total, crypt.METHOD_SHA512):
								print("yes")
								break
						else:
							for y in range(len(A_kigou)):
								res8 = A_kigou[y]
								total = res1 + res2 + res3 + res4 + res5 + res6 + res7 + res8
								print(total)
								if crypt.crypt(pas, crypt.METHOD_SHA512) == crypt.crypt(total, crypt.METHOD_SHA512):
									print("yes")
									break
					else:
						for x in range(len(all_key)):
							res7 = all_key[x]
							A_kigou = A + kigou
						if (res1+res2+res3+res4+res5+res6+res7) not in "!":
							res8 = "!"
							total = res1 + res2 + res3 + res4 + res5 + res6 + res7 + res8
							print(total)
							if crypt.crypt(pas, crypt.METHOD_SHA512) == crypt.crypt(total, crypt.METHOD_SHA512):
								print("yes")
								break
						else:
							for y in range(len(A_kigou)):
								res8 = A_kigou[y]
								total = res1 + res2 + res3 + res4 + res5 + res6 + res7 + res8
								print(total)
								if crypt.crypt(pas, crypt.METHOD_SHA512) == crypt.crypt(total, crypt.METHOD_SHA512):
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
