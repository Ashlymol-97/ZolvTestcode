import requests
import time
import json


print(f"\033[1;34m** ZOLV ADMIN TESTCODE **.\033[0m")


base_url= "https://qa-admin.zolv.health/"
login_url= "https://qa-admin.zolv.health/api/v1/user/login"
logout_url="https://qa-admin.zolv.health/api/v1/user/logout"



login_payload = {
    "loginId": "AshlyAdmin",
    "password": "Smm@1234"
}


failed_count=0
total_count=5
    
# 1 : Login : 

# print("\033[1;34mTESTING LOGIN!\033[0m")
response_login = requests.post(login_url,json=login_payload)
if response_login.status_code != 200:
    failed_count+=1
    error_text=response_login.json()["errorMessage"]
    print(f"\033[91m❌  Test Case ID - 001 : Login                      : TEST FAILED...! :   \033[0m")
    # print("Response:", response_login.json())
else:
    response_json = response_login.json()
    # print(f"Login Successfull   with status code {response_login.status_code}",login_payload)

    # print("Response JSON : ",json.dumps(response_json,indent=4))
    token= response_json.get('token',{}).get('token')
    company_id=response_json['company']['id']
    print(f"\033[92m✅ Test Case ID - 001 : Login                       : TEST PASSED...!  \033[0m")
    headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
    }
    # print(f"Token (Login): {token}") 









# ********************************************************Floor *******************************************



# 14 : Create Floor : 

    floor_payload={
    "name": "second floor",
    "code": 14,
    "buildingId": "68709372293ae6389032a058"
    }
    create_floor = requests.post(base_url + f"api/v1/masters/floor/web/{company_id}/create-floor",json=floor_payload,headers=headers)
    if create_floor.status_code == 201:
       create_floor_json=create_floor.json()
       floor_id = create_floor_json['id']
    #   print("Floor  Created Successfully..!",create_floor.text)
    #    print("Response JSON : ",json.dumps(create_floor_json,indent=4))
       print(f"\033[92m✅ Test Case ID - 014 : Floor Creation              : TEST PASSED...! \033[0m")
    else:
        failed_count+=1
        # error_text=create_floor.json()["errorMessage"]
        print(f"\033[91m❌ Test Case ID - 014 : Floor Creation              : TEST FAILED...! :  \033[0m")
 
    #    print("Failed Creation.",create_floor.text) 








# ******************************Time Delay *********************************************


    # wait_time = int(input("Enter wait time in seconds: "))

    # print("\033[38;5;208m⏳ Waiting for Area to be available in frontend...\033[0m")

    # # Countdown loop
    # for remaining in range(wait_time, 0, -1):
    #     print(f"\033[38;5;208m\r⏳ Waiting... {remaining} seconds left\033[0m", end="")
    #     time.sleep(1)

    # print("\033[38;5;208m\n✅ Done waiting!\033[0m")






# 15 : Floor : List ALL : 

    # print("\033[1;34mGet Area List!\033[0m")
    floor_list_all = requests.get(base_url + f"api/v1/masters/floor/web/{company_id}/get-floor-list",headers=headers)
    if floor_list_all.status_code == 201 :
        floor_list_json=floor_list_all.json()
        # print("Response JSON : ",json.dumps(floor_list_json,indent=4))
        # print("Floor Listed Successfully..!")
        print(f"\033[92m✅ Test Case ID - 015 : Get Floor List              : TEST PASSED...! \033[0m")

        # floor_id_detailed=floor_list_json['floors'][-1]['id']
        # floor_id_delete=floor_list_json['floors'][-1]['id']
        # print(floor_id_detailed)

    else:
        failed_count+=1
        # error_text=floor_list_all.json()["errorMessage"]
        print(f"\033[91m❌ Test Case ID - 015 : Get Floor List              : TEST FAILED...! :  \033[0m")

        # print("Floor Listed Failed..!",floor_list_all.text)

 





# # 16 : Floor : Get Detailed List : 

    # print("\033[1;34mTESTING AREA DETAILED LIST !\033[0m")
    floor_detailed_list = requests.get(base_url + f"api/v1/masters/floor/web/{company_id}/get-floor-list?floorId={floor_id}",headers=headers)
    if floor_detailed_list.status_code == 201:
        # print("Floor Detailed List Listed")
        floor_detailed_json=floor_detailed_list.json()
        print(f"\033[92m✅ Test Case ID - 016 : Get  Floor  Detailed        : TEST PASSED...! \033[0m")
        # print("Response JSON : ",json.dumps(floor_detailed_json,indent=4))

    else:
        failed_count+=1
        # error_text=floor_detailed_list.json()["errorMessage"]
        print(f"\033[91m❌ Test Case ID - 016 : Get  Floor  Detailed        : TEST FAILED...! : \033[0m")
        # print("Floor Detailed Listed Failed",floor_detailed_list.text)





# 17 : Floor : Update :  


    update_floor_payload = {
        "name": "second floor",
        "code": 14,
        "buildingId": "68709372293ae6389032a058"
    }

    floor_update = requests.put(
        base_url + f"api/v1/masters/floor/web/{company_id}/update-floor/{floor_id}",
        json=update_floor_payload,  # Corrected here
        headers=headers
    )

    if floor_update.status_code == 201:
        floor_update_json = floor_update.json()
        print(f"\033[92m✅ Test Case ID - 017 : Floor Updated               : TEST PASSED...! \033[0m")
    else: 
        failed_count += 1
        # error_text=floor_update.json()["errorMessage"]
        print(f"\033[91m❌ Test Case ID - 017 : Floor Updated               : TEST FAILED...! :  \033[0m")








# # 18 : Floor  :  Delete :

    floor_delete = requests.patch(base_url + f"api/v1/masters/floor/web/{company_id}/delete-floor/{floor_id}",headers=headers)
    if floor_delete.status_code == 200 :
        # print("Floor Deleted Successfully...!")
        print(f"\033[92m✅ Test Case ID - 018 : Floor Deleted               : TEST PASSED...!  \033[0m")

    else: 
        failed_count+=1
        # error_text=floor_delete.json()["errorMessage"]
        print(f"\033[91m❌ Test Case ID - 018 : Floor Deleted               : TEST FAILED...! :  \033[0m")
        # print("Floor Deleted failed...!",floor_delete.text) 


