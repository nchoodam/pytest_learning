import pytest 
import re

def test_1():
    text = "My name is Nandakumar, My experinec is 18 years. I work at Thinkpalm Technologieslocated at Kochi"
    x = re.search("Th.*m", text)
    x = x.group()
    if x:
        print("The company is {}".format(x))
    else:
        print("Nothing found")

    y = re.search(r"^My", text)
    if y:
        print("Found")
    else: 
        print("Not found")
    y = y.group()
    assert x == "Thinkpalm" 
    assert y == "My"

def test_2():
    ifconfig = """
    enp3s0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.27.10.77  netmask 255.255.255.0  broadcast 172.27.10.255
        inet6 fe80::e641:ce20:9e09:dfb8  prefixlen 64  scopeid 0x20<link>
        ether 1c:83:41:05:2e:da  txqueuelen 1000  (Ethernet)
        RX packets 561962  bytes 747893686 (747.8 MB)
        RX errors 0  dropped 2796  overruns 0  frame 0
        TX packets 264508  bytes 35076185 (35.0 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 5077  bytes 653488 (653.4 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 5077  bytes 653488 (653.4 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

wlp1s0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        ether f4:7b:09:f8:e4:c2  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0"""

    ip = re.findall(r"[1-9]+\.[1-9]+\.[1-9]+\.[1-9]", ifconfig)
    print(ip)


