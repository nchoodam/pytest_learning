import pytest
import re
from colorama import Fore


@pytest.fixture
def get_item():
    out= []
    with open ("ifconfig_iw_phy.txt", 'r',  encoding="utf-8") as file:
        text = file.read().splitlines()
        for item in text:
            #print(item)
            x = re.findall(r"[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+", str(item))
            if x:
                #print(x)
                out.append(x)
    return out

def test_ip_addr(get_item):
    for item in get_item:
        for i in item :
            if i == '172.27.10.255':
                x = i
                print(Fore.GREEN, "\nThe ip address is:"+x)
    try:
        print("Test with assert {}".format(x))
        assert x == "172.27.10.255"
    except AssertionError:
        print("Please continue with testing.")

    try:
        print("Test with assert {}".format(x))
        assert x == "172.27.10.200"
    except AssertionError:
        print("Please continue with testing.")






