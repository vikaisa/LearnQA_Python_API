import requests


def test_check_header():
    response = requests.get("https://playground.learnqa.ru/api/homework_header")
    header = dict(response.headers)
    assert len(header) != 0, f"No headers were returned"

    if "x-secret-homework-header" in header:
        assert header["x-secret-homework-header"] == "Some secret value", f"Wrong header value was returned: {header}"
    else:
        assert False, f"There is no header with name 'x-secret-homework-header' in the response. Actual headers: {header}"
