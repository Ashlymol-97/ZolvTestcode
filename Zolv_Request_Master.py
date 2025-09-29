

import requests
import json


failed_count=0
Toyal_count=0


# Not Completed :






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



# Request Group get list : 

    request_master_id=None

    Get_request_group = requests.get(base_url + f"api/v1/tasks/request-group/web/{company_id}/get-request-group-list",headers=headers)
    if Get_request_group.status_code == 200:
        Get_request_group_json=Get_request_group.json()
        # print("Response JSON : ",json.dumps(Get_request_group_json,indent=4))
        request_group_id1 = Get_request_group_json['requestGroup'][0]['id']
        request_group_id2 = Get_request_group_json['requestGroup'][1]['id']
        request_group_id3 = Get_request_group_json['requestGroup'][3]['id']


#Task status Get :
        get_task_status = requests.get(base_url + f"api/v1/masters/status/web/get-task-status-list",headers=headers)
    if get_task_status.status_code == 200:
        get_task_status_json=get_task_status.json()
        # print("Response JSON : ",json.dumps(get_task_status_json,indent=4))
        get_task_status_id1 = get_task_status_json['taskStatus'][0]['id']
        get_task_status_id2 = get_task_status_json['taskStatus'][1]['id']
        get_task_status_id3 = get_task_status_json['taskStatus'][3]['id']
        get_task_status_label1 = get_task_status_json['taskStatus'][0]['name']
        get_task_status_label2 = get_task_status_json['taskStatus'][1]['name']

        # print(get_task_status_label1)

#   Workflow Get: 
# 
# 
#       
#  Create Request Master : 

    print("\033[1;34mRequest Master Create !\033[0m")

    Create_request_master={
        "name":" request 89",

        "requestGroupIds":[request_group_id1,request_group_id2,request_group_id3],
        "isActive":False,
        # // "workflowId":"68d221b847a887d3dda9d6e1",
        "requestStatus":[
            {
            "statusId":get_task_status_id1,
            "label":get_task_status_label1
            },
            {
            "statusId":get_task_status_id2,
            "label":get_task_status_label2
            }
        ],
        "weightage":"a"
    }

    create_request_master = requests.post(base_url + f"api/v1/tasks/request-master/web/{company_id}/create-request-master",json=Create_request_master,headers=headers)
    if create_request_master.status_code == 201:
        create_request_master_json=create_request_master.json()
        request_master_id = create_request_master_json['id']
        # print("Response JSON : ",json.dumps(create_request_master_json,indent=4))
        # print(request_master_id)

        print(f"\033[92m✅ Test Case ID - RM1 : Request Master Creation         : TEST PASSED...!  \033[0m")
    else:
        # # error_message = create_request_master_json.get("errorMessage")
        # print(error_message)
        failed_count+=1
        print(f"\033[91m❌ Test Case ID - RM1 : Request Master Creation         : TEST FAILED...! : Task group with the same name exists \033[0m")
        print(create_request_master.text)
        






    
#   Request Master Get List: 

    print("\033[1;34mRequest Master Get List !\033[0m")

    request_Master_get_list = requests.get(base_url + f"api/v1/tasks/request-master/web/{company_id}/get-request-master-list",headers=headers)
    if request_Master_get_list.status_code == 200:
        request_Master_get_list_json=request_Master_get_list.json()
        request_master_id1 = request_Master_get_list_json['requestMasters'][0]['id']
        print("Response JSON : ",json.dumps(request_Master_get_list_json,indent=4))
        print(request_master_id)
        print(f"\033[92m✅ Test Case ID - RM2 : Request Master Get List         : TEST PASSED...!  \033[0m")
    else:
        request_Master_get_list.text
        failed_count+=1
        print(f"\033[91m❌ Test Case ID - RM2 : Request Master Get List         : TEST FAILED...! : Invalid endpoint specified  \033[0m")
        # print(request_group_get_list.text)








# Request Master Update : not completed 


    print("\033[1;34mRequest Master Update !\033[0m")

    update_request_master_payload={
        "name":" request 89",

        "requestGroupIds":[request_group_id1,request_group_id2,request_group_id3],
        "isActive":False,
        # // "workflowId":"68d221b847a887d3dda9d6e1",
        "requestStatus":[
            {
            "statusId":get_task_status_id1,
            "label":get_task_status_label1
            },
            {
            "statusId":get_task_status_id2,
            "label":get_task_status_label2
            }
        ],
        "weightage":"a"
    }



    request_master_update = requests.put(
        base_url + f"api/v1/tasks/request-master/web/{company_id}/update-request-master/{request_master_id1}",
        json=update_request_master_payload, 
        headers=headers
    )

    if request_master_update.status_code == 200:
        request_master_update_json = request_master_update.json()
        print(f"\033[92m✅ Test Case ID - RM3 : Request Master Updated          : TEST PASSED...! \033[0m")
    else: 
        failed_count += 1
        print(f"\033[91m❌ Test Case ID - RM3 : Request Master Updated          : TEST FAILED...! : Invalid Input \033[0m")
        print(request_master_update.text)










# # Request Master Detailed : 


    print("\033[1;34mRequest Master Detailed !\033[0m")


    request_master_detailed = requests.get(base_url + f"api/v1/tasks/request-master/web/{company_id}/get-request-master-details/{request_master_id1}",headers=headers)
    if request_master_detailed.status_code == 200:
        # print("Request Master Detailed")
        request_master_detailed_json=request_master_detailed.json()
        print(f"\033[92m✅ Test Case ID - RM4 : Get  Request Master Detailed    : TEST PASSED...! \033[0m")
        print("Response JSON : ",json.dumps(request_master_detailed_json,indent=4))

    else:
        failed_count+=1
        print(f"\033[91m❌ Test Case ID - RM4 : Get  Request Master Detailed    : TEST FAILED...! : Invalid Input \033[0m")
        print("Request Master Detailed  Failed",request_master_detailed.text)
















# Logout :
response_logout=requests.put(logout_url,headers=headers)
if response_logout.status_code == 200:
    # print("Logout Successfully")
    response_logout.text
else:
    response_logout.text
    # print("Logout Failed")