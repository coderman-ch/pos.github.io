import requests
import sys
args=sys.argv
if len(args) < 3:
    print("This is a cmd tool.It needs ARGS.")
    sys.exit(1)
url=sys.argv[1]
name=sys.argv[2]
#url = 'http://static.openjudge.cn/images/default_logo_large.png'
try:
    response = requests.get(url)
except:
    print("Faild")
else:
    if response.status_code == 200:
        with open(name, 'wb') as file:
            file.write(response.content)
        print('Succeed')
    else:
        print('Faild')
