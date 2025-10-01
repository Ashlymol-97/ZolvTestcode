
import requests
import json




print("\033[1;34mTask Group \033[0m")



base_url = "https://qa-tasks.zolv.health/"

login_url= "https://qa-tasks.zolv.health/api/v1/user/task-login"
logout_url="https://qa-tasks.zolv.health/api/v1/user/logout"

login_payload = {
    "loginId": "UserRequest",
    "password": "Smm@1234"
}
headers=None
taskGroupId=None
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

# 1 : Create Task Group : 


    create_task_group_payload ={
        "name": "Task Grou7p25",
        "remarks":"remart",
        "isActive":False
    }

    create_task_group = requests.post(base_url + f"api/v1/tasks/task-group/web/{company_id}/create-task-group",json=create_task_group_payload,headers=headers)
    if create_task_group.status_code == 200:
        create_task_group_json=create_task_group.json()
        # task_group_id = create_task_group_json['id']
        # print("Response JSON : ",json.dumps(create_task_group_json,indent=4))
        # print(task_group_id,create_task_group.status_code)
        print(f"\033[92m✅ Test Case ID - 002 : Task Group Creation   : TEST PASSED...!  \033[0m")
    else:
        error_text=create_task_group.json()["errorMessage"]
        print(f"\033[91m❌ Test Case ID - 002 : Task Group Creation   : TEST FAILED...! : {error_text} \033[0m")
        # print(create_task_group.text)









# 2 : Task Group List :
    taskGroupId=None
    response_Task_Group_list = requests.get(base_url + f"api/v1/tasks/task-group/web/{company_id}/get-task-group-list",headers=headers)
    if response_Task_Group_list.status_code == 200:
        response_Task_Group_list_json = response_Task_Group_list.json()
        # print("Response JSON : ",json.dumps(response_Task_Group_list_json,indent=4))
        print(f"\033[92m✅ Test Case ID - 004 : Task Group List       : TEST PASSED...!  \033[0m")
        taskGroupId=response_Task_Group_list_json['taskGroup'][0]['id']
        # print(taskGroupId)
    else:
        error_text=response_Task_Group_list.json()["errorMessage"]
        print(f"\033[91m❌ Test Case ID - 002 : Task Group List       : TEST FAILED...! : {error_text} \033[0m")
        # print(response_Task_Group_list.text)







# 3 :  Update Task Group : 

    update_task_group_payload ={
        "name": "Task 273",
        "remarks":"remart",
        "isActive":False
    }

    update_task_group = requests.put(base_url + f"api/v1/tasks/task-group/web/{company_id}/update-group/{taskGroupId}",json=update_task_group_payload,headers=headers)
    if update_task_group.status_code == 200:
        update_task_group_json=update_task_group.json()
        # print("Response JSON : ",json.dumps(update_task_group_json,indent=4))
        print(f"\033[92m✅ Test Case ID - 004 : Task Group Updation   : TEST PASSED...!  \033[0m")
    else:
        update_task_group.text
        error_text=update_task_group.json()["errorMessage"]
        print(f"\033[91m❌ Test Case ID - 004 : Task Group Updation   : TEST FAILED...! : {error_text}  \033[0m")







#4 :Task Group Detailed :

    response_task_group_detailed=requests.get(base_url + f"api/v1/tasks/task-group/web/{company_id}/get-task-group-details/{taskGroupId}",headers=headers)
    if response_task_group_detailed.status_code==200:
        response_task_group_detailed_json = response_task_group_detailed.json()
        # print("Response JSON:", json.dumps(response_task_group_detailed_json, indent=4))
        print(f"\033[92m✅ Test Case ID - 003 : Task Group Detailed   : TEST PASSED...!  \033[0m")

    else:
        error_text=response_task_group_detailed.json()["errorMessage"]
        print(f"\033[91m❌ Test Case ID - 003 : Task Group Detailed   : TEST FAILED...! : {error_text}  \033[0m")





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