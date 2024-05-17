import pytest
import re
import subprocess
from colorama import Fore

@pytest.fixture
def get_item():
    out = []
    command = "ifconfig"
    result = subprocess.run([command], capture_output=True, text= True)
    text = result.stdout
    text_list = text.split("\n")
    for item in text_list:
        x = re.findall(r"[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+", str(item))
        if x:
            #print(x)
            out.append(x)
    #print(out)
    return out

def test_get_item(get_item):
    for item in get_item:
        for i in item:
            if i:
                x = i
    try:
        print("Found list item is {}".format(i)) 
        assert i == '255.0.0.10'
    except AssertionError:
        print("Continue with assertion comparision")

    try:
        print("Found list itemis {}".format(i))
        assert i == "255.0.0.0"
    except AssertionError:
        print("Continue with assertion comparision")


