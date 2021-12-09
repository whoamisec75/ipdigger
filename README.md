<img src="https://github.com/whoamisec75/ipdigger/blob/main/static/IMG_20211209_182937.jpg"/>
<p align="center"><b><i>Takes a file of hosts or domains and outputs the IP address of each host/domain in the file.</b></i></p> 

## Installation

```
$ git clone https://github.com/whoamisec75/ipdigger.git
$ cd ipdigger
$ sudo python3 setup.py install
$ ipdigger -h
```

## Usage:

For example, I have subdomains list:

```
xyz.com
main.xyz.com
hack.xyz.com
support.xyz.com
hi.xyz.com
sql.xyz.com
rce.xyz.com
```

So if I want to find IP addresses of all these domains:

```
$ ipdigger subdomains.txt -ih -c 20 --output subdomains_ip.txt
 _       _ _                   
|_|___ _| |_|___ ___ ___ ___   
| | . | . | | . | . | -_|  _|  
|_|  _|___|_|_  |_  |___|_|    
  |_|       |___|___|          
                        @whoamisec
                        
[✓] xyz.com ---> 204.xx.xxx.xxx
[✓] main.xyz.com ---> 40.xx.x.xx
[✓] hack.xyz.com ---> 44.xxx.xx.x
[✓] support.xyz.com ---> 104.xx.xx.xx
...
```
