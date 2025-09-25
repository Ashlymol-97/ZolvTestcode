
import requests
import json


base_url = "https://qa-tasks.zolv.health/"

login_url= "https://qa-admin.zolv.health/api/v1/user/task-login"
logout_url="https://qa-admin.zolv.health/api/v1/user/logout"



login_payload = {
    "loginId": "UserRequest",
    "password": "Smm@1234"
}


print("\033[1;34m Task Group Detailed \033[0m")


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
    headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
                }
   
    response_Task_Group_list = requests.get(base_url + f"api/v1/masters/task-group/web/{company_id}/get-task-group-list",headers=headers)
    if response_Task_Group_list.status_code == 200:
        response_Task_Group_list_json = response_Task_Group_list.json()
        # print("Response JSON:", json.dumps(response_Task_Group_list_json, indent=4))
        taskGroupId=response_Task_Group_list_json['taskGroup'][0]['id']
        # print(taskGroupId)

#Task Group Detailed :
        response_task_group_detailed=requests.get(base_url + f"api/v1/masters/task-group/web/{company_id}/get-task-group-details/{taskGroupId}",headers=headers)
        if response_task_group_detailed.status_code==200:
          response_task_group_detailed_json = response_task_group_detailed.json()
          # print("Response JSON:", json.dumps(response_task_group_detailed_json, indent=4))
          print(f"\033[92m✅ Test Case ID - 003 : Task Group Detailed  : TEST PASSED...! : Task Group Detailed \033[0m")

        else:
          print(f"\033[91m❌ Test Case ID - 003 : Task Group Detailed  : TEST FAILED...! : Invalid Data or Invalid ID  \033[0m")

    else:
        print(f"Failed to list Task Group List")
        # print(response_Task_Group_list.text)





# Logout :
response_logout=requests.put(logout_url,headers=headers)
if response_logout.status_code == 200:
    # print("Logout Successfully")
    response_logout.text
else:
    response_logout.text
    # print("Logout Failed")