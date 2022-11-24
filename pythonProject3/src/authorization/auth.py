import pytest
import requests

class Test:

    def test(self):

        post_url_admin_auth = "http://213.139.208.142:8083/api/admin/auth/signin"
        post_json_admin_auth = {
             "password": "fM57Ls8rxVNE8gTD",
            "email": "admin@admin.com"
         }
        post_request_admin_auth = requests.post(post_url_admin_auth, json=post_json_admin_auth)
        admin_token = post_request_admin_auth.json()["data"]
        return admin_token