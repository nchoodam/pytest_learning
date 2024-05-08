import pytest
import re
from colorama import Fore

@pytest.fixture
def get_item():
    out = []
    with open ("ifconfig_iw_phy.txt", 'r',  encoding="utf-8") as file:
        text =file.read().splitlines()
        for item in text:
            x = re.search(r"\[81\]", str(item))
            if x:
                out.append(x.group())
    return out

####################################################################################################################################################

def test_bracket(get_item):
    for item in get_item:
        x = item
        if x == "[81]":
            print(Fore.BLUE,"\nThe value is : "+ x)
    assert x == "[81]"
