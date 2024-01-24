import requests
# class link = https://courses.thetestingacademy.com/courses/job-ready-python-automation-blueprint-selenium-api-automation-1x/contents/656d7bee3a25d
"""{
    "firstname": "Josh",
    "lastname": "Allen",
    "totalprice": 111,
    "depositpaid": true,
    "bookingdates": {
        "checkin": "2018-01-01",
        "checkout": "2019-01-01"
    },
    "additionalneeds": "superb owls"
}"""
# how to verify the API given in postman.

def main():
    id = "94"  # if you change the id which is not exist then it will throw an error
    url = "https://restful-booker.herokuapp.com/booking/"
    full_url = url + id
    print(full_url)
    response_body = requests.get(full_url)
    assert response_body.status_code == 200  # if status code is not equal to 200, it will throw an error else no error
    # first convert data into Json like

    data = response_body.json() #to check what type of data just enter 'print(type(data))'

    #(verfication of keys)
    # now add n number of assertions to validate all keys and values
    #assert 'firstname' in data, "enter what message should display when you get error" # here we are checkin first name is present in data
    # if we dont have any data in first name it will throw error with given message from us
    #assert 'lastname' in data, "enter what message should display when you get error"  # this is to validate the first and last name is present
    # if we dont have any data in first name it will throw error with given message from us

    #(verfication of Data)
    # to validate values
    # to find the key use this [] if you see { in JSON.
    assert data["firstname"] == "Josh", "enter what message should display when you get error in firstname"
    assert data["lastname"] == "Allen", "enter what message should display when you get error in lastname"
    assert data["bookingdates"]["checkin"] == "2018-01-01", "enter what message should display when you get error in check in date"


if __name__ == "__main__":
    main()
    # output
'''https://restful-booker.herokuapp.com/booking/94

Process finished with exit code 0'''

