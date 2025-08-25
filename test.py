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
total_count=11
    
# Login : 

# print("\033[1;34mTESTING LOGIN!\033[0m")
response_login = requests.post(login_url,json=login_payload)
if response_login.status_code != 200:
    failed_count+=1
    print(f"\033[91m❌ TEST FAILED...! : Invalid Credentials : Test Case ID - 001\033[0m")
            # print("Response:", response_login.json())
else:
    response_json = response_login.json()
    # print(f"Login Successfull   with status code {response_login.status_code}",login_payload)

    # print("Response JSON : ",json.dumps(response_json,indent=4))
    token= response_json.get('token',{}).get('token')
    company_id=response_json['company']['id']
    print(f"\033[92m✅ TEST PASSED...! : Test Case ID - 001 \033[0m")
    headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
    }
    # print(f"Token (Login): {token}") 








# # 5 : Area : Update List : Pending

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
    
    form_data = {}
    for key, value in update_area_payload.items():
        if isinstance(value, (dict, list)):
            form_data[key] = str(value)  # or json.dumps(value) for proper JSON string
        else:
            form_data[key] = value

    print("\033[1;34mTESTING AREA UPDATED LIST !\033[0m")
    area_update = requests.put(base_url + f"api/v1/masters/area/web/{company_id}/update-area/68ac10a1872a953f691153c3",data=form_data,headers=headers)
    if area_update.status_code == 200 :
        print("Area Updated Successfully..!")
    else:
        print("Area Updated Failed...! ",area_update.text,area_update.status_code)

