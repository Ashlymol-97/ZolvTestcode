import requests
import time
import json


print(f"\033[1;34m** ZOLV AREA TESTCODE **.\033[0m")


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
headers=None
# print("\033[1;34mTESTING LOGIN!\033[0m")
response_login = requests.post(login_url,json=login_payload)
if response_login.status_code == 200:
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




# 2 : Area : Create Parent :

    # print("\033[1;34mTESTING AREA CREATION !\033[0m")
    # print("\033[1;34mTESTING PARENT AREA CREATION !\033[0m")

    area_id =0
    create_parentarea_payload = {
        "name": "Hotels",
        "code":786,
        "areaType": "parent",
        "parentAreaId":"", #if choose child area in area type, parentarea id field is mandatory .
        "buildingId": "68709372293ae6389032a058",
        "floorId": "68709372293ae6389032a05a",
        "isActive": True,
        "moduleGroupId": "68709372293ae6389032a05b",
        "paymentModes": [
              {
                  "name": "paymentGateway",
                  "enabled": True
              },
              {
                  "name": "payOnDelivery",
                  "enabled": True
              },
              # // {
              # //     "name": "employeeCredit",
              # //     "enabled": false
              # // },
              {
                  "name": "roomCredit",
                  "enabled": True
              }
          ],
        "deliveryModes":[
              {
                  "name": "roomDelivery",
                  "enabled": True
              },
              {
                  "name": "takeAway",
                  "enabled": True
              },
              {
                  "name": "dineIn",
                  "enabled": True   
              }
          ],
        "preOrderStatus": False
        
    }
    create_parentarea = requests.post(base_url + f"api/v1/masters/area/web/{company_id}/create-area",json=create_parentarea_payload,headers=headers)
    if create_parentarea.status_code == 200:
        createparent_json=create_parentarea.json()
        area_id = createparent_json['id']

        # print("Parent Area Created Successfully..!",create_parentarea.text,area_id)
        # print("Response JSON : ",json.dumps(createparent_json,indent=4))
        print(f"\033[92m✅ Test Case ID - 002 : Area Creation (Parent)      : TEST PASSED...!  \033[0m")
    

    else:
        print(f"\033[91m❌ Test Case ID - 003 : Area Creation (Parent)       : TEST FAILED...! :   \033[0m")





# ******************************Time Delay *********************************************


    wait_time = int(input("Enter wait time in seconds: "))
    # Create area here...
    print("\033[38;5;208m⏳ Waiting \033[0m")
    # time.sleep(25)   # wait 3 seconds, adjust based on system behavior
    # print(time.sleep())
    # # Then delete area
    for remaining in range(wait_time, 0, -1):
      print(f"\033[38;5;208m\r⏳ Waiting... {remaining} seconds left\033[0m", end="")
      time.sleep(1)

    print("\033[38;5;208m\n✅ Done waiting!\033[0m") 




    
    # 3 : Area create Child area :

        # print("\033[1;34mTESTING CHILD AREA CREATION !\033[0m")
    child_area_id=None
    create_childarea_payload = {
        "name": "Third Floor",
        "code": 549,
        "areaType": "child",
        "parentAreaId":area_id, #if choose child area in area type, parentarea id field is mandatory .
        "buildingId": "68709372293ae6389032a058",
        "floorId": "68709372293ae6389032a05a",
        "isActive": True,
        "moduleGroupId": "68709372293ae6389032a05b",
        "paymentModes": [
            {
                "name": "paymentGateway",
                "enabled": True
            },
            {
                "name": "payOnDelivery",
                "enabled": True
            },
            # // {
            # //     "name": "employeeCredit",
            # //     "enabled": false
            # // },
            {
                "name": "roomCredit",
                "enabled": True
            }
        ],
        "deliveryModes":[
            {
                "name": "roomDelivery",
                "enabled": True
            },
            {
                "name": "takeAway",
                "enabled": True
            },
            {
                "name": "dineIn",
                "enabled": True
            }
        ],
        "preOrderStatus": True
        
    }

    create_childarea = requests.post(base_url + f"api/v1/masters/area/web/{company_id}/create-area",json=create_childarea_payload,headers=headers)
    if create_childarea.status_code == 200:
        createchild_json=create_childarea.json()
        print(f"\033[92m✅ Test Case ID - 003 : Area Creation (Child)       : TEST PASSED...! \033[0m")
        child_area_id = createchild_json['id']


        #   print("Child Area Created Successfully..!",create_childarea.text)
        # print("Response JSON : ",json.dumps(createchild_json,indent=4))

    else:
        failed_count+=1
        # error_text=create_childarea.json()["errorMessage"]

        print(f"\033[91m❌ Test Case ID - 003 : Area Creation (Child)       : TEST FAILED...! :   \033[0m")
        # print("Failed Creation.",create_childarea.text) 





# 4 : Area : List ALL : 

    # print("\033[1;34mGet Area List!\033[0m")
    area_list_all = requests.get(base_url + f"api/v1/masters/area/web/{company_id}/get-area-list",headers=headers)
    if area_list_all.status_code == 200 :
        list_json=area_list_all.json()
        # print("Response JSON : ",json.dumps(list_json,indent=4))
        # print("Area Listed Successfully..!")
        print(f"\033[92m✅ Test Case ID - 004 : Get Area List               : TEST PASSED...! \033[0m")

        # area_id_detailed=list_json['areas'][-1]['id']
        # area_id_parentdelete=list_json['areas'][-1]['id']
        # area_id_childdelete=list_json['areas'][-2]['id']
        # print(area_id_delete)

    else:
        failed_count+=1
        # error_text=area_list_all.json()["errorMessage"]
        print(f"\033[91m❌ Test Case ID - 004 : Get Area List               : TEST FAILED...! :  \033[0m")

        # print("Area Listed Failed..!")







# # 5 : Area : Get Detailed List : 

    # print("\033[1;34mTESTING AREA DETAILED LIST !\033[0m")
    area_detailed_list = requests.get(base_url + f"api/v1/masters/area/web/{company_id}/get-area/{area_id}",headers=headers)
    if area_detailed_list.status_code == 200:
        # print("Area Detailed List Listed")
        area_detailed_json=area_detailed_list.json()
        # print("Response JSON : ",json.dumps(area_detailed_json,indent=4))

        print(f"\033[92m✅ Test Case ID - 005 : Get Area Detailed           : TEST PASSED...! \033[0m")

    else:
        # error_text=area_detailed_list.json()["errorMessage"]
        failed_count+=1
        print(f"\033[91m❌ Test Case ID - 005 : Get Area Detailed           : TEST FAILED...! :  \033[0m")
        # print("Area Detailed Listed Failed",area_detailed_list.text)












# 7: Area : Child Area : Delete : 




    area_delete = requests.patch(base_url + f"api/v1/masters/area/web/{company_id}/delete-area/{child_area_id}",headers=headers)
    if area_delete.status_code == 200 :
        # print("Child Area Deleted Successfully...!")
        print(f"\033[92m✅ Test Case ID - 007 : Delete Area (Child)         : TEST PASSED...!  \033[0m")

    else: 
        failed_count+=1
        # error_text=area_delete.json()["errorMessage"]
        print(f"\033[91m❌ Test Case ID - 007 : Delete Area (Child)         : TEST FAILED...! :  \033[0m")
        # print("Child Area Deleted failed...!",area_delete.text) 









    # 8 : Area : Parent Area :  Delete :

    area_delete = requests.patch(base_url + f"api/v1/masters/area/web/{company_id}/delete-area/{area_id}",headers=headers)
    if area_delete.status_code == 200 :
        # print("Area Deleted Successfully...!")
        print(f"\033[92m✅ Test Case ID - 008 : Delete Area (Parent)        : TEST PASSED...!  \033[0m")

    else: 
        failed_count+=1
        # error_text=area_delete.json()["errorMessage"]
        print(f"\033[91m❌ Test Case ID - 008 : Delete Area (Parent)        : TEST FAILED...! :  \033[0m")
        # print("Area Deleted failed...!",area_delete.text) 



else:

    failed_count+=1
    error_text=response_login.json()["errorMessage"]
    print(f"\033[91m❌  Test Case ID - 001 : Login                      : TEST FAILED...! :   \033[0m")
    # print("Response:", response_login.json())





# 17 :logout :  

# response_logout = requests.put(logout_url,headers=headers) 
# if response_logout.status_code == 200:
#     logout_json = response_logout.json()
#     # print("Response JSON:", json.dumps(logout_json, indent=4))
#     # print(f"Token (Logout): {token}")
#     print(f"\033[92m✅ Test Case ID - 012 : Logout                      : TEST PASSED...! \033[0m") # login success so test failed becoz in oms logged with oms in other 3 credentials kds,go,testoms

# else:
#     failed_count+=1
#     # error_text=response_logout.json()["errorMessage"]
#     # print(f"Logout failed with status code {response_logout.status_code}")
#     # print("Response:", response_logout.json())
#     print(f"\033[91m❌ Test Case ID - 012  : Logout                     :  TEST FAILED...!  \033[0m") # login failed so test passed













print(f"\033[1;34mTotal TEST FAILEDS  : {failed_count}/{total_count}\033[0m")

if failed_count == 0:
    print("\033[92m ✅ All TEST PASSED \033[0m")







# # # 6 : Area : Update List : Pending

#     print("\033[1;34mTESTING AREA UPDATION !\033[0m")

#     update_area_payload = {
            
#             "name": "area",
#             "code": 80,
#             "areaType": "parent",
#             "parentAreaId": "68a6b1ba89c43b6512ea7925",
#             "buildingId": "68709372293ae6389032a058",
#             "floorId": "68709372293ae6389032a05a",
#             "isActive": True,
#             "moduleGroupId": "68709372293ae6389032a05b",
#             "paymentModes": [
#                 {
#                     "name": "paymentGateway",
#                     "enabled": True
#                 },
#                 {
#                     "name": "payOnDelivery",
#                     "enabled": True
#                 },
#                 {
#                     "name": "roomCredit",
#                     "enabled": True
#                 }
#             ],
#             "deliveryModes": [
#                 {
#                     "name": "roomDelivery",
#                     "enabled": True
#                 },
#                 {
#                     "name": "takeAway",
#                     "enabled": True
#                 },
#                 {
#                     "name": "dineIn",
#                     "enabled": True
#                 }
#             ],
#             "preOrderStatus":True,
#             "qrKey": "57463274",
#             "qrImage": "https://omniapictures.s3.ap-south-1.amazonaws.com/qrCodes/68a6b1ba89c43b6512ea7925.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20250821T070818Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=AKIA2MVKJRWJKAZW67NQ%2F20250821%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Signature=c551179ce8dad1230a09e0e48109078e51b8a3de2f63be764a2e5b8fbf4b6357",
#             "languageId": "686f510c6e7e978b9132a03e"
#         }

#     print("\033[1;34mTESTING AREA UPDATED LIST !\033[0m")
#     area_update = requests.put(base_url + f"api/v1/masters/area/web/{company_id}/update-area/68a6b1ba89c43b6512ea7925",json=update_area_payload,headers=headers)
#     if area_update.status_code == 200 :
#         print("Area Updated Successfully..!")
#     else:
#         print("Area Updated Failed...! ",area_update.text,area_update.status_code)










