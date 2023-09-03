import requests
header={"Cookie":"security=low;PHPSESSID=e2f43ab2911ea4d177541dc8380f591d;w"}
url="http://***.***.*.*"
file=open("fuzzing.txt", "r")
contents=file.read()
file.close()
for i in contents.splitlines():
    print(i)
    url_request=url+str(i)
    result=requests.get(url=url_request, headers=header)
    print("Dizin veya dosya"+ i)
    print("Status Code:", result.status_code)