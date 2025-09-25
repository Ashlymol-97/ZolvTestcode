
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

response_login = requests.post(login_url,json=login_payload)
if response_login.status_code == 200:
    response_json = response_login.json()
    token= response_json.get('token',{}).get('token')
    company_id=response_json['company']['id']
    headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
    }
    create_request_group_payload ={
        "name": "Request 36",
        "remarks":"remart",
        "isActive":to_bool(True)
    }

    create_request_group = requests.post(base_url + f"api/v1/tasks/request-group/web/{company_id}/create-request-group",json=create_request_group_payload,headers=headers)
    if create_request_group.status_code == 201:
        create_request_group_json=create_request_group.json()
        request_group_id = create_request_group_json['id']
        # print(request_group_id)


#  Update Task Group : 

        update_request_group_payload ={
            "name": "Task 777",
            "remarks":"remart",
            "isActive":to_bool(False)
        }

        update_request_group = requests.put(base_url + f"api/v1/tasks/request-group/web/{company_id}/update-group/{request_group_id}",json=update_request_group_payload,headers=headers)
        if update_request_group.status_code == 200:
            update_request_group=update_request_group.json()
        #    print("Response JSON : ",json.dumps(update_request_group,indent=4))
            print(f"\033[92m✅ Test Case ID - 007 : Request Group Updation   : TEST PASSED...!  \033[0m")
        else:
            update_request_group.text
            print(f"\033[91m❌ Test Case ID - 007 : Request Group Updation   : TEST FAILED...! : Invalid data or ID  \033[0m",update_request_group.text)


else:
    print(f"\033[91m❌ TEST FAILED...! : Error - Invalid Credentials \033[0m")