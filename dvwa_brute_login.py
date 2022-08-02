from requests import *

parameters = {'username':'Admin', 'password':'password', 'Login':'Login'}

cookie = {'security':'high', 'security':'low', 'PHPSESSID':'insert_cookie_here'}
header = {'Referer':'http://metasploitable/dvwa/brute'}
r = get("http://metasploitable/dvwa/vulnerabilities/brute/",
params = parameters,
cookies = cookie,
allow_redirects = False,
)

print(r.status_code)
print(r.text) #grep the output to check if it's right
