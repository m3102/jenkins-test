import sys
import xmlrunner

sys.path.append("../")

from flask import json
from unittest import TestCase, main

class UnitIntegration(TestCase):
    # def test_login_successful(self):
    #     payload = {
    #         "pageCredentials": {
    #             "email": "test1@gg.com",
    #             "password": "P@ssword1312",
    #         }
    #     }
    #     res = self.app.post(
    #         "/api/auth/login",
    #         headers={"Content-Type": "application/json"},
    #         data=encryption(payload),
    #     )
    #     data = json.loads(res.data.decode())
    #     self.assertEqual(True, data["status"])
    #     self.assertEqual(200, res.status_code)

    # def test_login_unsuccessful(self):
    #     payload = {
    #         "pageCredentials": {
    #             "email": "emailnotused@gmail.com",
    #             "password": "Password123!",
    #         }
    #     }
    #     res = self.app.post(
    #         "/api/auth/login",
    #         headers={"Content-Type": "application/json"},
    #         data=encryption(payload),
    #     )
    #     data = json.loads(res.data.decode())
    #     self.assertEqual(str, type(data["failedReason"]))
    #     self.assertEqual(400, res.status_code)
    pass



if __name__ == "__main__":
    runner = xmlrunner.XMLTestRunner(output="../unit-integration-test-reports")
    main(testRunner=runner)