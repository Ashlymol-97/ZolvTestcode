

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
    name=response_json.get('name')
    # print(f"\033[92m✅ Test Case ID - 001 : TEST PASSED...! : \033[0m")
    headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
                }


    create_request_group_payload ={
        "name": "Request Group666",
        "remarks":"remart",
        "isActive":to_bool(True)
    }

    create_request_group = requests.post(base_url + f"api/v1/tasks/request-group/web/{company_id}/create-request-group",json=create_request_group_payload,headers=headers)
    if create_request_group.status_code == 201:
        create_request_group_json=create_request_group.json()
        # request_group_id = create_request_group_json['id']
        # print(request_group_id)
#  Create Request Master : 


    Create_request_master={
        "name": "RequestMaster3",
        "description": "aaaa",
        "requestGroupId": [
            "68d3d832885c9068efd7de9d"  
            # request_group_id
        ],
        "requestStatus": [
        {
            "statusId": "string",
            "label": "string"
        }
        ],
        "workflowId": "string",
        "isActive": to_bool(True)
    }


    create_request_master = requests.post(base_url + f"api/v1/tasks/request-master/web/{company_id}/create-request-master",json=Create_request_master,headers=headers)
    if create_request_master.status_code == 200:
        create_request_master_json=create_request_master.json()
        request_master_id = create_request_master_json['id']
        print("Response JSON : ",json.dumps(create_request_master_json,indent=4))
        # print(request_master_id)
        print(f"\033[92m✅ Test Case ID - 002 : Request Master Creation   : TEST PASSED...!  \033[0m")
    else:
        # # error_message = create_request_master_json.get("errorMessage")
        # print(error_message)

        print(f"\033[91m❌ Test Case ID - 002 : Request Master Creation   : TEST FAILED...! : Task group with the same name exists \033[0m",create_request_master.text)


else:
    response_login.text
    print(f"\033[91m❌ Test Case ID - 001 : TEST FAILED...! : Error - Invalid Credentials \033[0m")





# Logout :
response_logout=requests.put(logout_url,headers=headers)
if response_logout.status_code == 200:
    # print("Logout Successfully")
    response_logout.text
else:
    response_logout.text
    # print("Logout Failed")