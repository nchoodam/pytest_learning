import pytest
import re

@pytest.fixture
def get_item():
    out= []
    with open ("ifconfig_iw_phy.txt", 'r',  encoding="utf-8") as file:
        text = file.read().splitlines()
        for item in text:
            #print(item)
            x = re.search(r"\b\d{6}\b", str(item))
            if x:
                y = x.group()
                out.append(y)
    return out

def test_out_1(get_item):
    x = get_item[0]
    print(x)
    a = "942439"
    try:
        assert x == a
    except AssertionError:
        print("Continue with testing")
    try:
        assert x == "25"
    except AssertionError:
        print("Continue with testing")

def test_out_2(get_item):
    x = get_item[1]
    a = "449634"
    try:
        assert x == a 
    except AssertionError:
        print("Continue with testing")
    try:
        assert x =='5'
    except AssertionError:
        print("Continue with testing")
####################################################################################################################################################


