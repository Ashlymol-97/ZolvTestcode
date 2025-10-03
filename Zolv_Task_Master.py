
import requests
import json
import os
admin_login_url= "https://qa-admin.zolv.health/api/v1/user/login"
admin_logout_url="https://qa-admin.zolv.health/api/v1/user/logout"


admin_login_payload = {
    "loginId": "AshlyAdmin",
    "password": "Smm@1234"
}


print("\033[1;34mTask Master \033[0m")




def to_bool(value):
    """Converts value into a strict boolean True/False."""
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in ("true", "1", "yes", "y", "t")
    if isinstance(value, (int, float)):
        return value == 1
    return False




# Get Execution department : 
execution_department_id=None
admin_login = requests.post(admin_login_url,json=admin_login_payload)
if admin_login.status_code == 200:
    admin_login_json = admin_login.json()
    # print("Response JSON : ",json.dumps(admin_login_json,indent=4))
    admin_token= admin_login_json.get('token',{}).get('token')
    company_id=admin_login_json['company']['id']
    admin_header = {
        "Authorization": f"Bearer {admin_token}",
        "Content-Type": "application/json"
    }

    admin_base_url="https://qa-admin.zolv.health/"
    execution_departments = requests.get(admin_base_url + f"api/v1/masters/department/web/{company_id}/get-department-list?isActive=&name=&ignorePaging=false&size=10&sort=1&page=1",headers=admin_header)
    if execution_departments.status_code==200:
        execution_departments_json=execution_departments.json()
        # print("Response JSON : ",json.dumps(execution_departments_json,indent=4))
        execution_department_id=execution_departments_json['departments'][1]['id']
    else:
        print("Failed list")

# print("Login Failed")


    # Logout :

    response_logout=requests.put(admin_logout_url,headers=admin_header)
    if response_logout.status_code == 200:
        # print("Logout Successfully")
        response_logout.text
    else:
        response_logout.text
        # print("Logout Failed")









# Tasks :


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
         
    




# 2 : Task Group List :

    taskgroupid=None
    Task_Group_list = requests.get(base_url + f"api/v1/tasks/task-group/web/{company_id}/get-task-group-list",headers=headers)
    if Task_Group_list.status_code == 200:
        Task_Group_list_json = Task_Group_list.json()
        # print("Response JSON : ",json.dumps(Task_Group_list_json,indent=4))
        # print(f"\033[92m✅ Task Group List       : TEST PASSED...!  \033[0m")
        taskgroupid=Task_Group_list_json['taskGroup'][17]['id']
        # print(taskgroupid)
    else:
        error_text=Task_Group_list.json()["errorMessage"]
        # print(f"\033[91m❌ Task Group List       : TEST FAILED...! : {error_text} \033[0m")
        # print(response_Task_GroTask_Group_listup_list.text)


    

    # 1 : Create Task MASTER :
    task_master_id=None
    data = {
        "name": "thes9",
        "executionDepartment": execution_department_id,
        "conditionalOutputAction": str(to_bool(True)).lower(),
        "taskGroupId": taskgroupid,
        "taskStatus[0].statusId": taskStatus1,
        "taskStatus[0].label": "open",
        "taskStatus[1].statusId": taskStatus2,
        "taskStatus[1].label": "pending",
        "isActive": str(to_bool(True)).lower()
    }

    desktop_path = r"C:\Users\SMM-06\Desktop\file1.txt"

    # Auto-create the file if it doesn't exist
    if not os.path.exists(desktop_path):
        with open(desktop_path, "w") as f:
            f.write("Sample content for upload")

    with open(desktop_path, "rb") as f:
        files = {
            "uploadfiles": ("dfadgdf.txt", f, "text/plain")
        }
        response = requests.post(
            base_url + f"api/v1/tasks/task-master/web/{company_id}/create-task-master",
            headers={"Authorization": f"Bearer {token}"},
            data=data,
            files=files,
            timeout=60
        )
        if response.status_code==200:
            task_master_creation_json=response.json()

            # print(response.status_code)
            # print(response.text)
            print(f"\033[92m✅ Test Case ID - TM1 : Task Master Creation   : TEST PASSED...!  \033[0m")
            task_master_id = task_master_creation_json['id']
            # print(task_master_id)
        else:
            error_text=response.json()["errorMessage"]
            response.text
            print(f"\033[91m❌ Test Case ID - 005 : Task Master Creation   : TEST FAILED...! : {error_text}  \033[0m")

        







    
    # 2 : Task Master Get List: 


    task_master_get_list = requests.get(base_url + f"api/v1/tasks/task-master/web/{company_id}/get-task-master-list",headers=headers)
    if task_master_get_list.status_code == 200:
        task_master_get_list_json=task_master_get_list.json()
        # print("Response JSON : ",json.dumps(task_master_get_list_json,indent=4))
        # task_master_id = task_master_get_list_json['taskMasters'][0]['id']

        # print(task_master_id)
        print(f"\033[92m✅ Test Case ID - 005 : Task Master Get List   : TEST PASSED...!  \033[0m")
    else:
        error_text=task_master_get_list.json()["errorMessage"]
        task_master_get_list.text
        print(f"\033[91m❌ Test Case ID - 005 : Task Master Get List   : TEST FAILED...! : {error_text}  \033[0m")



   


    

    
     
# 3 : Update Task Master : 

    Update_data = {
        "name": "th",
        "executionDepartment": execution_department_id,
        "conditionalOutputAction": str(to_bool(True)).lower(),
        "taskGroupId": taskgroupid,
        "taskStatus[0].statusId": taskStatus1,
        "taskStatus[0].label": "open",
        "taskStatus[1].statusId": taskStatus2,
        "taskStatus[1].label": "pending",
        "isActive": str(to_bool(True)).lower()
    }

    desktop_path = r"C:\Users\SMM-06\Desktop\file1.txt"

    # Auto-create the file if it doesn't exist
    if not os.path.exists(desktop_path):
        with open(desktop_path, "w") as f:
            f.write("Sample content for upload")

    with open(desktop_path, "rb") as f:
        files = {
            "uploadfiles": ("dfadgdf.txt", f, "text/plain")
        }
        response_update = requests.put(
            base_url + f"api/v1/tasks/task-master/web/{company_id}/update-task-master/{task_master_id}",
            headers={"Authorization": f"Bearer {token}"},
            data=data,
            files=files,
            timeout=60
        )
    if response_update.status_code == 200:
        response_update_json=response_update.json()
        # print("Response JSON : ",json.dumps(response_update_json,indent=4))
        print(f"\033[92m✅ Test Case ID - 007 : Task Master Updation   : TEST PASSED...!  \033[0m")
    else:
        error_text=response_update.json()["errorMessage"]
        response_update.text
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










# Logout :
# response_logout=requests.put(logout_url,headers=headers)
# if response_logout.status_code == 200:
#     # print("Logout Successfully")
#     response_logout.text
# else:
#     response_logout.text
#     # print("Logout Failed")
