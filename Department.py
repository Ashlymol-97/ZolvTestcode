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






#*********************************************************Departments*****************************************************







# 19 : Create Department : 

    # print("\033[1;34mGet Department List!\033[0m")
    department_id=0
    department_payload={
        "name": "Dep Test",
        "isActive": True
    }
    create_department = requests.post(base_url + f"api/v1/masters/department/web/{company_id}/create-department",json=department_payload,headers=headers)
    if create_department.status_code == 201:
       create_department_json=create_department.json()
       department_id = create_department_json['id']
    #    print(department_id)

      
    #   print("Department  Created Successfully..!",create_department.text)
    #    print("Response JSON : ",json.dumps(create_department_json,indent=4))
       print(f"\033[92m✅ Test Case ID - 019 : Department Creation         : TEST PASSED...! \033[0m")
    else:
       failed_count+=1
    #    error_text=create_department.json()["errorMessage"]
       print(f"\033[91m❌ Test Case ID - 019 : Department Creation         : TEST FAILED...! :  \033[0m")
 
    #    print("Failed Creation.",create_department.text) 










# 20 : Department : List ALL : 

    # print("\033[1;34mGet Department List!\033[0m")
    dep_list_all = requests.get(base_url + f"api/v1/masters/area/web/{company_id}/get-area-list",headers=headers)
    if dep_list_all.status_code == 200 :
        dep_json=dep_list_all.json()
        # print("Response JSON : ",json.dumps(dep_json,indent=4))
        # print("Department Listed Successfully..!",dep_list_all.text)
        print(f"\033[92m✅ Test Case ID - 020 : Get Department List         : TEST PASSED...! \033[0m")


    else:
        failed_count+=1
        # error_text=dep_list_all.json()["errorMessage"]
        print(f"\033[91m❌ Test Case ID - 020 : Get Department List         : TEST FAILED...! :  \033[0m")
        # print("Department Listed Failed..!",dep_list_all.text)







# # 21 : Department : Get Detailed List : 

    # print("\033[1;34mTESTING Department DETAILED LIST !\033[0m")
    dep_detailed_list = requests.get(base_url + f"api/v1/masters/department/web/{company_id}/get-department-list?departmentId={department_id}",headers=headers)
    if dep_detailed_list.status_code == 200:
        # print("Floor Detailed  ")
        dep_detailed_json=dep_detailed_list.json()
        print(f"\033[92m✅ Test Case ID - 021 : Get  Floor Detailed         : TEST PASSED...! \033[0m")
        # print("Response JSON : ",json.dumps(dep_detailed_json,indent=4))

    else:
        failed_count+=1
        # error_text=dep_detailed_list.json()["errorMessage"]
        print(f"\033[91m❌ Test Case ID - 021 : Get  Floor  Detailed        : TEST FAILED...! :  \033[0m")
        # print("Floor Detailed  Failed",dep_detailed_list.text)






       
# 22 : Department : Update :  


    update_dep_payload = {
        "name": "Department test",
        "isActive": True
    }

    dep_update = requests.put(
        base_url + f"api/v1/masters/department/web/{company_id}/update-department/{department_id}",
        json=update_dep_payload,  # Corrected here
        headers=headers
    )

    if dep_update.status_code == 200:
        dep_update_json = dep_update.json()
        print(f"\033[92m✅ Test Case ID - 022 : Department Updated          : TEST PASSED...! \033[0m")
    else: 
        failed_count += 1
        # error_text=dep_update.json()["errorMessage"]
        print(f"\033[91m❌ Test Case ID - 022 : Department Updated          : TEST FAILED...! :  \033[0m")





 # 23 : Department  :  Delete :

    dep_delete = requests.patch(base_url + f"api/v1/masters/department/web/{company_id}/delete-department/{department_id}",headers=headers)
    if dep_delete.status_code == 200 :
        # print("Department Deleted Successfully...!")
        print(f"\033[92m✅ Test Case ID - 023 : Department Deleted          : TEST PASSED...!  \033[0m")

    else: 
        failed_count+=1
        # error_text=dep_delete.json()["errorMessage"]
        print(f"\033[91m❌ Test Case ID - 023 : Department Deleted          : TEST FAILED...! :  \033[0m")
        # print("Department Deleted failed...!",dep_delete.text) 



# else:
#     failed_count+=1
#     # error_text=create_parentarea.json()["errorMessage"]

#     print(f"\033[91m❌ Test Case ID - 002 : Area Creation (Parent)      : TEST FAILED...! :   \033[0m")

#     #    print("Failed Creation.",create_parentarea.text) 






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
