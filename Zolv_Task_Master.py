
import requests
import json



# doubt

# def to_bool(value):
#     """Converts value into a strict boolean True/False."""
#     if isinstance(value, bool):   # Already a boolean
#         return value
#     if isinstance(value, str): 
#         if str in ["True","False","true","false"]:  # Strings like "true", "false", "1", "0"
#            return value.strip().lower() in ("true", "1", "yes", "y", "t")
        

#     if isinstance(value, (int, float)):  # Numbers: 1 → Truea, 0 → False
#         return value == 1
#     return False  

def to_bool(value: str) -> str:
    if value.strip() == "True":
        return "true"
    elif value.strip() == "False":
        return "false"
    return value




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
        # print("Response JSON : ",json.dumps(task_status_get_list_json,indent=4))
        taskStatus1=task_status_get_list_json['taskStatus'][0]['id']
        taskStatus2=task_status_get_list_json['taskStatus'][1]['id']

    else:
        task_status_get_list.text
        print(task_status_get_list.text)
        
        print("Failed")
         
# Get Execution department : 

        execution_departments = requests.get(base_url + "api/v1/masters/execution-department-list", headers=headers)
        if execution_departments.status_code==200:

           print(execution_departments.json())
        print("Failed list")


# 1 : Create Task Master : 


#     data = {
#         "name": "uhest",
#         "executionDepartment": "68709372293ae6389032a053",
#         "conditionalOutputAction": True,  # Assuming this should be a boolean
#         "taskGroupId": "6d83b402885c9068efd7de7a",
#         "taskStatus": [
#             {
#                 "statusId": "68c947c1c7a22fd66932a03c",
#                 "label": "open"
#             },
#             {
#                 "statusId": "68c947c1c7a22fd66932a03d",
#                 "label": "pending"
#             }
#         ],
#         "isActive": True
#     }

# # files = {
# #     "uploadfiles": ("uploadfiles.avif", open("uploadfiles.avif", "rb"), "image/avif")
# # }

    


#     # doubt
#     create_task_master = requests.post(base_url + f"api/v1/tasks/task-master/web/{company_id}/create-task-master",headers=headers,json=data)
#     if create_task_master.status_code == 201:
#         create_task_master_json=create_task_master.json()
#         # task_master_id = create_task_master_json['id']
#         print("Response JSON : ",json.dumps(create_task_master_json,indent=4))
#         # print(task_group_id)
#         print(f"\033[92m✅ Test Case ID - 002 : Task Master Creation   : TEST PASSED...!  \033[0m")
#     else:
#         error_text=create_task_master.json()["errorMessage"]
#         print(f"\033[91m❌ Test Case ID - 002 : Task Master Creation   : TEST FAILED...! : {error_text}  \033[0m",create_task_master.status_code)





        

    data = {
        "name": "tasktest",
        "executionDepartment": "68709372293ae6389032a053",
        "conditionalOutputAction": to_bool(str(True)),
        "taskGroupId": "6d83b402885c9068efd7de7a",
        "taskStatus": [
            {
                "statusId": taskStatus1,
                "label": "open"
            },
            {
                "statusId": taskStatus2,
                "label": "pending"
            }
        ],
        "isActive": to_bool(str(True))
    }


    create_task_master = requests.post(base_url + f"api/v1/tasks/task-master/web/{company_id}/create-task-master",headers=headers,json=data)
    if create_task_master.status_code == 201:
        create_task_master_json=create_task_master.json()
        # task_master_id = create_task_master_json['id']
        print("Response JSON : ",json.dumps(create_task_master_json,indent=4))
        # print(task_group_id)
        print(taskStatus1)
        print(f"\033[92m✅ Test Case ID - 002 : Task Master Creation   : TEST PASSED...!  \033[0m")
    else:
        error_text=create_task_master.json()["errorMessage"]
        print(f"\033[91m❌ Test Case ID - 002 : Task Master Creation   : TEST FAILED...! : {error_text}  \033[0m")








    
    # 2 : Task Master Get List: 


    task_master_get_list = requests.get(base_url + f"api/v1/tasks/task-master/web/{company_id}/get-task-master-list",headers=headers)
    if task_master_get_list.status_code == 200:
        task_master_get_list_json=task_master_get_list.json()
        # print("Response JSON : ",json.dumps(task_master_get_list_json,indent=4))
        task_master_id = task_master_get_list_json['taskMasters'][0]['id']

        # print(task_master_id)
        print(f"\033[92m✅ Test Case ID - 005 : Task Master Get List   : TEST PASSED...!  \033[0m")
    else:
        error_text=task_master_get_list.json()["errorMessage"]
        task_master_get_list.text
        print(f"\033[91m❌ Test Case ID - 005 : Task Master Get List   : TEST FAILED...! : {error_text}  \033[0m")



   


    

    
     
# 3 : Update Task Master : 

    update_task_master_payload ={
        "name": "tasktestupdated",
        "executionDepartment": "68709372293ae6389032a053",
        "conditionalOutputAction": to_bool(str(True)),
        "taskGroupId": "6d83b402885c9068efd7de7a",
        "taskStatus": [
            {
                "statusId": taskStatus1,
                "label": "open"
            },
            {
                "statusId": taskStatus2,
                "label": "pending"
            }
        ],
        "isActive": to_bool(str(True))
    }

    update_task_master = requests.put(base_url + f"api/v1/tasks/task-master/web/{company_id}/update-task-master/{task_master_id}",json=update_task_master_payload,headers=headers)
    if update_task_master.status_code == 200:
        update_task_master_json=update_task_master.json()
        # print("Response JSON : ",json.dumps(update_task_master_json,indent=4))
        print(f"\033[92m✅ Test Case ID - 007 : Task Master Updation   : TEST PASSED...!  \033[0m")
    else:
        error_text=update_task_master.json()["errorMessage"]
        update_task_master.text
        print(f"\033[91m❌ Test Case ID - 007 : Task Master Updation   : TEST FAILED...! : {error_text}  \033[0m")






    
      
# 4 : Task Master Detailed :

    Task_master_detailed=requests.get(base_url + f"api/v1/tasks/task-master/web/{company_id}/get-task-master-details/{task_master_id}",headers=headers)
    if Task_master_detailed.status_code==200:
        Task_master_detailed_json = Task_master_detailed.json()
        # print("Response JSON:", json.dumps(Task_master_detailed_json, indent=4))
        print(f"\033[92m✅ Test Case ID - 006 : Task Master Detailed   : TEST PASSED...!  \033[0m")

        # response_delete=requests.patch(base_url + f"api/v1/tasks/request-group/web/{company_id}/delete-taskmaster/{task_master_id}")
        # if response_delete.status_code==200:
        #     print("Deleted")
        # else:
        #     print("Not Deleted")

    else:
        error_text=Task_master_detailed.json()["errorMessage"]
        print(f"\033[91m❌ Test Case ID - 006 : Task Master Detailed    : TEST FAILED...! : {error_text}  \033[0m")



    
else:
    print(f"\033[91m❌ Test Case ID - 001 : TEST FAILED...!  :  Invalid Credentials \033[0m")