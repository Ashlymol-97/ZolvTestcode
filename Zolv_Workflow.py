
import requests
import json


failed_count=0
Toyal_count=0


# Not Completed :



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




# Login : 

response_login = requests.post(login_url,json=login_payload)
if response_login.status_code != 200:
    failed_count+=1
else:
    response_json = response_login.json()
    # print("Response JSON : ",json.dumps(response_json,indent=4))
    token= response_json.get('token',{}).get('token')
    company_id=response_json['company']['id']
    headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
    }




# 1 : Work Flow : Creation

    print("\033[1;34mWork Flow Creation !\033[0m")

    create_workflow_payload = {
      "name": "Workflow",
      "isActive": to_bool(True),
      "data": {}
    }

    create_work_flow = requests.post(base_url + f"api/v1/tasks/workflow/web/{company_id}/create-workflow",json=create_workflow_payload,headers=headers)
    if create_work_flow.status_code == 201:
       create_work_flow_json=create_work_flow.json()
       workflow_id = create_work_flow_json['id']
    
    #    print("Work Flow Created Successfully..!",create_work_flow.text,area_id)
    #    print("Response JSON : ",json.dumps(create_work_flow_json,indent=4))
       print(f"\033[92m✅ Test Case ID - WF1 : Work Flow  Creation     : TEST PASSED...!  \033[0m")
    else:
       failed_count+=1

       print(f"\033[91m❌ Test Case ID - WF1 : Work Flow Creation       : TEST FAILED...! : Invalid data or missing fields  \033[0m")
 
      #  print("Failed Creation.",create_work_flow.text) 











    
# 2 :   Work Flow Get List: 

    print("\033[1;34mWork Flow Get List !\033[0m")
    Work_Flow_id=None
    Work_Flow_get_list = requests.get(base_url + f"api/v1/tasks/workflow/web/{company_id}/get-workflow-list",headers=headers)
    if Work_Flow_get_list.status_code == 200:
        Work_Flow_get_list_json=Work_Flow_get_list.json()
        Work_Flow_id = Work_Flow_get_list_json['id']
        print("Response JSON : ",json.dumps(Work_Flow_get_list_json,indent=4))
        # print(Work_Flow_id)
        print(f"\033[92m✅ Test Case ID - WF2 : Work Flow  Get List         : TEST PASSED...!  \033[0m")
    else:
        Work_Flow_get_list.text
        failed_count+=1
        print(f"\033[91m❌ Test Case ID - WF2 : Work Flow Get List        : TEST FAILED...! : Invalid endpoint specified  \033[0m")
        # print(Work_Flow_get_list.text)













#  Work Flow Update : 


    print("\033[1;34mWork Flow  Update !\033[0m")

    update_work_flow_payload ={
      "name": "Workflowsupdated",
      "isActive": to_bool(True),
      "data": {}
    }
    

    work_flow_update = requests.put(
        base_url + f"api/v1/tasks/request-master/web/{company_id}/update-request-master/{Work_Flow_id}",
        json=update_work_flow_payload, 
        headers=headers
    )

    if work_flow_update.status_code == 200:
        work_flow_update_json = work_flow_update.json()
        print(f"\033[92m✅ Test Case ID - WF3 : Work Flow Updated          : TEST PASSED...! \033[0m")
    else: 
        failed_count += 1
        print(f"\033[91m❌ Test Case ID - WF3 : Work Flow Updated          : TEST FAILED...! : Invalid Input \033[0m")
        # print(work_flow_update.text)











# Work Flow Detailed : 


    print("\033[1;34mWork Flow Detailed !\033[0m")


    work_flow_detailed = requests.get(base_url + f"api/v1/tasks/request-master/web/{company_id}/get-request-master-details/{Work_Flow_id}",headers=headers)
    if work_flow_detailed.status_code == 200:
        # print("Work Flow Detailed")
        work_flow_detailed_json=work_flow_detailed.json()
        print(f"\033[92m✅ Test Case ID - WF4 : Get  Work Flow Detailed    : TEST PASSED...! \033[0m")
        print("Response JSON : ",json.dumps(work_flow_detailed_json,indent=4))

    else:
        failed_count+=1
        print(f"\033[91m❌ Test Case ID - WF4 : Get  Work Flow Detailed    : TEST FAILED...! : Invalid Input \033[0m")
        # print("Work Flow  Failed",work_flow_detailed.text)



