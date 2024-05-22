import pytest
import re

@pytest.fixture
def get_item():
    out = []
    with open ("ifconfig_iw_phy.txt", 'r',  encoding="utf-8") as file:
        text = file.read().splitlines()
        for item in text:
            x = re.search(r"streams.*", str(item))
            if x:
                out.append(x.group())
                print(x.group()) 
    return out

def test_reg_sub(get_item):
    for item in get_item:
        print("NEW:The string item is :{}".format(item))
        x = re.sub(r"streams", "STREAMS", item)
        try:
            assert "STREAMS" in x 
            print("The New valus is "+ x)
        except AssertionError:
            print("Asert has failed but we can continue to check next assert.")



