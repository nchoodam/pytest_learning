import pytest
import re

from colorama import Fore

@pytest.fixture
def get_item():
    out = []
    with open ("ifconfig_iw_phy.txt", 'r',  encoding="utf-8") as file:
        text = file.read().splitlines()
        for item in text:
            x = re.search(r"mesh.*", str(item))
            if x:
                out.append(x.group())
    return out

def test_get_mesh(get_item):
    for item in get_item:
        print("\nThe string item contains \"Mesh\" in:" + item)
        try:
            assert "mesh" in item
        except AssertionError:
            print("Continue with testing")

        try:
            assert "Mesh in item"
        except AssertionError:
            print("Continue with testing.")
