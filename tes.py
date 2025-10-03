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
total_count=23
    
# 1 : Login : 
# print("\033[1;34mTESTING LOGIN!\033[0m")
response_login = requests.post(login_url,json=login_payload)
if response_login.status_code != 200:
    failed_count+=1
    print(f"\033[91m❌  Test Case ID - 001 : Login                      : TEST FAILED...! : Invalid Credentials  \033[0m")
    # print("Response:", response_login.json())
else:
    response_json = response_login.json()
    # print(f"Login Successfull   with status code {response_login.status_code}",login_payload)

    # print("Response JSON : ",json.dumps(response_json,indent=4))
    token= response_json.get('token',{}).get('token')
    company_id=response_json['company']['id']
    print(f"\033[92m✅ Test Case ID - 001 : Login                       : TEST PASSED...!  \033[0m")
    header = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
    }
    print(f"Token (Login): {token}") 





# 2 : Area : Create Parent :

    # print("\033[1;34mTESTING AREA CREATION !\033[0m")
    # print("\033[1;34mTESTING PARENT AREA CREATION !\033[0m")

    area_id =None
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
    create_parentarea = requests.post(base_url + f"api/v1/masters/area/web/{company_id}/create-area",json=create_parentarea_payload,headers=header)
    if create_parentarea.status_code == 200:
        createparent_json=create_parentarea.json()
        area_id = createparent_json['id']

        # area_detailed_list = requests.get(base_url + f"api/v1/masters/area/web/{company_id}/get-area/{area_id}",headers=header)
        # if area_detailed_list.status_code == 200:
           
        #     area_detailed_list_json=area_detailed_list.json()
        #     # area_name=createparent_json.get('name')

            #    print("Parent Area Created Successfully..!",create_parentarea.text,area_id)
            # print("Response JSON : ",json.dumps(createparent_json,indent=4))
        print(f"\033[92m✅ Test Case ID - 002 : Area Creation (Parent)      : TEST PASSED...!  \033[0m")
    else:
        failed_count+=1

        print(f"\033[91m❌ Test Case ID - 002 : Area Creation (Parent)      : TEST FAILED...! : Invalid data or missing fields  \033[0m")
    
        print("Failed Creation.",create_parentarea.text) 








# ******************************Time Delay *********************************************
    
    wait_time = 15
    # Create area here...
    print("\033[38;5;208m⏳ Waiting for Area to be available in frontend...\033[0m")
    # time.sleep(25)   # wait 3 seconds, adjust based on system behavior
    # print(time.sleep())
    # # Then delete area
    for remaining in range(wait_time, 0, -1):
        print(f"\033[38;5;208m\r⏳ Waiting... {remaining} seconds left\033[0m", end="")
        time.sleep(1)

    print("\033[38;5;208m\n✅ Done waiting!\033[0m") 


   

# 3 : Area create Child area :

    # print("\033[1;34mTESTING CHILD AREA CREATION !\033[0m")
    child_area_id=0
    create_childarea_payload = {
        "name": "Third Floor",
        "code": 574,
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

    create_childarea = requests.post(base_url + f"api/v1/masters/area/web/{company_id}/create-area",json=create_childarea_payload,headers=header)
    if create_childarea.status_code == 200:
       createchild_json=create_childarea.json()
       print(f"\033[92m✅ Test Case ID - 003 : Area Creation (Child)       : TEST PASSED...! \033[0m")
       child_area_id = createchild_json['id']


    #   print("Child Area Created Successfully..!",create_childarea.text)
      # print("Response JSON : ",json.dumps(createchild_json,indent=4))

    else:
       failed_count+=1
       print(f"\033[91m❌ Test Case ID - 003 : Area Creation (Child)       : TEST FAILED...! : Invalid data or missing fields  \033[0m")
       print("Failed Creation.",create_childarea.text) 




# 4 : Area : List ALL : 

    # print("\033[1;34mGet Area List!\033[0m")
    area_list_all = requests.get(base_url + f"api/v1/masters/area/web/{company_id}/get-area-list",headers=header)
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
        print(f"\033[91m❌ Test Case ID - 004 : Get Area List               : TEST FAILED...! : Invalid Request \033[0m")

        print("Area Listed Failed..!",area_list_all.status_code)







# # 5 : Area : Get Detailed List : 

    # print("\033[1;34mTESTING AREA DETAILED LIST !\033[0m")
    area_detailed_list = requests.get(base_url + f"api/v1/masters/area/web/{company_id}/get-area/{area_id}",headers=header)
    if area_detailed_list.status_code == 200:
        # print("Area Detailed List Listed")
        area_detailed_json=area_detailed_list.json()
        # print("Response JSON : ",json.dumps(area_detailed_json,indent=4))

        print(f"\033[92m✅ Test Case ID - 005 : Get Area Detailed           : TEST PASSED...! \033[0m")

    else:
        failed_count+=1
        print(f"\033[91m❌ Test Case ID - 005 : Get Area Detailed           : TEST FAILED...! : Invalid Input \033[0m")
        print("Area Detailed Listed Failed",area_detailed_list.status_code)








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







# 7: Area : Child Area : Delete : 




    area_delete = requests.patch(base_url + f"api/v1/masters/area/web/{company_id}/delete-area/{child_area_id}",headers=header)
    if area_delete.status_code == 200 :
        # print("Child Area Deleted Successfully...!")
        print(f"\033[92m✅ Test Case ID - 007 : Delete Area (Child)         : TEST PASSED...!  \033[0m")

    else: 
        failed_count+=1
        print(f"\033[91m❌ Test Case ID - 007 : Delete Area (Child)         : TEST FAILED...! : Invalid request or area ID \033[0m")
        print("Child Area Deleted failed...!",area_delete.status_code) 









# 8 : Area : Parent Area :  Delete :

    area_delete = requests.patch(base_url + f"api/v1/masters/area/web/{company_id}/delete-area/{area_id}",headers=header)
    if area_delete.status_code == 200 :
        # print("Area Deleted Successfully...!")
        print(f"\033[92m✅ Test Case ID - 008 : Delete Area (Parent)        : TEST PASSED...!  \033[0m")

    else: 
        failed_count+=1
        print(f"\033[91m❌ Test Case ID - 008 : Delete Area (Parent)        : TEST FAILED...! : Invalid request or area ID \033[0m")
        print("Area Deleted failed...!",area_delete.status_code) 












# **************************Building *********************************




    # 9 : : Building : Create :
    building_id=None
    # print("\033[1;34mTESTING BUILDING CREATION !\033[0m")
    create_building_payload = {
        "name": "Thejaswini",
        "code": 226
    }


    create_building = requests.post(base_url + f"api/v1/masters/building/web/{company_id}/create-building",json=create_building_payload,headers=header)
    if create_building.status_code == 201:
        building_id_json=create_building.json()
        building_id = building_id_json['id']
        print(building_id)
        print("Response JSON : ",json.dumps(building_id_json,indent=4))
        # print("Create Building Successfully..!")
        print(f"\033[92m✅ Test Case ID - 009 : Building Creation           : TEST PASSED...! \033[0m")

    else:
        failed_count+=1
        print(f"\033[91m❌ Test Case ID - 009 : Building Creation           : TEST FAILED...! : Invalid data or missing fields \033[0m")
        print(f"\033[1;91m❌ TEST FAILED...! : Failed Building Creation \033[0m",create_building.status_code)







# # ******************************Time Delay *********************************************








# # 10 : Building : List ALL : 

    # print("\033[1;34mGet BUILDING LIST !\033[0m")
    building_list_all = requests.get(base_url + f"api/v1/masters/building/web/{company_id}/get-building-list",headers=header)
    if building_list_all.status_code == 200 :
        build_json=building_list_all.json()
        # print("Building Listed Successfully..!")
        print(f"\033[92m✅ Test Case ID - 010 : Get Building List           : TEST PASSED...! \033[0m")
        print("Response JSON : ",json.dumps(build_json,indent=4))

    else:
        failed_count+=1
        print(f"\033[91m❌ Test Case ID - 010 : Get Building List           : TEST FAILED...! : Invalid Request \033[0m")
        print("Building Listed Failed..!",building_list_all.status_code)






# # # 11 : Buildng : Get Detailed List : 

#     # print("\033[1;34mTESTING AREA DETAILED LIST !\033[0m")
#     area_detailed_list = requests.get(base_url + f"api/v1/masters/building/web/{company_id}/get-building-list?buildingId={building_id}",headers=header)
#     if area_detailed_list.status_code == 200:
#         area_detailed_json=area_detailed_list.json()
#         # print("Building Detailed List Listed")
#         print(f"\033[92m✅ Test Case ID - 011 : Get  Building detailed      : TEST PASSED...! \033[0m")
#         print("Response JSON : ",json.dumps(area_detailed_json,indent=4))
#     else:
#         failed_count+=1
#         # print("Building Detailed Listed Failed",area_detailed_list.text,area_detailed_list.status_code)
#         print(f"\033[91m❌ Test Case ID - 011 : Get  Building Detailed      : TEST FAILED...! : Invalid Input \033[0m")







# # 12 : Building : update :pending


#     update_building_payload = {
#         "name": "Block 3",
#         "code": 224
#     }

#     building_update = requests.put(
#         base_url + f"api/v1/masters/building/web/{company_id}/update-building/{building_id}",
#         json=update_building_payload, 
#         headers=headers
#     )

#     if building_update.status_code == 200:
#         building_update_json = building_update.json()
#         print(f"\033[92m✅ Test Case ID - 012 : Building Updated            : TEST PASSED...! \033[0m")
#     else: 
#         failed_count += 1
#         print(f"\033[91m❌ Test Case ID - 012 : Building Updated            : TEST FAILED...! : Invalid Input \033[0m")
#         print(building_update)








# # 13 : Building : Delete : 



#     building_delete = requests.patch(base_url + f"api/v1/masters/building/web/{company_id}/delete-building/{building_id}",headers=header)
#     if building_delete.status_code == 200 :
#         # print("Building Deleted Successfully...!")
#         print(f"\033[92m✅ Test Case ID - 013 : Delete Building             : TEST PASSED...! \033[0m")

#     else: 
#         failed_count+=1
#         print("Building Deleted failed...! ",building_delete.text) 
#         print(f"\033[91m❌ Test Case ID - 013 : Delete Building             : TEST FAILED...! : Invalid request or area ID \033[0m")














# # ********************************************************Floor *******************************************



# # 14 : Create Floor : 
#     floor_id=None
#     floor_payload={
#     "name": "second floor",
#     "code": 14,
#     "buildingId": "68709372293ae6389032a058"
#     }
#     create_floor = requests.post(base_url + f"api/v1/masters/floor/web/{company_id}/create-floor",json=floor_payload,headers=header)
#     if create_floor.status_code == 201:
#        create_floor_json=create_floor.json()
#        floor_id = create_floor_json['id']
#     #   print("Floor  Created Successfully..!",create_floor.text)
#     #    print("Response JSON : ",json.dumps(create_floor_json,indent=4))
#        print(f"\033[92m✅ Test Case ID - 014 : Floor Creation              : TEST PASSED...! \033[0m")
#     else:
#        failed_count+=1

#        print(f"\033[91m❌ Test Case ID - 014 : Floor Creation              : TEST FAILED...! : Invalid data or missing fields \033[0m")
 
#        print("Failed Creation.",create_floor.text) 








# # ******************************Time Delay *********************************************


 


# # 15 : Floor : List ALL : 

#     # print("\033[1;34mGet Area List!\033[0m")
#     floor_list_all = requests.get(base_url + f"api/v1/masters/floor/web/{company_id}/get-floor-list",headers=header)
#     if floor_list_all.status_code == 201 :
#         floor_list_json=floor_list_all.json()
#         # print("Response JSON : ",json.dumps(floor_list_json,indent=4))
#         # print("Floor Listed Successfully..!")
#         print(f"\033[92m✅ Test Case ID - 015 : Get Floor List              : TEST PASSED...! \033[0m")

#         # floor_id_detailed=floor_list_json['floors'][-1]['id']
#         # floor_id_delete=floor_list_json['floors'][-1]['id']
#         # print(floor_id_detailed)

#     else:
#         failed_count+=1
#         print(f"\033[91m❌ Test Case ID - 015 : Get Floor List              : TEST FAILED...! : Invalid Request \033[0m")

#         print("Floor Listed Failed..!",floor_list_all.text)

 





# # # 16 : Floor : Get Detailed List : 

#     # print("\033[1;34mTESTING AREA DETAILED LIST !\033[0m")
#     floor_detailed_list = requests.get(base_url + f"api/v1/masters/floor/web/{company_id}/get-floor-list?floorId={floor_id}",headers=header)
#     if floor_detailed_list.status_code == 201:
#         # print("Floor Detailed List Listed")
#         floor_detailed_json=floor_detailed_list.json()
#         print(f"\033[92m✅ Test Case ID - 016 : Get  Floor  Detailed        : TEST PASSED...! \033[0m")
#         # print("Response JSON : ",json.dumps(floor_detailed_json,indent=4))

#     else:
#         failed_count+=1
#         print(f"\033[91m❌ Test Case ID - 016 : Get  Floor  Detailed        : TEST FAILED...! : Invalid Input \033[0m")
#         print("Floor Detailed Listed Failed",floor_detailed_list.text)





# # 17 : Floor : Update :  


#     update_floor_payload = {
#         "name": "second floor",
#         "code": 14,
#         "buildingId": "68709372293ae6389032a058"
#     }

#     floor_update = requests.put(
#         base_url + f"api/v1/masters/floor/web/{company_id}/update-floor/{floor_id}",
#         json=update_floor_payload,  # Corrected here
#         headers=headers
#     )

#     if floor_update.status_code == 201:
#         floor_update_json = floor_update.json()
#         print(f"\033[92m✅ Test Case ID - 017 : Floor Updated               : TEST PASSED...! \033[0m")
#     else: 
#         failed_count += 1
#         print(f"\033[91m❌ Test Case ID - 017 : Floor Updated               : TEST FAILED...! : Invalid Input \033[0m")
#         print(floor_update.text)







# # # 18 : Floor  :  Delete :

#     floor_delete = requests.patch(base_url + f"api/v1/masters/floor/web/{company_id}/delete-floor/{floor_id}",headers=header)
#     if floor_delete.status_code == 200 :
#         # print("Floor Deleted Successfully...!")
#         print(f"\033[92m✅ Test Case ID - 018 : Floor Deleted               : TEST PASSED...!  \033[0m")

#     else: 
#         failed_count+=1
#         print(f"\033[91m❌ Test Case ID - 018 : Floor Deleted               : TEST FAILED...! : Invalid request or area ID \033[0m")
#         print("Floor Deleted failed...!",floor_delete.text) 







# #*********************************************************Departments*****************************************************







# # 19 : Create Department : 

#     # print("\033[1;34mGet Department List!\033[0m")
#     department_id=0
#     department_payload={
#         "name": "Dep Test",
#         "isActive": True
#     }
#     create_department = requests.post(base_url + f"api/v1/masters/department/web/{company_id}/create-department",json=department_payload,headers=header)
#     if create_department.status_code == 201:
#        create_department_json=create_department.json()
#        department_id = create_department_json['id']
#     #    print(department_id)

      
#     #   print("Department  Created Successfully..!",create_department.text)
#     #    print("Response JSON : ",json.dumps(create_department_json,indent=4))
#        print(f"\033[92m✅ Test Case ID - 019 : Department Creation         : TEST PASSED...! \033[0m")
#     else:
#        failed_count+=1

#        print(f"\033[91m❌ Test Case ID - 019 : Department Creation         : TEST FAILED...! : Invalid data or missing fields \033[0m")
 
#        print("Failed Creation.",create_department.text) 







# # ******************************Time Delay *********************************************

    




# # 20 : Department : List ALL : 

#     # print("\033[1;34mGet Department List!\033[0m")
#     dep_list_all = requests.get(base_url + f"api/v1/masters/area/web/{company_id}/get-area-list",headers=headers)
#     if dep_list_all.status_code == 200 :
#         dep_json=dep_list_all.json()
#         # print("Response JSON : ",json.dumps(dep_json,indent=4))
#         # print("Department Listed Successfully..!",dep_list_all.text)
#         print(f"\033[92m✅ Test Case ID - 020 : Get Department List         : TEST PASSED...! \033[0m")


#     else:
#         failed_count+=1
#         print(f"\033[91m❌ Test Case ID - 020 : Get Department List         : TEST FAILED...! : Invalid Request \033[0m")
#         print("Department Listed Failed..!",dep_list_all.text)







# # # 21 : Department : Get Detailed List : 

#     # print("\033[1;34mTESTING Department DETAILED LIST !\033[0m")
#     dep_detailed_list = requests.get(base_url + f"api/v1/masters/department/web/{company_id}/get-department-list?departmentId={department_id}",headers=header)
#     if dep_detailed_list.status_code == 200:
#         # print("Floor Detailed  ")
#         dep_detailed_json=dep_detailed_list.json()
#         print(f"\033[92m✅ Test Case ID - 021 : Get  Floor Detailed         : TEST PASSED...! \033[0m")
#         # print("Response JSON : ",json.dumps(dep_detailed_json,indent=4))

#     else:
#         failed_count+=1
#         print(f"\033[91m❌ Test Case ID - 021 : Get  Floor  Detailed        : TEST FAILED...! : Invalid Input \033[0m")
#         # print("Floor Detailed  Failed",dep_detailed_list.text)






       
# # 22 : Department : Update :  


#     update_dep_payload = {
#         "name": "Department test",
#         "isActive": True
#     }

#     dep_update = requests.put(
#         base_url + f"api/v1/masters/department/web/{company_id}/update-department/{department_id}",
#         json=update_dep_payload,  # Corrected here
#         headers=headers
#     )

#     if dep_update.status_code == 200:
#         dep_update_json = dep_update.json()
#         print(f"\033[92m✅ Test Case ID - 022 : Department Updated          : TEST PASSED...! \033[0m")
#     else: 
#         failed_count += 1
#         print(f"\033[91m❌ Test Case ID - 022 : Department Updated          : TEST FAILED...! : Invalid Input \033[0m")





#  # 23 : Department  :  Delete :

#     dep_delete = requests.patch(base_url + f"api/v1/masters/department/web/{company_id}/delete-department/{department_id}",headers=header)
#     if dep_delete.status_code == 200 :
#         # print("Department Deleted Successfully...!")
#         print(f"\033[92m✅ Test Case ID - 023 : Department Deleted          : TEST PASSED...!  \033[0m")

#     else: 
#         failed_count+=1
#         print(f"\033[91m❌ Test Case ID - 023 : Department Deleted          : TEST FAILED...! : Invalid request or area ID \033[0m")
#         print("Department Deleted failed...!",dep_delete.text) 









# # 17 :logout :  

# response_logout = requests.put(logout_url,headers=header) 
# if response_logout.status_code == 200:
#     logout_json = response_logout.json()
#     # print("Response JSON:", json.dumps(logout_json, indent=4))
#     # print(f"Token (Logout): {token}")
#     print(f"\033[92m✅ Test Case ID - 012 : Logout                      : TEST PASSED...! \033[0m") # login success so test failed becoz in oms logged with oms in other 3 credentials kds,go,testoms

# else:
#     failed_count+=1
#     # print(f"Logout failed with status code {response_logout.status_code}")
#     # print("Response:", response_logout.json())
#     print(f"\033[91m❌ Test Case ID - 012  : Logout                     :  TEST FAILED...! :  Error - Invalid or expired session token. \033[0m") # login failed so test passed









print(f"\033[1;34mTotal TEST FAILEDS  : {failed_count}/{total_count}\033[0m")

if failed_count == 0:
    print("\033[92m ✅ All TEST PASSED \033[0m")