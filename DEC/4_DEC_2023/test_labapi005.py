import requests
import pytest
def test_sample():  # Testcase 1
    assert 4 ==4

def test_sample2():  # Testcase 2
    assert 6 == 5

def test_gettrequest():  # Testcase 3
    id = "94"  # if you change the id which is not exist then it will throw an error
    url = "https://restful-booker.herokuapp.com/booking/"
    full_url = url + id
    print(full_url)
    response_body = requests.get(full_url)
    assert response_body.status_code == 200
    data = response_body.json() #to check what type of data just enter 'print(type(data))'

    assert data["firstname"] == "Jane", "enter what message should display when you get error in firstname"
    assert data["lastname"] == "Doe", "enter what message should display when you get error in lastname"
    assert data["bookingdates"]["checkin"] == "2018-01-01", "enter what message should display when you get error in check in date"

'''# you can either run from the side arrow or from terminal like open terminal below and make sure you are correct directory
# In terminal type pytest followed by the path of the file name of where we written the testcases."pytest DEC/4_DEC_2023/test_labapi005.py"'''
# #########important to install the pytest report = pip install pytest-html allure-pytest#########################################
# to run report in terminal type =pytest DEC/4_DEC_2023/test_labapi005.py --alluredir=reports and hit enter and report will be created in files side which is doesn't look so good
# we can get good allure report just type= "allure serve reports" it will open new link of good report