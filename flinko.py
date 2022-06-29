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

login('eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJzaGVlcmF6enVsZmkxMjNAZ21haWwuY29tIiwic2NvcGUiOlsicmVhZCIsIndyaXRlIl0sIm5hbWUiOiJzaGVlcmF6IHp1bGZpIiwiYWN0aXZhdGlvblN0YXR1cyI6IkFDVElWRSIsImlkIjoiVVNSMjQ3NiIsInByaXZpbGVnZSI6IlN1cGVyIEFkbWluIiwiZXhwIjoyNjU2MDQ2NDQ2LCJ1c2VyTmFtZSI6InNoZWVyYXp6dWxmaTEyM0BnbWFpbC5jb20iLCJsaWNlbnNlSWQiOiJMSUMxNjcyIiwianRpIjoidlVWdVJlcHJNQWtlS1JFby1RbEtRUlhEY1EwIiwiY2xpZW50X2lkIjoiY2xpZW50Vml2In0.qwJYJWQTZ9OmH8gcewA70YnkYf72UoASfhIlaeRSwrj8PZ1MyIh6IVgHIUChwlLoFAKMOjka9HQx3MtohlGz8v1a8LWnE1e3camHSyJGZGlct8Kwdk-vTJn086Ctrjn6BQ8Tb4kha4uk01z9E-Q75mFNgUdG7_koohFLYGZglSTQeyWrxHtO_LQQbqSsEEegx4j9ru9pQLL3AX9CI4aJBVy73_UfO9DmirgIeo5ut1wxJqilxCfX0z1uvncJ24fs1YQDgjmDv2T-Hwe5uzxXftL_JyOc74RbVTXaQbK7eDicVKqF7nrccu9ZYdLAvBwuLfKC3OlyjuXpl1SZyZD74g')
