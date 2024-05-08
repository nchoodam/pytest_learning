import pytest
import re
from colorama import Fore

@pytest.fixture
def get_item():
    out = []
    with open ("ifconfig_iw_phy.txt", 'r',  encoding="utf-8") as file:
        text =file.read().splitlines()
        for item in text:
            x = re.findall(r"\dx\d+", str(item))
            out.append(x)
    return out

def test_get_item(get_item):
    for i in get_item:
        for item in i:
            if item == "0x039071":
                x = item
    print(Fore.YELLOW+"\nThe value is 0x039071")
    assert x == "0x039071"

