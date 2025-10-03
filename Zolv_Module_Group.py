

import requests
import json

    # print("\033[1;34mModule Group \033[0m")




base_url = "https://qa-admin.zolv.health/"

login_url= "https://qa-admin.zolv.health/api/v1/user/login"
logout_url="https://qa-admin.zolv.health/api/v1/user/logout"



login_payload = {
    "loginId": "AshlyAdmin",
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


  # modules Get : 
  
    request_module_get_list = requests.get(base_url + f"api/v1/module/web/get-global-module-list",headers=headers)
    if request_module_get_list.status_code == 200:
        request_module_get_list_json=request_module_get_list.json()
        # print("Response JSON : ",json.dumps(request_module_get_list_json,indent=4))
        request_module_id1 = request_module_get_list_json['modulesList'][0]['id']
        request_module_id2 = request_module_get_list_json['modulesList'][1]['id']
        request_module_id3 = request_module_get_list_json['modulesList'][2]['id']
        request_module_id4 = request_module_get_list_json['modulesList'][3]['id']

        # print(request_module_id1)
        # print(f"\033[92m✅ Test Case ID - 006 : Modules Get List        : TEST PASSED...!  \033[0m")
    else:
        request_module_get_list.text
        # print(f"\033[91m❌ Test Case ID - 006 : Modules Get List        : TEST FAILED...! : Invalid endpoint specified  \033[0m")






# 1: Create Module Group : 


    create_module_group_payload ={
      "name":"Module11",
      "modules":[request_module_id3,request_module_id1],
      #  "requestGroup":"68db663aa688ac54c64b7102",
      "isActive":True

    }
  


    create_module_group = requests.post(base_url + f"api/v1/masters/module-group/web/{company_id}/create-module-group",json=create_module_group_payload,headers=headers)
    if create_module_group.status_code == 201:
        create_module_group_json=create_module_group.json()
        # request_group_id = create_module_group_json['id']

        print("Response JSON : ",json.dumps(create_module_group_json,indent=4))
        # print(request_group_id)
        print(f"\033[92m✅ Test Case ID - 005 : Module Group Creation   : TEST PASSED...!  \033[0m")
    else:
        create_module_group.text
        error_text=create_module_group.json()["errorMessage"]
        print(f"\033[91m❌ Test Case ID - 005 : Module Group Creation   : TEST FAILED...! : {error_text}  \033[0m")
    





    # 2 : Module Group Get List: 


    module_group_get_list = requests.get(base_url + f"api/v1/masters/module-group/web/{company_id}/get-modules-group-list",headers=headers)
    if module_group_get_list.status_code == 200:
        module_group_get_list_json=module_group_get_list.json()
        # print("Response JSON : ",json.dumps(module_group_get_list_json,indent=4))
        module_group_id = module_group_get_list_json['moduleGroups'][0]['id']

        # print(module_group_id)
        print(f"\033[92m✅ Test Case ID - 005 : Module Group Get List   : TEST PASSED...!  \033[0m")
    else:
        error_text=module_group_get_list.json()["errorMessage"]
        module_group_get_list.text
        print(f"\033[91m❌ Test Case ID - 005 : Module Group Get List   : TEST FAILED...! : {error_text}  \033[0m")







     
# # 3 : Update Module Group : 

#     update_request_group_payload ={
#         "name": "Task47",
#         "remarks":"remart",
#         "isActive":to_bool(False)
#     }
#     update_request_group = requests.put(base_url + f"api/v1/tasks/request-group/web/{company_id}/update-group/{request_group_id}",json=update_request_group_payload,headers=headers)
#     if update_request_group.status_code == 200:
#         update_request_group=update_request_group.json()
#         # print("Response JSON : ",json.dumps(update_request_group,indent=4))
#         print(f"\033[92m✅ Test Case ID - 007 : Request Group Updation   : TEST PASSED...!  \033[0m")
#     else:
#         update_request_group.text
        #  error_text=create_task_master.json()["errorMessage"]

#         print(f"\033[91m❌ Test Case ID - 007 : Request Group Updation   : TEST FAILED...! : Invalid data or ID  \033[0m",update_request_group.text)

#         print(request_group_id)


    










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
