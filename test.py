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
    }
    # print(f"Token (Login): {token}") 








# # # 5 : Area : Update List : Pending

    print("\033[1;34mTESTING AREA UPDATION !\033[0m")

    update_area_payload = {    
        "name"  : "areas",
        "code"  : 80,
        "areaType" : "parent",
        "isActive" : True,
        "buildingId" : "68709372293ae6389032a058",
        "floorId" : "68709372293ae6389032a05a",
        "preOrderStatus" : True,
        "parentAreaId" : "68a6b1ba89c43b6512ea7925",
        "moduleGroupId" : "68709372293ae6389032a05b",
        "qrKey" : 57463274,
        "languageId" : "686f510c6e7e978b9132a03e",
        "deliveryModes[0].name" : "roomDelivery",
        "deliveryModes[0].enabled" : True,
        "deliveryModes[1].name" : "takeAway",
        "deliveryModes[1].enabled" : True,
        # "deliveryModes[2].name" : "dineIn",
        # "deliveryModes[2].enabled" : True,
        "paymentModes[0].name" : "paymentGateway",
        "paymentModes[0].enabled" : True,
        "paymentModes[1].name" : "payOnDelivery",
        "paymentModes[1].enabled" : True,
        "paymentModes[2].name" : "roomCredit",
        "paymentModes[2].enabled" : True,
        }
    files = {
        "image": ("QRcodeimage.png", open("C:/Users/SMM-06/Downloads/QRcodeimage.png", "rb"),"image/png")
    }
 

    print("\033[1;34mTESTING AREA UPDATED LIST !\033[0m")

    area_update = requests.put(
        base_url + f"api/v1/masters/area/web/{company_id}/update-area/68ac10a1872a953f691153c3",
        data=update_area_payload,
        headers=headers
    )
    if area_update.status_code == 200 :
        print("Area Updated Successfully..!")
    else:
        print("Area Updated Failed...! ",area_update.text)





















































# #  5 : Area : Update List : Pending

#     print("\033[1;34mTESTING AREA UPDATION !\033[0m")

#     update_area_payload = {    
#         "name"  : "First",
#         "code"  : 579,
#         "areaType" : "child",
#         "isActive" : True,
#         "buildingId" : "68709372293ae6389032a058",
#         "floorId" : "68709372293ae6389032a05a",
#         "preOrderStatus" : True,
#         "parentAreaId" : "68a5af7a03cfe84816ecd0d7",
#         "moduleGroupId" : "68709372293ae6389032a05b",
#         "qrKey" : 70869307,
#         "languageId" : "686f510c6e7e978b9132a03e",
#         "deliveryModes[0].name" : "roomDelivery",
#         "deliveryModes[0].enabled" : True,
#         "deliveryModes[1].name" : "takeAway",
#         "deliveryModes[1].enabled" : True,
#         "deliveryModes[2].name" : "dineIn",
#         "deliveryModes[2].enabled" : True,
#         "paymentModes[0].name" : "paymentGateway",
#         "paymentModes[0].enabled" : True,
#         "paymentModes[1].name" : "payOnDelivery",
#         "paymentModes[1].enabled" : True,
#         "paymentModes[2].name" : "roomCredit",
#         "paymentModes[2].enabled" : True,
#         }
#     files = {
#         "image": ("QRcodeimage.png", open("C:/Users/SMM-06/Downloads/QRcodeimage.png", "rb"),"image/png")
#     }
 

#     print("\033[1;34mTESTING AREA UPDATED LIST !\033[0m")

#     area_update = requests.put(
#         base_url + f"api/v1/masters/area/web/{company_id}/update-area/68ac10a1872a953f691153c3",
#         data=update_area_payload,
#         headers=headers
#     )
#     if area_update.status_code == 200 :
#         print("Area Updated Successfully..!")
#     else:
#         print("Area Updated Failed...! ",area_update.text)

# # C:\Users\SMM-06\Downloads\QRcodeimage.png







# # area_update = requests.put(
# #     base_url + f"api/v1/masters/area/web/{company_id}/update-area/68ac10a1872a953f691153c3",
#     data={"payload": json.dumps(update_area_payload)},
#     headers=headers,
#     files=files
# )
