import requests # which help to make Http request

def main():
    response_body = requests.get("https://restful-booker.herokuapp.com/booking/94")# here we not using main fuction as it is copied in Lab_API001.py
    print(response_body.status_code)
    #  print(response_body.text)
    #  print(response_body.headers)
    #  print(response_body.json())
    if response_body.status_code == 200:
        print("TC01 is successful")
    else:
        print("TC01 is not successful")

if __name__ == "__main__": # here we are saying to python that if name is equal to main then run this function.
        print(main())

import requests

'''def main ():
            #GET test case 01
            response_body = requests.get("https://restful-booker.herokuapp.com/booking/4364")
            #print(response_body.text)
            #print(response_body.status_code)
            #print(response_body.json())
            if response_body.status_code == 200:
                print("Testcase#1 - GET request is successful")
            else:
                print("Testcase#1 - GET request is not successful")

if __name__ == "__main__":
    main()'''

"""Output: Testcase#1 - GET request is not successful

Process finished with exit code 0"""

#
'''  Here's a breakdown of the code:

import requests: This line imports the requests module, which is necessary for making HTTP requests.

response_body = requests.get("https://restful-booker.herokuapp.com/booking/633"): This line sends an HTTP GET request to the specified URL, and the response is stored in the response_body variable.

print(response_body.status_code): This line prints the HTTP status code returned by the server. In this case, it checks if the status code is 200.

The subsequent lines are commented out using #. These lines show additional information that you can print from the response, such as the response text, headers, and JSON content. Depending on your needs, you can uncomment and use these lines for more detailed information.

The code then checks if the status code is equal to 200 and prints a corresponding message. If the status code is 200, it prints "TC01 is successful"; otherwise, it prints "TC01 is not successful."

Regarding the commented-out code below, it seems to be an alternate version of the main function with a different URL ("https://restful-booker.herokuapp.com/booking/612"). It is another test case with a different booking ID. You can choose to use this version of the code if you want to test against a different resource.

It's worth noting that the second version of the code is indented differently, which may be a formatting issue. Make sure the indentation is consistent throughout your code.'''