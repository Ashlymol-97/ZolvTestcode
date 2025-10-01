


import requests
import json



print("\033[1;34mRequest Group \033[0m")


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
        "name": "Request Grouper865",
        "remarks":"remart",
        "isActive":True
    }


    create_request_group = requests.post(base_url + f"api/v1/tasks/request-group/web/{company_id}/create-request-group",json=create_request_group_payload,headers=headers)
    if create_request_group.status_code == 201:
        create_request_group_json=create_request_group.json()
        # request_group_id = create_request_group_json['id']

    #    print("Response JSON : ",json.dumps(create_request_group_json,indent=4))
        # print(request_group_id)
        print(f"\033[92m✅ Test Case ID - RG1 : Request Group Creation   : TEST PASSED...!  \033[0m")
    else:
        # print(create_request_group.text)
        # print(create_request_group.json()["errorMessage"])
        error_text=create_request_group.json()["errorMessage"]
        print(f"\033[91m❌ Test Case ID - RG1 : Request Group Creation   : TEST FAILED...! : {error_text}\033[0m")
    





    # 2 : Request Group Get List: 


    request_group_get_list = requests.get(base_url + f"api/v1/tasks/request-group/web/{company_id}/get-request-group-list",headers=headers)
    if request_group_get_list.status_code == 200:
        request_group_get_list_json=request_group_get_list.json()
        # print("Response JSON : ",json.dumps(request_group_get_list_json,indent=4))
        request_group_id = request_group_get_list_json['requestGroup'][0]['id']

        # print(request_group_id)
        print(f"\033[92m✅ Test Case ID - RG2 : Request Group Get List   : TEST PASSED...!  \033[0m")
    else:
        # print(request_group_get_list.text)
        error_text=request_group_get_list.json()["errorMessage"]
        print(f"\033[91m❌ Test Case ID - RG2 : Request Group Get List   : TEST FAILED...! : {error_text} \033[0m")







     
# 3 : Update Request Group : 

    update_request_group_payload ={
        "name": "Task473",
        "remarks":"remart",
        "isActive":False
    }
    update_request_group = requests.put(base_url + f"api/v1/tasks/request-group/web/{company_id}/update-group/{request_group_id}",json=update_request_group_payload,headers=headers)
    if update_request_group.status_code == 200:
        update_request_group=update_request_group.json()
        # print("Response JSON : ",json.dumps(update_request_group,indent=4))
        print(f"\033[92m✅ Test Case ID - RG3 : Request Group Updation   : TEST PASSED...!  \033[0m")
    else:
        error_text=update_request_group.json()["errorMessage"]
        print(f"\033[91m❌ Test Case ID - RG3 : Request Group Updation   : TEST FAILED...! : {error_text}  \033[0m")

        # print(update_request_group.text)


    






      
# 4 : Request Group Detailed :

    response_request_group_detailed=requests.get(base_url + f"api/v1/tasks/request-group/web/{company_id}/get-request-group-details/{request_group_id}",headers=headers)
    if response_request_group_detailed.status_code==200:
        request_group_detailed_json = response_request_group_detailed.json()
        # print("Response JSON:", json.dumps(request_group_detailed_json, indent=4))
        print(f"\033[92m✅ Test Case ID - RG4 : Request Group Detailed   : TEST PASSED...!  \033[0m")
        # response_delete=requests.patch(base_url + f"api/v1/tasks/request-group/web/{company_id}/delete-request/{request_group_id}")
        # if response_delete.status_code==200:
        #     print("Deleted")
        # else:
        #     print("Not Deleted")

    else:
        error_text=response_request_group_detailed.json()["errorMessage"]

        print(f"\033[91m❌ Test Case ID - RG4 : Request Group Detailed   : TEST FAILED...! : {error_text}  \033[0m")
        # print(response_request_group_detailed.text)





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
