import pytest 

@pytest.fixture(autouse= True)
def init_config():
    print("1_Open_browser")
    print("1_open_udl")
    print("1_input_credentials")
    print("Performa tasks and complete")
    yield
    print("1_Complete and close tasks")
    print("1_close the url")
    print("1_close the browser")


