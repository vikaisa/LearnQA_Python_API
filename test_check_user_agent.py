import pytest
import requests

user_agents = [(
    "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
    "Mobile", "No", "Android"),
    ("Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
     "CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1", "Mobile", "Chrome", "iOS"),
    ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
     "Googlebot", "Unknown", "Unknown"),
    (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0",
        "Web", "Chrome", "No"),
    (
        "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
        "Mobile", "No", "iPhone")
]


@pytest.mark.parametrize("user_agent_value_in_request, expected_platform, expected_browser, expected_device", user_agents)
def test_check_user_agent(user_agent_value_in_request, expected_platform, expected_browser, expected_device):
    response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check",
                            headers={"User-Agent": user_agent_value_in_request})
    response_as_json = response.json()
    if "user_agent" in response_as_json:
        user_agent_value_in_response = response_as_json["user_agent"]
        assert user_agent_value_in_response == user_agent_value_in_request, f"Wrong user agent value\n" \
                                                                            f"Actual: {user_agent_value_in_response}\n" \
                                                                            f"Expected: {user_agent_value_in_request}"
    else:
        print(f"Ключа 'user_agent' в тексте ответа нет")
    if "platform" in response_as_json:
        actual_platform = response_as_json["platform"]
        assert actual_platform == expected_platform, f"Wrong platform value\nActual: {actual_platform}\nExpected: {expected_platform}"
    else:
        print(f"Ключа 'platform' в тексте ответа нет")
    if "browser" in response_as_json:
        actual_browser = response_as_json["browser"]
        assert actual_browser == expected_browser, f"Wrong browser value\nActual: {actual_browser}\nExpected: {expected_browser}"
    else:
        print(f"Ключа 'browser' в тексте ответа нет")
    if "device" in response_as_json:
        actual_device = response_as_json["device"]
        assert actual_device == expected_device, f"Wrong device value\nActual: {actual_device}\nExpected: {expected_device}"
    else:
        print(f"Ключа 'device' в тексте ответа нет")
