



# # **************************Building *********************************




# # 9 : : Building : Create :
#     building_id=None
#     # print("\033[1;34mTESTING BUILDING CREATION !\033[0m")
#     create_building_payload = {
#       "name": "Thejaswini",
#       "code": 224
#     }


#     create_building = requests.post(base_url + f"api/v1/masters/building/web/{company_id}/create-building",json=create_building_payload,headers=headers)
#     if create_building.status_code == 201:
#         building_json=create_building.json()
#         building_id = building_json['id']
#         print(building_id)
#         print("Response JSON : ",json.dumps(building_json,indent=4))
#         # print("Create Building Successfully..!")
#         print(f"\033[92m✅ Test Case ID - 009 : Building Creation           : TEST PASSED...! \033[0m")

#     else:
#         failed_count+=1
#         # error_text=create_building.json()["errorMessage"]
#         print(f"\033[91m❌ Test Case ID - 009 : Building Creation           : TEST FAILED...! :  \033[0m")
#         print(f"\033[1;91m❌ TEST FAILED...! : Failed Building Creation \033[0m",create_building.text)







# # ******************************Time Delay *********************************************


#     # wait_time = int(input("Enter wait time in seconds: "))

#     # print("\033[38;5;208m⏳ Waiting for Area to be available in frontend...\033[0m")

#     # # Countdown loop
#     # for remaining in range(wait_time, 0, -1):
#     #     print(f"\033[38;5;208m\r⏳ Waiting... {remaining} seconds left\033[0m", end="")
#     #     time.sleep(1)

#     # print("\033[38;5;208m\n✅ Done waiting!\033[0m")









# # 10 : Building : List ALL : 

#     # print("\033[1;34mGet BUILDING LIST !\033[0m")
#     building_list_all = requests.get(base_url + f"api/v1/masters/building/web/{company_id}/get-building-list",headers=headers)
#     if building_list_all.status_code == 200 :
#         build_json=building_list_all.json()
#         # print("Building Listed Successfully..!")
#         print(f"\033[92m✅ Test Case ID - 010 : Get Building List           : TEST PASSED...! \033[0m")
#         print("Response JSON : ",json.dumps(build_json,indent=4))

#     else:
#         failed_count+=1
#         # error_text=building_list_all.json()["errorMessage"]
#         print(f"\033[91m❌ Test Case ID - 010 : Get Building List           : TEST FAILED...! :  \033[0m")
#         # print("Building Listed Failed..!")






# # # 11 : Buildng : Get Detailed List : 

#     # print("\033[1;34mTESTING AREA DETAILED LIST !\033[0m")
#     build_detailed_list = requests.get(base_url + f"api/v1/masters/building/web/{company_id}/get-building-list?buildingId={building_id}",headers=headers)
#     if build_detailed_list.status_code == 200:
#         build_detailed_list_json=build_detailed_list.json()
#         # print("Building Detailed List Listed")
#         print(f"\033[92m✅ Test Case ID - 011 : Get  Building detailed      : TEST PASSED...! \033[0m")
#         print("Response JSON : ",json.dumps(build_detailed_list_json,indent=4))
#     else:
#         failed_count+=1
#         # error_text=build_detailed_list.json()["errorMessage"]
#         # print("Building Detailed Listed Failed",build_detailed_list.text,area_detailed_list.status_code)
#         print(f"\033[91m❌ Test Case ID - 011 : Get  Building Detailed      : TEST FAILED...! :  \033[0m")







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
#         # error_text=building_update.json()["errorMessage"]
#         print(f"\033[91m❌ Test Case ID - 012 : Building Updated            : TEST FAILED...! :  \033[0m")









# # 13 : Building : Delete : 



#     building_delete = requests.patch(base_url + f"api/v1/masters/building/web/{company_id}/delete-building/{building_id}",headers=headers)
#     if building_delete.status_code == 200 :
#         # print("Building Deleted Successfully...!")
#         print(f"\033[92m✅ Test Case ID - 013 : Delete Building             : TEST PASSED...! \033[0m")

#     else: 
#         failed_count+=1
#         # error_text=building_delete.json()["errorMessage"]
#         # print("Building Deleted failed...! ",building_delete.text) 
#         print(f"\033[91m❌ Test Case ID - 013 : Delete Building             : TEST FAILED...! :  \033[0m")














# # ********************************************************Floor *******************************************



# # 14 : Create Floor : 

#     floor_payload={
#     "name": "second floor",
#     "code": 14,
#     "buildingId": "68709372293ae6389032a058"
#     }
#     create_floor = requests.post(base_url + f"api/v1/masters/floor/web/{company_id}/create-floor",json=floor_payload,headers=headers)
#     if create_floor.status_code == 201:
#        create_floor_json=create_floor.json()
#        floor_id = create_floor_json['id']
#     #   print("Floor  Created Successfully..!",create_floor.text)
#     #    print("Response JSON : ",json.dumps(create_floor_json,indent=4))
#        print(f"\033[92m✅ Test Case ID - 014 : Floor Creation              : TEST PASSED...! \033[0m")
#     else:
#         failed_count+=1
#         # error_text=create_floor.json()["errorMessage"]
#         print(f"\033[91m❌ Test Case ID - 014 : Floor Creation              : TEST FAILED...! :  \033[0m")
 
#     #    print("Failed Creation.",create_floor.text) 








# # ******************************Time Delay *********************************************


#     # wait_time = int(input("Enter wait time in seconds: "))

#     # print("\033[38;5;208m⏳ Waiting for Area to be available in frontend...\033[0m")

#     # # Countdown loop
#     # for remaining in range(wait_time, 0, -1):
#     #     print(f"\033[38;5;208m\r⏳ Waiting... {remaining} seconds left\033[0m", end="")
#     #     time.sleep(1)

#     # print("\033[38;5;208m\n✅ Done waiting!\033[0m")






# # 15 : Floor : List ALL : 

#     # print("\033[1;34mGet Area List!\033[0m")
#     floor_list_all = requests.get(base_url + f"api/v1/masters/floor/web/{company_id}/get-floor-list",headers=headers)
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
#         # error_text=floor_list_all.json()["errorMessage"]
#         print(f"\033[91m❌ Test Case ID - 015 : Get Floor List              : TEST FAILED...! :  \033[0m")

#         # print("Floor Listed Failed..!",floor_list_all.text)

 





# # # 16 : Floor : Get Detailed List : 

#     # print("\033[1;34mTESTING AREA DETAILED LIST !\033[0m")
#     floor_detailed_list = requests.get(base_url + f"api/v1/masters/floor/web/{company_id}/get-floor-list?floorId={floor_id}",headers=headers)
#     if floor_detailed_list.status_code == 201:
#         # print("Floor Detailed List Listed")
#         floor_detailed_json=floor_detailed_list.json()
#         print(f"\033[92m✅ Test Case ID - 016 : Get  Floor  Detailed        : TEST PASSED...! \033[0m")
#         # print("Response JSON : ",json.dumps(floor_detailed_json,indent=4))

#     else:
#         failed_count+=1
#         # error_text=floor_detailed_list.json()["errorMessage"]
#         print(f"\033[91m❌ Test Case ID - 016 : Get  Floor  Detailed        : TEST FAILED...! : \033[0m")
#         # print("Floor Detailed Listed Failed",floor_detailed_list.text)





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
#         # error_text=floor_update.json()["errorMessage"]
#         print(f"\033[91m❌ Test Case ID - 017 : Floor Updated               : TEST FAILED...! :  \033[0m")








# # # 18 : Floor  :  Delete :

#     floor_delete = requests.patch(base_url + f"api/v1/masters/floor/web/{company_id}/delete-floor/{floor_id}",headers=headers)
#     if floor_delete.status_code == 200 :
#         # print("Floor Deleted Successfully...!")
#         print(f"\033[92m✅ Test Case ID - 018 : Floor Deleted               : TEST PASSED...!  \033[0m")

#     else: 
#         failed_count+=1
#         # error_text=floor_delete.json()["errorMessage"]
#         print(f"\033[91m❌ Test Case ID - 018 : Floor Deleted               : TEST FAILED...! :  \033[0m")
#         # print("Floor Deleted failed...!",floor_delete.text) 







# #*********************************************************Departments*****************************************************







# # 19 : Create Department : 

#     # print("\033[1;34mGet Department List!\033[0m")
#     department_id=0
#     department_payload={
#         "name": "Dep Test",
#         "isActive": True
#     }
#     create_department = requests.post(base_url + f"api/v1/masters/department/web/{company_id}/create-department",json=department_payload,headers=headers)
#     if create_department.status_code == 201:
#        create_department_json=create_department.json()
#        department_id = create_department_json['id']
#     #    print(department_id)

      
#     #   print("Department  Created Successfully..!",create_department.text)
#     #    print("Response JSON : ",json.dumps(create_department_json,indent=4))
#        print(f"\033[92m✅ Test Case ID - 019 : Department Creation         : TEST PASSED...! \033[0m")
#     else:
#        failed_count+=1
#     #    error_text=create_department.json()["errorMessage"]
#        print(f"\033[91m❌ Test Case ID - 019 : Department Creation         : TEST FAILED...! :  \033[0m")
 
#     #    print("Failed Creation.",create_department.text) 










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
#         # error_text=dep_list_all.json()["errorMessage"]
#         print(f"\033[91m❌ Test Case ID - 020 : Get Department List         : TEST FAILED...! :  \033[0m")
#         # print("Department Listed Failed..!",dep_list_all.text)







# # # 21 : Department : Get Detailed List : 

#     # print("\033[1;34mTESTING Department DETAILED LIST !\033[0m")
#     dep_detailed_list = requests.get(base_url + f"api/v1/masters/department/web/{company_id}/get-department-list?departmentId={department_id}",headers=headers)
#     if dep_detailed_list.status_code == 200:
#         # print("Floor Detailed  ")
#         dep_detailed_json=dep_detailed_list.json()
#         print(f"\033[92m✅ Test Case ID - 021 : Get  Floor Detailed         : TEST PASSED...! \033[0m")
#         # print("Response JSON : ",json.dumps(dep_detailed_json,indent=4))

#     else:
#         failed_count+=1
#         # error_text=dep_detailed_list.json()["errorMessage"]
#         print(f"\033[91m❌ Test Case ID - 021 : Get  Floor  Detailed        : TEST FAILED...! :  \033[0m")
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
#         # error_text=dep_update.json()["errorMessage"]
#         print(f"\033[91m❌ Test Case ID - 022 : Department Updated          : TEST FAILED...! :  \033[0m")





#  # 23 : Department  :  Delete :

#     dep_delete = requests.patch(base_url + f"api/v1/masters/department/web/{company_id}/delete-department/{department_id}",headers=headers)
#     if dep_delete.status_code == 200 :
#         # print("Department Deleted Successfully...!")
#         print(f"\033[92m✅ Test Case ID - 023 : Department Deleted          : TEST PASSED...!  \033[0m")

#     else: 
#         failed_count+=1
#         # error_text=dep_delete.json()["errorMessage"]
#         print(f"\033[91m❌ Test Case ID - 023 : Department Deleted          : TEST FAILED...! :  \033[0m")
#         # print("Department Deleted failed...!",dep_delete.text) 



# # else:
# #     failed_count+=1
# #     # error_text=create_parentarea.json()["errorMessage"]

# #     print(f"\033[91m❌ Test Case ID - 002 : Area Creation (Parent)      : TEST FAILED...! :   \033[0m")

# #     #    print("Failed Creation.",create_parentarea.text) 






# # 17 :logout :  

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









# print(f"\033[1;34mTotal TEST FAILEDS  : {failed_count}/{total_count}\033[0m")

# if failed_count == 0:
#     print("\033[92m ✅ All TEST PASSED \033[0m")
