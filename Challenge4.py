#!/usr/bin/env python3
import requests
import json

# API calling function to return json dictionary of institution data
def getInstitutionData(offset):
    client_ID = '5cb79ee85f6405001217f174'
    secret = '025476d4aa2c21172ee9c4b20b7428'
    url = 'https://sandbox.plaid.com/institutions/get'
    payload = {
        "client_id": client_ID,
        "secret": secret,
        "count": 500,       # returns 500 institutions per call (max permitted)
        "offset": offset    # offset is incremented by 500 on each call to get next set of data
    }
    res = requests.post(url, json=payload)
    result_dic = res.json()
    return result_dic

def main():
    totalInstitutions = getInstitutionData(0)['total']      # Determining total number of institutions
    print("Total Plaid institutions: "+ str(totalInstitutions))
    institutionsIdentity = []
    institutionsFirst = []
    offset = 0
    while offset <= totalInstitutions:      # While we haven't captured each institution up to the total
        institutionDic = getInstitutionData(offset)["institutions"]
        for item in institutionDic:
            if "identity" in item["products"]:
                institutionsIdentity.append(item['name'])   # Could have incremented a count for extra space efficiency
            if 'First' in item['name'] or 'first' in item['name']:
                institutionsFirst.append(item['name'])      # Could have incremented a count for extra space efficiency
        offset += 500
    print("Institutions supporting identity product: " + str(len(institutionsIdentity)))
    print("Institutions with first in the name: " + str(len(institutionsFirst)))

if __name__ == '__main__':
    main()