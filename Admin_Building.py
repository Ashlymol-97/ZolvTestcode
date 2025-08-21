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
    print(f"\033[1;91m❌ TEST FAILED...! : Invalid Credentials \033[0m")
            # print("Response:", response_login.json())
else:
    response_json = response_login.json()
    print(f"Login Successfull   with status code {response_login.status_code}",login_payload)

    # print("Response JSON : ",json.dumps(response_json,indent=4))
    token= response_json.get('token',{}).get('token')
    company_id=response_json['company']['id']
    print(f"\033[1;92m✅ TEST PASSED...! \033[0m")
    headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
    }
    # print(f"Token (Login): {token}") 





# 2 : Building : Create :

    print("\033[1;34mTESTING AREA CREATION !\033[0m")
    create_building_payload = {
      "name": "BuildTest3",
      "code": 4
    }


    create_building = requests.post(base_url + f"api/v1/masters/building/web/{company_id}/create-building",json=create_building_payload,headers=headers)
    if create_building.status_code == 201:
        # print("Create Building Successfully..!")
        print(f"\033[1;92m✅ TEST PASSED...! \033[0m")

    else:
        print("Create Building Failed...!",create_building.text)
        print(f"\033[1;91m❌ TEST FAILED...! : Failed Building Creation \033[0m")


