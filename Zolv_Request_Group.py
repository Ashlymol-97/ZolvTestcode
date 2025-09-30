


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
request_group_id=None
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





# 1: Create Request Group : 


    create_request_group_payload ={
        "name": "Request Grouper8",
        "remarks":"remart",
        "isActive":to_bool(True)
    }


    create_request_group = requests.post(base_url + f"api/v1/tasks/request-group/web/{company_id}/create-request-group",json=create_request_group_payload,headers=headers)
    if create_request_group.status_code == 201:
        create_request_group_json=create_request_group.json()
        # request_group_id = create_request_group_json['id']

    #    print("Response JSON : ",json.dumps(create_request_group_json,indent=4))
        # print(request_group_id)
        print(f"\033[92m✅ Test Case ID - 005 : Request Group Creation   : TEST PASSED...!  \033[0m")
    else:
        create_request_group.text
        print(f"\033[91m❌ Test Case ID - 005 : Request Group Creation   : TEST FAILED...! : Request group with the same name exists  \033[0m")
    





    # 2 : Request Group Get List: 


    request_group_get_list = requests.get(base_url + f"api/v1/tasks/request-group/web/{company_id}/get-request-group-list",headers=headers)
    if request_group_get_list.status_code == 200:
        request_group_get_list_json=request_group_get_list.json()
        # print("Response JSON : ",json.dumps(request_group_get_list_json,indent=4))
        request_group_id = request_group_get_list_json['requestGroup'][0]['id']

        # print(request_group_id)
        print(f"\033[92m✅ Test Case ID - 005 : Request Group Get List   : TEST PASSED...!  \033[0m")
    else:
        request_group_get_list.text
        print(f"\033[91m❌ Test Case ID - 005 : Request Group Get List   : TEST FAILED...! : Invalid endpoint specified  \033[0m")







     
# 3 : Update Request Group : 

    update_request_group_payload ={
        "name": "Task47",
        "remarks":"remart",
        "isActive":to_bool(False)
    }
    update_request_group = requests.put(base_url + f"api/v1/tasks/request-group/web/{company_id}/update-group/{request_group_id}",json=update_request_group_payload,headers=headers)
    if update_request_group.status_code == 200:
        update_request_group=update_request_group.json()
        # print("Response JSON : ",json.dumps(update_request_group,indent=4))
        print(f"\033[92m✅ Test Case ID - 007 : Request Group Updation   : TEST PASSED...!  \033[0m")
    else:
        update_request_group.text
        print(f"\033[91m❌ Test Case ID - 007 : Request Group Updation   : TEST FAILED...! : Invalid data or ID  \033[0m",update_request_group.text)

        print(request_group_id)


    






      
# 4 : Task Group Detailed :

    response_task_group_detailed=requests.get(base_url + f"api/v1/tasks/request-group/web/{company_id}/get-request-group-details/{request_group_id}",headers=headers)
    if response_task_group_detailed.status_code==200:
        response_task_group_detailed_json = response_task_group_detailed.json()
        print("Response JSON:", json.dumps(response_task_group_detailed_json, indent=4))
        print(f"\033[92m✅ Test Case ID - 006 : Request Group Detailed  : TEST PASSED...!  \033[0m")
        # response_delete=requests.patch(base_url + f"api/v1/tasks/request-group/web/{company_id}/delete-request/{request_group_id}")
        # if response_delete.status_code==200:
        #     print("Deleted")
        # else:
        #     print("Not Deleted")

    else:
        print(f"\033[91m❌ Test Case ID - 006 : Request Group Detailed  : TEST FAILED...! : Invalid Data or Invalid ID  \033[0m")







# Delete :




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
