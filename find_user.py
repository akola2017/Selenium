#!/usr/bin/python
import paramiko
print('Ala')
polaczenie=paramiko.SSHClient()
type(polaczenie)
polaczenie.set_missing_host_key_policy(paramiko.AutoAddPolicy())
polaczenie.connect("localhost", username='tester01', password="Alamakota!")
a,b,c=polaczenie.exec_command("uname -a")
#b-komunikat o poprawnym wykonaniu, c-komunikat o bledzie
zmienna=b.read()
#print(zmienna)

a,b,c=polaczenie.exec_command("cat /etc/passwd ")
wynik=b.read()
#print(wynik)
lista = wynik.split("\n")
jest=False
drugijest=False
for linia in lista:
    if linia.find("tester01")+1:
        jest=True
        print(linia)

if jest:
    print("jest uzytkownik tester01")
else: print("nie ma")
