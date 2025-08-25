import requests
import time
import json
import random
import urllib.parse

import base64
import hashlib

print(f"\033[1;34m** ZOLV ADMIN TESTCODE **.\033[0m")


base_url= "https://qa-admin.zolv.health/"
login_url= "https://qa-admin.zolv.health/api/v1/user/login"
logout_url="https://qa-admin.zolv.health/api/v1/user/logout"



login_payload = {
    "loginId": "AutotestAdmin",
    "password": "Smm@1234"
}


failed_count=0
total_count=12
    
# Login : 

# print("\033[1;34mTESTING LOGIN!\033[0m")
response_login = requests.post(login_url,json=login_payload)
if response_login.status_code != 200:
    failed_count+=1
    print(f"\033[91m❌  Test Case ID - 001 : TEST FAILED...! : Invalid Credentials : Login \033[0m")
    # print("Response:", response_login.json())
else:
    response_json = response_login.json()
    # print(f"Login Successfull   with status code {response_login.status_code}",login_payload)

    # print("Response JSON : ",json.dumps(response_json,indent=4))
    token= response_json.get('token',{}).get('token')
    company_id=response_json['company']['id']
    print(f"\033[92m✅ Test Case ID - 001 : TEST PASSED...! : Login \033[0m")
    headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
    }
    # print(f"Token (Login): {token}") 





# 1 : Area : Create Parent :

    # print("\033[1;34mTESTING AREA CREATION !\033[0m")
    # print("\033[1;34mTESTING PARENT AREA CREATION !\033[0m")


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
      
    #   print("Parent Area Created Successfully..!",create_parentarea.text)
    #    print("Response JSON : ",json.dumps(createparent_json,indent=4))
       print(f"\033[92m✅ Test Case ID - 002 : TEST PASSED...! :  Area Creation (Parent) \033[0m")
    else:
       failed_count+=1

       print(f"\033[91m❌ Test Case ID - 002 : TEST FAILED...! : Invalid data or missing fields :  Area Creation (Parent) \033[0m")
 
    #    print("Failed Creation.",create_parentarea.text) 





   

# 3 : Area create Child area :

    # print("\033[1;34mTESTING CHILD AREA CREATION !\033[0m")

    create_childarea_payload = {
        "name": "First Floors",
        "code": 579,
        "areaType": "child",
        "parentAreaId":"68a5af7a03cfe84816ecd0d7", #if choose child area in area type, parentarea id field is mandatory .
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
       print(f"\033[92m✅ Test Case ID - 003 : TEST PASSED...! :  Area Creation (Child) \033[0m")
    #   area_id = createparent_json.get('area', {}).get('id')
    #   print(area_id)

    #   print("Child Area Created Successfully..!",create_childarea.text)
      # print("Response JSON : ",json.dumps(createchild_json,indent=4))

    else:
       failed_count+=1
       print(f"\033[91m❌  Test Case ID - 003 : TEST FAILED...! : Invalid data or missing fields :  Area Creation (Child) \033[0m")
    #   print("Failed Creation.",create_childarea.text) 





# 3 : Area : List ALL : 

    # print("\033[1;34mGet Area List!\033[0m")
    area_list_all = requests.get(base_url + f"api/v1/masters/area/web/{company_id}/get-area-list",headers=headers)
    if area_list_all.status_code == 200 :
        list_json=area_list_all.json()
        # print("Response JSON : ",json.dumps(list_json,indent=4))
        # print("Area Listed Successfully..!")
        print(f"\033[92m✅ Test Case ID - 004 : TEST PASSED...! : Get Area List  \033[0m")

        area_id_detailed=list_json['areas'][0]['id']
        area_id_delete=list_json['areas'][-1]['id']
        # print(area_id_delete)

    else:
        failed_count+=1
        print(f"\033[91m❌  Test Case ID - 004 : TEST FAILED...! : Invalid Request : Get Area List\033[0m")

        # print("Area Listed Failed..!")





# # 4 : Area : Get Detailed List : 

    # print("\033[1;34mTESTING AREA DETAILED LIST !\033[0m")
    area_detailed_list = requests.get(base_url + f"api/v1/masters/area/web/{company_id}/get-area/{area_id_detailed}",headers=headers)
    if area_detailed_list.status_code == 200:
        # print("Area Detailed List Listed")
        area_detailed_json=area_detailed_list.json()
        # print(area_detailed_json)
        print(f"\033[92m✅ Test Case ID - 005 : TEST PASSED...! : Get Area \033[0m")

    else:
        failed_count+=1
        print(f"\033[91m❌ Test Case ID - 005 : TEST FAILED...! : Invalid Input : Get Area \033[0m")
        # print("Area Detailed Listed Failed",area_detailed_list.text)








# # # 5 : Area : Update List : Pending

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






# 6 : Area : Delete :

    area_delete = requests.patch(base_url + f"api/v1/masters/area/web/{company_id}/delete-area/{area_id_delete}",headers=headers)
    if area_delete.status_code == 200 :
        # print("Area Deleted Successfully...!")
        print(f"\033[92m✅  Test Case ID - 007  : TEST PASSED...! : Delete Area \033[0m")

    else: 
        failed_count+=1
        print(f"\033[91m❌ Test Case ID - 007 :  TEST FAILED...! : Invalid request or area ID : Delete Area \033[0m")
        # print("Area Deleted failed...!",area_delete.text) 













# **************************Building *********************************




# 7 : : Building : Create :

    # print("\033[1;34mTESTING BUILDING CREATION !\033[0m")
    create_building_payload = {
      "name": "Thejaswini",
      "code": 224
    }


    create_building = requests.post(base_url + f"api/v1/masters/building/web/{company_id}/create-building",json=create_building_payload,headers=headers)
    if create_building.status_code == 201:
        # print("Create Building Successfully..!")
        print(f"\033[92m✅ Test Case ID - 008 : TEST PASSED...! :  Building Creation \033[0m")

    else:
        failed_count+=1
        print(f"\033[91m❌ Test Case ID - 008 : TEST FAILED...! : Invalid data or missing fields :  Building Creation \033[0m")
        # print(f"\033[1;91m❌ TEST FAILED...! : Failed Building Creation \033[0m",create_building.text)






# 8 : Building : List ALL : 

    # print("\033[1;34mGet BUILDING LIST !\033[0m")
    building_list_all = requests.get(base_url + f"api/v1/masters/building/web/{company_id}/get-building-list",headers=headers)
    if building_list_all.status_code == 200 :
        build_json=building_list_all.json()
        # print("Response JSON : ",json.dumps(build_json,indent=4))
        # print("Building Listed Successfully..!")
        print(f"\033[92m✅  Test Case ID - 009 :  TEST PASSED...! :  Get Building List \033[0m")

        building_id_detailed=build_json['buildings'][0]['id']
        building_id_delete=build_json['buildings'][-1]['id']
        # print(building_id)

    else:
        failed_count+=1
        print(f"\033[91m❌  Test Case ID - 009 :  TEST FAILED...! : Invalid Request :  Get Building List \033[0m")
        # print("Building Listed Failed..!")




# # 9 : Buildng : Get Detailed List : 

    # print("\033[1;34mTESTING AREA DETAILED LIST !\033[0m")
    area_detailed_list = requests.get(base_url + f"api/v1/masters/building/web/{company_id}/get-building-list?{building_id_detailed}",headers=headers)
    if area_detailed_list.status_code == 200:
        # print("Building Detailed List Listed")
        print(f"\033[92m✅ Test Case ID - 010 : TEST PASSED...! : Get Building List \033[0m")
        # print(area_detailed_json)
    else:
        failed_count+=1
        # print("Building Detailed Listed Failed",area_detailed_list.text,area_detailed_list.status_code)
        print(f"\033[91m❌ Test Case ID - 010 : TEST FAILED...! : Invalid Input : Get Building List \033[0m")




# 10 : Building : update :pending









# 11 : Building : Delete : 



    building_delete = requests.patch(base_url + f"api/v1/masters/building/web/{company_id}/delete-building/{building_id_delete}",headers=headers)
    if building_delete.status_code == 200 :
        # print("Building Deleted Successfully...!")
        print(f"\033[92m✅  Test Case ID - 011  :  TEST PASSED...! : \033[0m")

    else: 
        failed_count+=1
        # print("Building Deleted failed...! ",building_delete.text) 
        print(f"\033[91m❌  Test Case ID - 011  : TEST FAILED...! : Invalid request or area ID : Delete Building \033[0m")














# ********************************************************Floor *******************************************



# 13 : Create Floor : 

    floor_payload={
    "name": "second floor",
    "code": 14,
    "buildingId": "68709372293ae6389032a058"
    }
    create_floor = requests.post(base_url + f"api/v1/masters/floor/web/{company_id}/create-floor",json=floor_payload,headers=headers)
    if create_floor.status_code == 201:
       create_floor_json=create_floor.json()
      
    #   print("Floor  Created Successfully..!",create_floor.text)
    #    print("Response JSON : ",json.dumps(create_floor_json,indent=4))
       print(f"\033[92m✅ Test Case ID - 013  :  TEST PASSED...! : Floor Creation \033[0m")
    else:
       failed_count+=1

       print(f"\033[91m❌ Test Case ID - 013  :  TEST FAILED...! : Invalid data or missing fields : Floor Creation \033[0m")
 
    #    print("Failed Creation.",create_floor.text) 









# 14 : Floor : List ALL : 

    # print("\033[1;34mGet Area List!\033[0m")
    floor_list_all = requests.get(base_url + f"api/v1/masters/floor/web/{company_id}/get-floor-list",headers=headers)
    if floor_list_all.status_code == 201 :
        floor_list_json=floor_list_all.json()
        # print("Response JSON : ",json.dumps(floor_list_json,indent=4))
        # print("Floor Listed Successfully..!")
        print(f"\033[92m✅ Test Case ID - 014  :  TEST PASSED...! :  Get Floor List \033[0m")

        floor_id_detailed=floor_list_json['floors'][0]['id']
        floor_id=floor_list_json['floors'][-1]['id']
        # print(floor_id_detailed)

    else:
        failed_count+=1
        print(f"\033[91m❌ Test Case ID - 014  :  TEST FAILED...! : Invalid Request : Get Floor List \033[0m")

        # print("Floor Listed Failed..!",floor_list_all.text)







# # 15 : Floor : Get Detailed List : 

    # print("\033[1;34mTESTING AREA DETAILED LIST !\033[0m")
    floor_detailed_list = requests.get(base_url + f"api/v1/masters/floor/web/{company_id}/get-floor-list?{floor_id_detailed}",headers=headers)
    if floor_detailed_list.status_code == 201:
        # print("Floor Detailed List Listed")
        floor_detailed_json=floor_detailed_list.json()

        # print("Response JSON : ",json.dumps(floor_detailed_json,indent=4))

        # print(floor_detailed_json)
        print(f"\033[92m✅ Test Case ID - 005  :  TEST PASSED...! : Get Detailed list \033[0m")

    else:
        failed_count+=1
        print(f"\033[91m❌ Test Case ID - 005  :  TEST FAILED...! : Invalid Input : Get Detailed list \033[0m")
        # print("Floor Detailed Listed Failed",floor_detailed_list.text)














# # logout :  

# response_logout = requests.put(logout_url,headers=headers) 
# if response_logout.status_code == 200:
#     logout_json = response_logout.json()
#     # print("Response JSON:", json.dumps(logout_json, indent=4))
#     print(f"Token (Logout): {token}")
#     print(f"\033[92m✅ Test Case ID - 012 : TEST PASSED...! : Logout \033[0m") # login success so test failed becoz in oms logged with oms in other 3 credentials kds,go,testoms

# else:
#     failed_count+=1
#     # print(f"Logout failed with status code {response_logout.status_code}")
#     # print("Response:", response_logout.json())
#     print(f"\033[91m❌ Test Case ID - 012  :  TEST FAILED...! :  Error - Invalid or expired session token.  : Logout \033[0m") # login failed so test passed









print(f"\033[1;34mTotal TEST FAILEDS  : {failed_count}/{total_count}\033[0m")

if failed_count == 0:
    print("\033[92m ✅ All TEST PASSED \033[0m")
