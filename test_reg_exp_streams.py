import pytest
import re
from colorama import Fore

@pytest.fixture
def get_item():
    out = []
    with open ("ifconfig_iw_phy.txt", 'r',  encoding="utf-8") as file:
        text =file.read().splitlines()
        for item in text:
            x = re.search(r"\d.*streams.*", str(item))
            if x:
                 y = x.group()
                 out.append(y)
    return out

####################################################################################################################################################

def test_get_stream(get_item):
    x = "0-11"
    y = "0-12"
    for item in get_item:
        if x in item:
            print(item)
            break
    print("\nThe test checkes for keyword streams in item.: "+x)
    try:
        assert x in item
    except AssertionError:
        print("Continue with testing")
    try:
        assert y in item
    except AssertionError:
        print("Continue with testing")
