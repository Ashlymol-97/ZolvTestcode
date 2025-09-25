
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


    Task_Group_list = requests.get(base_url + f"api/v1/masters/task-group/web/{company_id}/get-task-group-list",headers=headers)
    if Task_Group_list.status_code == 200:
        Task_Group_list_json = Task_Group_list.json()
        # print("Response JSON:", json.dumps(Task_Group_list, indent=4))
        taskGroupId=Task_Group_list_json['taskGroup'][0]['id']


#  Update Task Group : 

        update_task_group_payload ={
            "name": "Task 3",
            "remarks":"remart",
            "isActive":to_bool(False)
        }

        update_task_group = requests.put(base_url + f"api/v1/masters/task-group/web/{company_id}/update-group/{taskGroupId}",json=update_task_group_payload,headers=headers)
        if update_task_group.status_code == 200:
            update_task_group_json=update_task_group.json()
        #    print("Response JSON : ",json.dumps(update_task_group_json,indent=4))
            print(f"\033[92m✅ Test Case ID - 004 : Task Group Updation   : TEST PASSED...!  \033[0m")
        else:
            update_task_group.text
            print(f"\033[91m❌ Test Case ID - 004 : Task Group Updation   : TEST FAILED...! : Invalid data or ID  \033[0m")


else:
    print(f"\033[91m❌ TEST FAILED...! : Error - Invalid Credentials \033[0m")