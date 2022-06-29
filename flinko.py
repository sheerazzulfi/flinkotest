import time
from aifc import Error

import requests
import json

class Execution_Failure(Error):
    pass

def login(token):
    s = requests.Session()

    head = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    head["Authorization"] = "Bearer " + token
    suiteid = 'SUITE1002'
    pes = s.post('https://app.flinko.com:8109/optimize/v1/dashboard/execution/suite/' + suiteid, headers=head)
    out = json.loads(pes.content)
    exid = out['responseObject']['id']
    
    time.sleep(3)
    sc = 0
    while (sc < 1):
        r1 = s.get('https://app.flinko.com:8110/optimize/v1/executionResponse/result/' + exid, headers=head)
        c1 = json.loads(r1.content)
        fr1 = c1['responseObject']['suiteStatus']
        if fr1 == 'PASS':
            print('Success')
            sc = 1
        if fr1 == 'FAIL':
            raise Execution_Failure
            sc = 1
        time.sleep(3)

login('eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJ0YWhlci50QHRlc3R5YW50cmEuY29tIiwic2NvcGUiOlsicmVhZCIsIndyaXRlIl0sIm5hbWUiOiJUYWhlciBTdXBlciBBZG1pbiIsImFjdGl2YXRpb25TdGF0dXMiOiJBQ1RJVkUiLCJpZCI6IlVTUjEwMDIiLCJwcml2aWxlZ2UiOiJTdXBlciBBZG1pbiIsImV4cCI6MjYzMTY4NDU3MywidXNlck5hbWUiOiJ0YWhlci50QHRlc3R5YW50cmEuY29tIiwibGljZW5zZUlkIjoiTElDMTAwMSIsImp0aSI6IjJaUGxVSmZxSUlvSXpnU0o5TVVzMU1pZDNMNCIsImNsaWVudF9pZCI6ImNsaWVudFZpdiJ9.Xrfn0-K1LUFuO2vM2YakQ1_XI-mHmiy7pqLhromCuqT84dLjNC-LlyGD7fT6xpQxMPIuds9qR9qtGPU4FgaLyNVadzZFmwUHXcRqflOn2rVlw-0SDRIYO8qoXSPhoWg4FLm_OFnAAxKZXW7TyyuLXLaBSdxA4-_6HqVIlXOTuy0TF3FKM97n_vJ1tcTz4x_3mD0_xnGAfB3WclaOiz-KzBRUVK5avP8dDOP-B2W-j1AN2UC_HB5tIkopyxauWCBOUJt0d2ldJUkyCT9cT0mT5CScf_mPzV9tUEv72c7CHc3M79hH16c7tqgqLzE_LaCthdMloaRnzq2hNglA5lnikw')
