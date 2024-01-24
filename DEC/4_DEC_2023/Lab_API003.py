import requests
# Here we are giving dynamic Id, url,

def main():
    id = "94"  # if you change the id which is not exist then it will throw an error
    url = "https://restful-booker.herokuapp.com/booking/"
    full_url = url +id
    print(full_url)
    response_body = requests.get(full_url)
    assert response_body.status_code == 200  # if status code is not equal to 200, it will throw an error else no error


if __name__ == "__main__":# here if name is equal to main then run main() which is above main () which included our code.
    main()
#output =
'''https://restful-booker.herokuapp.com/booking/1623

Process finished with exit code 0'''
