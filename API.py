import requests

url = "https://accounts.google.com/_/signup/usernameavailability?hl=en&TL=AJvNCbYx0rGXgaUtKS-Xn3Vdu_VDSN_Z7A7aAHVeaX4NM8RPonT0sIVezE-1FTGb"
payload = {
    "continue": "https%3A%2F%2Fmail.google.com%2Fmail%2F",
    "flowEntry": "SignUp",
    "ltmpl": "default",
    "service": "mail",
    "f.req": '["TL:AJvNCbYx0rGXgaUtKS-Xn3Vdu_VDSN_Z7A7aAHVeaX4NM8RPonT0sIVezE-1FTGb","RAHULK",0,0,1]',
    "azt": "AFoagUV1gBrFst3iY6laMd1vGk095ckGnA:1689616960904",
    "cookiesDisabled": "false",
    "deviceinfo": "[null,null,null,[],null,\"US\",null,null,null,\"GlifWebSignIn\",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[],null,null,null,null,[]],null,null,null,null,0,null,0,1,\"\",null,null,1,0]",
    "gmscoreversion": "undefined",
    "flowName": "GlifWebSignIn",
    "checkConnection": "youtube:250:1",
    "checkedDomains": "youtube",
    "pstMsg": "1"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2F&ltmpl=default&gmb=exp&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp&TL=AJvNCbYx0rGXgaUtKS-Xn3Vdu_VDSN_Z7A7aAHVeaX4NM8RPonT0sIVezE-1FTGb",
    "X-Same-Domain": "1",
    "Google-Accounts-XSRF": "1",
    "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
    "Origin": "https://accounts.google.com",
    "Alt-Used": "accounts.google.com",
    "Connection": "keep-alive"
}

response = requests.post(url, headers=headers, data=payload)
print(response.text)