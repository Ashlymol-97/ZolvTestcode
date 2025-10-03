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





# **************************Building *********************************




# 9 : : Building : Create :
    building_id=None
    # print("\033[1;34mTESTING BUILDING CREATION !\033[0m")
    create_building_payload = {
      "name": "Thejaswini",
      "code": 224
    }


    create_building = requests.post(base_url + f"api/v1/masters/building/web/{company_id}/create-building",json=create_building_payload,headers=headers)
    if create_building.status_code == 201:
        building_json=create_building.json()
        building_id = building_json['id']
        print(building_id)
        print("Response JSON : ",json.dumps(building_json,indent=4))
        # print("Create Building Successfully..!")
        print(f"\033[92m✅ Test Case ID - 009 : Building Creation           : TEST PASSED...! \033[0m")

    else:
        failed_count+=1
        # error_text=create_building.json()["errorMessage"]
        print(f"\033[91m❌ Test Case ID - 009 : Building Creation           : TEST FAILED...! :  \033[0m")
        print(f"\033[1;91m❌ TEST FAILED...! : Failed Building Creation \033[0m",create_building.text)









# 10 : Building : List ALL : 

    # print("\033[1;34mGet BUILDING LIST !\033[0m")
    building_list_all = requests.get(base_url + f"api/v1/masters/building/web/{company_id}/get-building-list",headers=headers)
    if building_list_all.status_code == 200 :
        build_json=building_list_all.json()
        # print("Building Listed Successfully..!")
        print(f"\033[92m✅ Test Case ID - 010 : Get Building List           : TEST PASSED...! \033[0m")
        print("Response JSON : ",json.dumps(build_json,indent=4))

    else:
        failed_count+=1
        # error_text=building_list_all.json()["errorMessage"]
        print(f"\033[91m❌ Test Case ID - 010 : Get Building List           : TEST FAILED...! :  \033[0m")
        # print("Building Listed Failed..!")






# # 11 : Buildng : Get Detailed List : 

    # print("\033[1;34mTESTING AREA DETAILED LIST !\033[0m")
    build_detailed_list = requests.get(base_url + f"api/v1/masters/building/web/{company_id}/get-building-list?buildingId={building_id}",headers=headers)
    if build_detailed_list.status_code == 200:
        build_detailed_list_json=build_detailed_list.json()
        # print("Building Detailed List Listed")
        print(f"\033[92m✅ Test Case ID - 011 : Get  Building detailed      : TEST PASSED...! \033[0m")
        print("Response JSON : ",json.dumps(build_detailed_list_json,indent=4))
    else:
        failed_count+=1
        # error_text=build_detailed_list.json()["errorMessage"]
        # print("Building Detailed Listed Failed",build_detailed_list.text,area_detailed_list.status_code)
        print(f"\033[91m❌ Test Case ID - 011 : Get  Building Detailed      : TEST FAILED...! :  \033[0m")







# 12 : Building : update :pending


    update_building_payload = {
        "name": "Block 3",
        "code": 224
    }

    building_update = requests.put(
        base_url + f"api/v1/masters/building/web/{company_id}/update-building/{building_id}",
        json=update_building_payload, 
        headers=headers
    )

    if building_update.status_code == 200:
        building_update_json = building_update.json()
        print(f"\033[92m✅ Test Case ID - 012 : Building Updated            : TEST PASSED...! \033[0m")
    else: 
        failed_count += 1
        # error_text=building_update.json()["errorMessage"]
        print(f"\033[91m❌ Test Case ID - 012 : Building Updated            : TEST FAILED...! :  \033[0m")





# 13 : Building : Delete : 



    building_delete = requests.patch(base_url + f"api/v1/masters/building/web/{company_id}/delete-building/{building_id}",headers=headers)
    if building_delete.status_code == 200 :
        # print("Building Deleted Successfully...!")
        print(f"\033[92m✅ Test Case ID - 013 : Delete Building             : TEST PASSED...! \033[0m")

    else: 
        failed_count+=1
        # error_text=building_delete.json()["errorMessage"]
        # print("Building Deleted failed...! ",building_delete.text) 
        print(f"\033[91m❌ Test Case ID - 013 : Delete Building             : TEST FAILED...! :  \033[0m")








# 17 :logout :  

response_logout = requests.put(logout_url,headers=headers) 
if response_logout.status_code == 200:
    logout_json = response_logout.json()
    # print("Response JSON:", json.dumps(logout_json, indent=4))
    # print(f"Token (Logout): {token}")
    print(f"\033[92m✅ Test Case ID - 012 : Logout                      : TEST PASSED...! \033[0m") # login success so test failed becoz in oms logged with oms in other 3 credentials kds,go,testoms

else:
    failed_count+=1
    # error_text=response_logout.json()["errorMessage"]
    # print(f"Logout failed with status code {response_logout.status_code}")
    # print("Response:", response_logout.json())
    print(f"\033[91m❌ Test Case ID - 012  : Logout                     :  TEST FAILED...!  \033[0m") # login failed so test passed









print(f"\033[1;34mTotal TEST FAILEDS  : {failed_count}/{total_count}\033[0m")

if failed_count == 0:
    print("\033[92m ✅ All TEST PASSED \033[0m")
