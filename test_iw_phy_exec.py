import pytest
import re
import subprocess
from colorama import Fore

@pytest.fixture
def get_item():
    out = []
    #command = "iw phy"
    result = subprocess.run(['iw', 'phy'], capture_output=True, text= True)
    text = result.stdout
    text_list = text.split("\n")
    #print(text_list)
    for item in text_list:
        x = re.findall(r"radar", str(item))
        if x:
            print(x)
            out.append(x)
    print(out)
    return out

def test_get_item(get_item):
    for item in get_item:
        for i in item:
            if i:
                x = i
    try:
        print("Found list item is {}".format(i)) 
        assert i == 'Radar'
    except AssertionError:
        print("Found list item is {}".format(i))
        assert i =="radar"


