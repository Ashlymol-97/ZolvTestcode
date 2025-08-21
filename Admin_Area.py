import requests
import time
import json
import random
import urllib.parse

import base64
import hashlib

print(f"\033[1;92m** ZOLV ADMIN TESTCODE **.\033[0m")


base_url= "https://qa-admin.zolv.health/"
login_url= "https://qa-admin.zolv.health/api/v1/user/login"
logout_url="https://qa-admin.zolv.health/api/v1/user/logout"



login_payload = {
    "loginId": "AutotestAdmin",
    "password": "Smm@1234"
}



    
# Login : 

print("\033[1;34mTESTING LOGIN!\033[0m")
response_login = requests.post(login_url,json=login_payload)
if response_login.status_code != 200:
    print(f"\033[91m❌ TEST FAILED...! : Invalid Credentials \033[0m")
            # print("Response:", response_login.json())
else:
    response_json = response_login.json()
    print(f"Login Successfull   with status code {response_login.status_code}",login_payload)

    print("Response JSON : ",json.dumps(response_json,indent=4))
    token= response_json.get('token',{}).get('token')
    company_id=response_json['company']['id']
    print(f"\033[92m✅ TEST PASSED...!8888 \033[0m")
    headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
    }
    print(f"Token (Login): {token}") 





# 1 : Area : Create Parent :

    print("\033[1;34mTESTING AREA CREATION !\033[0m")
    print("\033[1;34mTESTING PARENT AREA CREATION !\033[0m")


    create_parentarea_payload = {
        "name": "areatestparent",
        "code": 61,
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
        "preOrderStatus": True
        
    }
    create_parentarea = requests.post(base_url + f"api/v1/masters/area/web/{company_id}/create-area",json=create_parentarea_payload,headers=headers)
    if create_parentarea.status_code == 200:
      createparent_json=create_parentarea.json()
      print("Parent Area Created Successfully..!",create_parentarea.text)
      print("Response JSON : ",json.dumps(createparent_json,indent=4))

    else:

      print("Failed Creation.",create_parentarea.text) 





   

# 2 : Area create Child area :

    print("\033[1;34mTESTING CHILD AREA CREATION !\033[0m")

    create_childarea_payload = {
        "name": "area",
        "code": 45,
        "areaType": "child",
        "parentAreaId":"68a6b31389c43b6512ea7928", #if choose child area in area type, parentarea id field is mandatory .
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
      print("Child Area Created Successfully..!",create_childarea.text)
      # print("Response JSON : ",json.dumps(createchild_json,indent=4))

    else:

      print("Failed Creation.",create_childarea.text) 






# 3 : Area : List ALL : 

    print("\033[1;34mTESTING AREA LIST ALL!\033[0m")
    area_list_all = requests.get(base_url + f"api/v1/masters/area/web/{company_id}/get-area-list",headers=headers)
    if area_list_all.status_code == 200 :
        list_json=area_list_all.json()
        print("Response JSON : ",json.dumps(list_json,indent=4))
        print("Area Listed Successfully..!")
        area_id=list_json['areas'][0]['id']
        # print(area_id)

    else:
        print("Area Listed Failed..!")




# # 4 : Area : Get Detailed List : 

    print("\033[1;34mTESTING AREA DETAILED LIST !\033[0m")
    area_detailed_list = requests.get(base_url + f"api/v1/masters/area/web/{company_id}/get-area/{area_id}",headers=headers)
    if area_detailed_list.status_code == 200:
        print("Area Detailed List Listed")
        area_detailed_json=area_detailed_list.json()
        print(area_detailed_json)
    else:
        print("Area Detailed Listed Failed",area_detailed_list.text)




# # 5 : Area : Update List : doubt

    print("\033[1;34mTESTING AREA UPDATION !\033[0m")

    update_area_payload = {
            
            "name": "area",
            "code": 80,
            "areaType": "parent",
            "parentAreaId": "68a6b1ba89c43b6512ea7925",
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
                {
                    "name": "roomCredit",
                    "enabled": True
                }
            ],
            "deliveryModes": [
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
            "preOrderStatus":True,
            "qrKey": "57463274",
            "qrImage": "https://omniapictures.s3.ap-south-1.amazonaws.com/qrCodes/68a6b1ba89c43b6512ea7925.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20250821T070818Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=AKIA2MVKJRWJKAZW67NQ%2F20250821%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Signature=c551179ce8dad1230a09e0e48109078e51b8a3de2f63be764a2e5b8fbf4b6357",
            "languageId": "686f510c6e7e978b9132a03e"
        }

    print("\033[1;34mTESTING AREA UPDATED LIST !\033[0m")
    area_update = requests.put(base_url + f"api/v1/masters/area/web/{company_id}/update-area/68a6b1ba89c43b6512ea7925",json=update_area_payload,headers=headers)
    if area_update.status_code == 200 :
        print("Area Updated Successfully..!")
    else:
        print("Area Updated Failed...! ",area_update.text,area_update.status_code)






# 6 : Area : Delete :

    area_delete = requests.patch(base_url + f"api/v1/masters/area/web/{company_id}/delete-area/68a6daa489c43b6512ea79a5",headers=headers)
    if area_delete.status_code == 200 :
        print("Area Deleted Successfully...!")
    else: 
        print("Area Deleted failed...!",area_delete.text) 





# **************************Building *********************************




# 7 : : Building : Create :

    print("\033[1;34mTESTING BUILDING CREATION !\033[0m")
    create_building_payload = {
      "name": "BuildTest4",
      "code": 5
    }


    create_building = requests.post(base_url + f"api/v1/masters/building/web/{company_id}/create-building",json=create_building_payload,headers=headers)
    if create_building.status_code == 201:
        # print("Create Building Successfully..!")
        print(f"\033[1;92m✅ TEST PASSED...! \033[0m")

    else:
        print("Create Building Failed...!",create_building.text)
        print(f"\033[1;91m❌ TEST FAILED...! : Failed Building Creation \033[0m")




# 8 : Building : List ALL : 

    print("\033[1;34mTESTING BUILDING LIST ALL!\033[0m")
    building_list_all = requests.get(base_url + f"api/v1/masters/building/web/{company_id}/get-building-list",headers=headers)
    if building_list_all.status_code == 200 :
        build_json=building_list_all.json()
        print("Response JSON : ",json.dumps(build_json,indent=4))
        print("Building Listed Successfully..!")
        building_id=build_json['buildings'][0]['id']
        # print(building_id)

    else:
        print("Building Listed Failed..!")

