---
# ufw
```
$ sudo ufw status
```
---
# ufw
```
$ sudo ufw enable or disable
```
---
# ufw
```
$ sudo ufw default allow|deny|reject [incoming|outgoing]
```
---
# ufw allow
```
# ufw allow service|port/protocol
$ sudo ufw allow http
```
---
# ufw deny
```
# ufw deny service|port/protocol
$ sudo ufw deny ftp
```
---
# ufw delete
```
# delete a rule
$ ufw delete deny ftp 
```
---
# ufw  allow 
```
$ ufw allow 3030/tcp
```
---
# ufw allow
```
$ ufw allow from 192.168.0.12 to any port http
```
---
# nmap
```
$ sudo apt-get install nmap
```
---
# nmap
  - -sS : TCP SYN scan
  - -sT : TCP connection scan
  - -sP : ping scan
  - -sU : UDP scan
  - -sO : IP protocol scan
  - -O : OS
  - -v : print scan result thoroughly
  - -p : scan specified port
  - -F : fast mode
---
# nmap
```
$ nmap localhost
```
---
# nmap 
```
$ sudo nmap -O 192.168.0.11
```
---
# nmap
```
# TCP scan
$ sudo nmap -sT 192.168.0.11
```
---
# nmap 
```
$ sudo nmap -sT -O -v 192.168.0.0/24
```
