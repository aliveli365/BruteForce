import requests
import subprocess


subprocess.call('clear', shell=True)
header =  {"Cookies" : "security= low; PHPSESSID:f6612757495af90e878e674d2e34947e;"}
url = input("Url giriniz:")

dosya = open("fuzz.txt", "r")
icerik = dosya.read()
dosya.close

for i in icerik.splitlines():
    url_istek = url+str(i)
    sonuc = requests.get(url=url_istek,headers=header)
    code = sonuc.status_code
    print(" {}{} status:{} \n".format(url,i,code))
    print("=="*20)
