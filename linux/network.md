# /etc/services
```
$ cat /etc/services
```
---
# hostname
```
$ hostname
```
---
# ifconfig
```
$ ifconfig 
wlp3s0: mtu 1500 inet(ip address) netmask
inet6(IPv6) ether(MAC address)
RX(packets, bytes), TX(packets, bytes)
```
---
# route
```
# handle routing table
$ route
Destination: dest network
Gateway: gateway address 0.0.0.0 - default
Flag: U-UP
      G-gateway
      H-host

```
---
# rounte add network
```
route add -net 192.168.1.0 netmask 255.255.255.0 dev eth0
```
---
# route add del network
```
route del -net 192.168.1.0 netmask 255.255.255.0
```
---
# route add host
```
route add -host 192.168.1.2 dev eh0
```
---
# route del host
```
route del -host 192.168.0.2
```
---
# route add default gw
```
route add default gw 192.168.1.1
```
---
# route del default gw
```
route del default gw 192.168.1.1
```
---
# nslookup
```
$ nslookup google.com
```
---
# ping
```
ping www.google.com
```
---
# traceroute
```
$ traceroute google.com
```
---
# whois
```
$ whois 58.229.119.29
```
---
# netstat
  - -a : all sockets' info
  - -r : routing info
  - -n : ip address, NOT hostname
  - -i : all interface info
  - -s : summary statistics for each protocol
  - -p : process name and PID 
---
# netstat -a
```
# service port LISTEN
$ netstat -a | grep LISTEN
```
---
# netstat -r
```
# print routing table
$ netstat -r
```
---
# netstat -p
```
# print process name and PID 
$ netstat -p | less
```
---
# netstat -s
```
# print statistics for protocol
$ netstat -s
```
---
# arp
```
# mac address and biding ip address 
$ arp 192.168.0.1
```
---
# tcpdump
```
$ tcpdump
```
---
# tcpdump
```
# close after num of packets
$ tcpdump -c <num>
```
---
# tcpdump
```
# select interface
$ tcpdump -i <iface>
```
---
# tcpdump
```
# write
$ tcpdump -w dfile
```
---
# tcpdump
```
# read
$ tcpdump -r dfile
```
---
# tcpdump
```
$ tcpdump host 192.168.0.12
```
---
# tcpdump
```
$ tcpdump tcp port 23
```
---
# tcpdump
```
$ tcpdump -Xqr dfile
```

