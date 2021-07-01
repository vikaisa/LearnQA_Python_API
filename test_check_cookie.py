import requests


def test_check_cookie():
    response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
    cookie = dict(response.cookies)
    assert len(cookie) != 0, f"No cookies were returned"
    if "HomeWork" in cookie:
        assert cookie["HomeWork"] == "hw_value", f"Wrong cookie value was returned: {cookie}"
    else:
        assert False, f"There is no cookie with name 'HomeWork' in the response. Actual cookies: {cookie}"
