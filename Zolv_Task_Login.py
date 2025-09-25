
import requests
import json

print(f"\033[1;92mZolv Task management.\033[0m")


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




