import requests
import json

logout_url="https://qa-tasks.zolv.health/api/v1/user/logout"

login_url= "https://qa-tasks.zolv.health/api/v1/user/task-login"



login_payload = {
    "loginId": "UserRequest",
    "password": "Smm@1234"
}



# Login :

print("\033[1;34mTESTING LOGIN!\033[0m")
response_login = requests.post(login_url,json=login_payload)
if response_login.status_code == 200:
    response_json = response_login.json()
    # print("Response JSON : ",json.dumps(response_json,indent=4))
    token= response_json.get('token',{}).get('token')
    print(f"\033[92m✅ TEST PASSED...! : Test Case ID - 001 \033[0m")
    headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
                }
else:
    print(f"\033[91m❌ TEST FAILED...! : Test Case ID - 001 : Error - Invalid Credentials \033[0m")




# 17 :logout :  

response_logout = requests.put(logout_url,headers=headers) 
if response_logout.status_code == 200:
    logout_json = response_logout.json()
    # print("Response JSON:", json.dumps(logout_json, indent=4))
    # print(f"Token (Logout): {token}")
    print(f"\033[92m✅ Test Case ID - 012 : Logout                      : TEST PASSED...! \033[0m") # login success so test failed becoz in oms logged with oms in other 3 credentials kds,go,testoms

else:
    # print(f"Logout failed with status code {response_logout.status_code}")
    # print("Response:", response_logout.json())
    print(f"\033[91m❌ Test Case ID - 012  : Logout                     :  TEST FAILED...! :  Error - Invalid or expired session token. \033[0m") # login failed so test passed


