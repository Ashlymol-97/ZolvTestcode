


import requests
import json





def to_bool(value):
    """Converts value into a strict boolean True/False."""
    if isinstance(value, bool):   # Already a boolean
        return value
    if isinstance(value, str): 
        if str in ["True","False","true","false"]:  # Strings like "true", "false", "1", "0"
           return value.strip().lower() in ("true", "1", "yes", "y", "t")
        

    if isinstance(value, (int, float)):  # Numbers: 1 → True, 0 → False
        return value == 1
    return False  






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

#  Create Request Group : 


    create_request_group_payload ={
        "name": "Request Group 23",
        "remarks":"remart",
        "isActive":to_bool(True)
    }


    create_request_group = requests.post(base_url + f"api/v1/tasks/request-group/web/{company_id}/create-request-group",json=create_request_group_payload,headers=headers)
    if create_request_group.status_code == 201:
        create_request_group_json=create_request_group.json()
        request_group_id = create_request_group_json['id']
    #    print("Response JSON : ",json.dumps(create_request_group_json,indent=4))
        # print(request_group_id)
        print(f"\033[92m✅ Test Case ID - 005 : Request Group Creation   : TEST PASSED...!  \033[0m")
    else:
        create_request_group.text
        print(f"\033[91m❌ Test Case ID - 005 : Request Group Creation   : TEST FAILED...! : Invalid data or missing fields  \033[0m")


else:
    print(f"\033[91m❌ TEST FAILED...! : Error - Invalid Credentials \033[0m")



# Logout :
response_logout=requests.put(logout_url,headers=headers)
if response_logout.status_code == 200:
    # print("Logout Successfully")
    response_logout.text
else:
    response_logout.text
    # print("Logout Failed")
