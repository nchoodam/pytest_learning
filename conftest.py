import pytest 

@pytest.fixture(autouse= True)
def init_config():
    print("Perform: initial configuration.")
    print("Perform: 1_Open_browser")
    print("Perform: 1_open_udl")
    print("Perform: 1_input_credentials")
    print("Perform: tasks and complete")
    yield
    print("\nRemove auto configuration.") 
    print("Remove: 1_Complete and close tasks")
    print("Remove: 1_close the url")
    print("Remove: 1_close the browser")


