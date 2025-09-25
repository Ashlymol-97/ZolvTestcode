
import requests
import json





def to_bool(value):
    """Converts value into a strict boolean True/False."""
    if isinstance(value, bool):   # Already a boolean
        return value
    if isinstance(value, str): 
        if str in ["True","False","true","false"]:  # Strings like "true", "false", "1", "0"
           return value.strip().lower() in ("true", "1", "yes", "y", "t")
        

    if isinstance(value, (int, float)):  # Numbers: 1 → Truea, 0 → False
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
    # print("Response JSON : ",json.dumps(response_json,indent=4))
    token= response_json.get('token',{}).get('token')
    company_id=response_json['company']['id']
    name=response_json.get('name')
    # print(f"\033[92m✅ Test Case ID - 001 : TEST PASSED...! : \033[0m")
    headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
                }
    

    # Task Status :
    task_status_get_list=requests.get(base_url + f"api/v1/masters/status/web/get-task-status-list",headers=headers)
    if task_status_get_list.status_code==200:
        task_status_get_list_json=task_status_get_list.json()
        print("Response JSON : ",json.dumps(task_status_get_list_json,indent=4))
        taskStatus1=task_status_get_list_json['taskStatus'][0]['id']
        taskStatus2=task_status_get_list_json['taskStatus'][1]['id']

        print(taskStatus1)
    else:
        task_status_get_list.text
        print(task_status_get_list.text)
        
        print("Failed")
              
#  Create Task Group : 


    create_task_master_payload ={
          "name": "Trest1",
          "executionDepartment": "68709372293ae6389032a053",
          "conditionalOutputAction": to_bool(True),
          # "statusBasedOutputTrigger": "",
          "taskGroupId":"68d3b402885c9068efd7de7a",
          "taskStatus": [
              {"id": taskStatus1, "name": "open"},
              {"id": taskStatus2, "name": "pending"}
        ],
          "uploadFile": "",  
          "isActive": to_bool(True)
    }


    # doubt
    create_task_group = requests.post(base_url + f"api/v1/tasks/task-master/web/{company_id}/create-task-master",json=create_task_master_payload,headers=headers)
    if create_task_group.status_code == 201:
        create_task_group_json=create_task_group.json()
        task_group_id = create_task_group_json['id']
    #    print("Response JSON : ",json.dumps(create_task_group_json,indent=4))
        # print(task_group_id)
        print(f"\033[92m✅ Test Case ID - 002 : Task Group Creation   : TEST PASSED...!  \033[0m")
    else:
        print(f"\033[91m❌ Test Case ID - 002 : Task Group Creation   : TEST FAILED...! : Invalid data or missing fields  \033[0m",create_task_group.text)


else:
    print(f"\033[91m❌ Test Case ID - 001 : TEST FAILED...! : Error - Invalid Credentials \033[0m")