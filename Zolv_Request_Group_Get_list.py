
import requests
import json




base_url = "https://qa-tasks.zolv.health/"

login_url= "https://qa-tasks.zolv.health/api/v1/user/task-login"
logout_url="https://qa-tasks.zolv.health/api/v1/user/logout"

login_payload = {
    "loginId": "UserRequest",
    "password": "Smm@1234"
}
headers=None
response_login = requests.post(login_url,json=login_payload)
if response_login.status_code == 200:
    response_json = response_login.json()
    # print("Response JSON : ",json.dumps(response_json,indent=4))
    token= response_json.get('token',{}).get('token')
    company_id=response_json['company']['id']
    # print(f"\033[92mTEST PASSED...! : \033[0m")
    headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
    }

#   Request Group Get List: 


    request_group_get_list = requests.get(base_url + f"api/v1/tasks/request-group/web/{company_id}/get-request-group-list",headers=headers)
    if request_group_get_list.status_code == 200:
        request_group_get_list_json=request_group_get_list.json()
        print("Response JSON : ",json.dumps(request_group_get_list_json,indent=4))
        # print(request_group_id)
        print(f"\033[92m✅ Test Case ID - 005 : Request Group Get List   : TEST PASSED...!  \033[0m")
    else:
        request_group_get_list.text
        print(f"\033[91m❌ Test Case ID - 005 : Request Group Get List   : TEST FAILED...! : Invalid endpoint specified  \033[0m")


else:
    print(f"\033[91m❌ TEST FAILED...! : Error - Invalid Credentials \033[0m")



# Logout :
# response_logout=requests.put(logout_url,headers=headers)
# if response_logout.status_code == 200:
#     # print("Logout Successfully")
#     response_logout.text
# else:
#     response_logout.text
#     # print("Logout Failed")