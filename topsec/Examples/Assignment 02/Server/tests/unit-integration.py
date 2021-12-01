import sys

sys.path.append("../")

from flask import json
from unittest import TestCase, main
import xmlrunner, json, psycopg2


# from configuration import setup_testing_environment
# setup_testing_environment()

from server import app
from controller.validation.authController import AuthController
from controller.validation.donateController import DonateController
from controller.database.dbController import DatabaseController
from controller.database.user import UserController
from globals import AESEncryptor


auth = AuthController()
donate = DonateController()
db = DatabaseController()
user = UserController(db)


def encryption(payload):
    encryption = AESEncryptor.encrypt(
        json.dumps(payload).encode(), AESEncryptor.encoded_key
    )
    return json.dumps({"cipherText": encryption.decode()})


class UnitIntegration(TestCase):
    # Mock existing server
    def setUp(self):
        self.app = app.test_client()

    # Unit tests
    def test_validation_username(self):
        testCases = {
            "": "Username cannot be empty",
            "g": "Username must be 8 to 20 characters",
            "giggs123?=": "Username can only have alphanumeric, underscore and dot characters",
            123456789: None,
            "giggs123": None,
        }
        for testValue, expectedResult in testCases.items():
            self.assertEqual(auth.validateUsername(testValue), expectedResult)

    def test_validation_email(self):
        testCases = {
            "test@test.com": None,
            "email@subdomain.examample.com": None,
            "ankitrai326.com": "Invalid email format",
            "Abc..123@example.com": "Invalid email format",
            "@#$@#.com": "Invalid email format",
        }
        for testValue, expectedResult in testCases.items():
            self.assertEqual(auth.validateEmail(testValue), expectedResult)

    def test_validation_password(self):
        testCases = {
            "p": "Password must be length of 8 - 128 characters",
            "ligma": "Password must be length of 8 - 128 characters",
            "12345": "Password used is too common (NIST guideline)",
            "password": "Password used is too common (NIST guideline)",
            "PASSWORD123!": None,
        }
        for testValue, expectedResult in testCases.items():
            self.assertEqual(auth.validatePassword(testValue), expectedResult)

    def test_validate_creditcard(self):
        testCases = {
            "3710293": False,
            "5190990281925290": False,
            "3716820019271998": True,
            "37168200192719989": False,
            "8102966371298364": False,
            "6823119834248189": True,
        }
        for testValue, expectedResult in testCases.items():
            self.assertEqual(donate.luhnAlgorithm(testValue), expectedResult)

    # Integration tests
    def test_database_connection(self):
        self.assertEqual(True, db.isConnected())

    def test_fetch_user_successful(self):
        self.assertEqual(
            psycopg2.extras.RealDictRow, type(user.fetchUser("test1@gg.com"))
        )

    def test_fetch_user_unsuccesful(self):
        self.assertEqual(None, user.fetchUser("emailnotused@gmail.com"))

    def test_signup_successful(self):
        payload = {
            "pageCredentials": {
                "username": "usernotused",
                "email": "emailnotused@test.com",
                "password": "Ligma123!",
                "confirmPassword": "Ligma123!",
                "agreed": True,
            }
        }
        res = self.app.post(
            "/api/auth/signupInitial",
            headers={"Content-Type": "application/json"},
            data=encryption(payload),
        )
        self.assertEqual(dict, type(res.json))
        self.assertEqual(200, res.status_code)

    def test_signup_unsuccessful(self):
        payload = {
            "pageCredentials": {
                "username": "testuser",
                "email": "test@test.com",
                "password": "Ligma123!",
                "confirmPassword": "Ligma123!",
                "agreed": False,
            }
        }
        res = self.app.post(
            "/api/auth/signupInitial",
            headers={"Content-Type": "application/json"},
            data=encryption(payload),
        )
        self.assertEqual(str, type(res.json["failedReason"]))
        self.assertEqual(400, res.status_code)

    def test_forgotpassword_successful(self):
        payload = {"email": "test1@gg.com"}
        res = self.app.post(
            "/api/auth/forgotInitial",
            headers={"Content-Type": "application/json"},
            data=encryption(payload),
        )
        self.assertEqual(str, type(res.json["question"]))
        self.assertEqual(200, res.status_code)

    def test_forgotpassword_unsuccesful(self):
        payload = {"email": "emailnotused@gmail.com"}
        res = self.app.post(
            "/api/auth/forgotInitial",
            headers={"Content-Type": "application/json"},
            data=encryption(payload),
        )
        self.assertEqual(str, type(res.json["failedReason"]))
        self.assertEqual(400, res.status_code)

    def test_login_successful(self):
        payload = {
            "pageCredentials": {
                "email": "test1@gg.com",
                "password": "P@ssword1312",
            }
        }
        res = self.app.post(
            "/api/auth/login",
            headers={"Content-Type": "application/json"},
            data=encryption(payload),
        )
        data = json.loads(res.data.decode())
        self.assertEqual(True, data["status"])
        self.assertEqual(200, res.status_code)

    def test_login_unsuccessful(self):
        payload = {
            "pageCredentials": {
                "email": "emailnotused@gmail.com",
                "password": "Password123!",
            }
        }
        res = self.app.post(
            "/api/auth/login",
            headers={"Content-Type": "application/json"},
            data=encryption(payload),
        )
        data = json.loads(res.data.decode())
        self.assertEqual(str, type(data["failedReason"]))
        self.assertEqual(400, res.status_code)

    def test_changepassword_unsuccesful(self):
        payload = {
            "pageCredentials": {
                "oldPassword": "P@ssword1312",
                "newPassword": "Dickbutt123!",
                "confirmPassword": "Dickbutt321!",
            },
            "email": "test1@gg.com",
            "external": False,
        }
        res = self.app.post(
            "/api/registered/changeInitial",
            headers={"Content-Type": "application/json"},
            data=encryption(payload),
        )
        data = json.loads(res.data.decode())
        self.assertEqual(str, type(data["failedReason"]))
        self.assertEqual(400, res.status_code)


if __name__ == "__main__":
    runner = xmlrunner.XMLTestRunner(output="../unit-integration-test-reports")
    main(testRunner=runner)
    # main()
