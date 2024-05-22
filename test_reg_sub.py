import pytest
import re

@pytest.fixture
def get_item():
    out = []
    with open ("ifconfig_iw_phy.txt", 'r',  encoding="utf-8") as file:
        text = file.read().splitlines()
        for item in text:
            x = re.search(r"mesh.*", str(item))
            if x:
                out.append(x.group())
                print(x.group()) 
    return out

def test_reg_sub(get_item):
    for item in get_item:
        print("NEW:The string item is :{}".format(item))
        x = re.sub(r"mesh", "MESH", item)
        try:
            assert "MESH" in x 
            print(x)
        except AssertionError:
            print("If assert fails but we can continue to check next assert.")



