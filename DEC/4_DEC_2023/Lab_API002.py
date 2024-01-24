import requests

response_body = requests.get("https://restful-booker.herokuapp.com/booking/94") #
print(response_body.json())
print(response_body.status_code)
print(response_body.headers)

# out put below

"""{'firstname': 'Rakesh', 'lastname': 'Yadav', 'totalprice': 195, 'depositpaid': True, 'bookingdates': {'checkin': '2024-01-11', 'checkout': '2024-01-01'}, 'additionalneeds': 'Breakfast'}
200
{'Server': 'Cowboy', 'Report-To': '{"group":"heroku-nel","max_age":3600,"endpoints":[{"url":"https://nel.heroku.com/reports?ts=1705196470&sid=c46efe9b-d3d2-4a0c-8c76-bfafa16c5add&s=55Q004Kq65mXaawkBQ%2FettTnudYI8kXQqYBeElUkQ0Y%3D"}]}', 'Reporting-Endpoints': 'heroku-nel=https://nel.heroku.com/reports?ts=1705196470&sid=c46efe9b-d3d2-4a0c-8c76-bfafa16c5add&s=55Q004Kq65mXaawkBQ%2FettTnudYI8kXQqYBeElUkQ0Y%3D', 'Nel': '{"report_to":"heroku-nel","max_age":3600,"success_fraction":0.005,"failure_fraction":0.05,"response_headers":["Via"]}', 'Connection': 'keep-alive', 'X-Powered-By': 'Express', 'Content-Type': 'application/json; charset=utf-8', 'Content-Length': '171', 'Etag': 'W/"ab-oY5qk/pskXEbzMhHTCplz5u5fOU"', 'Date': 'Sun, 14 Jan 2024 01:41:10 GMT', 'Via': '1.1 vegur'}

Process finished with exit code 0"""