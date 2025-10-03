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
    error_text=response_login.json()["errorMessage"]
    print(f"\033[91m❌  Test Case ID - 001 : Login                      : TEST FAILED...! : {error_text}  \033[0m")
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

        area_detailed_list = requests.get(base_url + f"api/v1/masters/area/web/{company_id}/get-area/{area_id}",headers=headers)
        if area_detailed_list.status_code == 200:
           
            area_detailed_list_json=area_detailed_list.json()
            # area_name=createparent_json.get('name')

            #    print("Parent Area Created Successfully..!",create_parentarea.text,area_id)
            # print("Response JSON : ",json.dumps(createparent_json,indent=4))
            print(f"\033[92m✅ Test Case ID - 002 : Area Creation (Parent)      : TEST PASSED...!  \033[0m")
    else:
        failed_count+=1
        error_text=create_parentarea.json()["errorMessage"]

        print(f"\033[91m❌ Test Case ID - 002 : Area Creation (Parent)      : TEST FAILED...! : {error_text}  \033[0m")
    
        #    print("Failed Creation.",create_parentarea.text) 








# ******************************Time Delay *********************************************


    import time

    choice = input("\033[38;5;208mDo you want to add a wait delay? (yes/no): \033[0m").strip().lower()

    if choice == "yes":
        wait_time = int(input("\033[38;5;208mEnter wait time in seconds: \033[0m"))
        print("\033[38;5;208m⏳ Waiting for Area to be available in frontend...\033[0m")

        # Countdown loop
        for remaining in range(wait_time, 0, -1):
            print(f"\033[38;5;208m\r⏳ Waiting... {remaining} seconds left\033[0m", end="")
            time.sleep(1)

        print("\033[38;5;208m\n✅ Done waiting!\033[0m")

    else:
        print("\033[38;5;82m⏩ Skipping wait... proceeding immediately!\033[0m")





    
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
        

        # print("Area Listed Failed..!")
        try:
          error_text=area_list_all.json()["errorMessage"]
          print(f"\033[91m❌ Test Case ID - 004 : Get Area List               : TEST FAILED...! : {error_text}  \033[0m")
        except ValueError:
         error_text = area_list_all.text



