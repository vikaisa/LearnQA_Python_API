import time
import requests

response_create_status = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
response_create_status_message = response_create_status.json()
print(f"Текст ответа на первый запрос: {response_create_status_message}")

token = None
seconds = None

keys_wo_get_param = ["token", "seconds"]
for key in keys_wo_get_param:
    if key in response_create_status_message and key == "token":
        token = response_create_status_message[key]
    if key in response_create_status_message and key == "seconds":
        seconds = response_create_status_message[key]
    if key not in response_create_status_message:
        print(f"Ключа {key} в тексте ответе нет")


response_check_status = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})
response_check_status_message = response_check_status.json()
print(f"Текст ответа на второй запрос: {response_check_status_message}")

tmp_status = None
tmp_result = None
tmp_error = None

keys_with_get_param = ["status", "result", "error"]
for key in keys_with_get_param:
    if key in response_check_status_message and key == "status":
        tmp_status = response_check_status_message[key]
    if key in response_check_status_message and key == "result":
        tmp_result = response_check_status_message[key]
    if key in response_check_status_message and key == "error":
        print(f"В ответе вернулась ошибка: '{response_check_status_message[key]}'")
    if key not in response_check_status_message:
        print(f"Ключа {key} в тексте ответе нет")


if tmp_status == "Job is NOT ready" and tmp_error is None:
    time.sleep(seconds)
    response_check_result = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})
    response_check_result_message = response_check_result.json()
    print(f"Текст ответа на третий запрос: {response_check_result_message}")

    status = None
    result = None
    error = None

    keys_with_get_param = ["status", "result", "error"]
    for key in keys_with_get_param:
        if key in response_check_result_message and key == "status":
            status = response_check_result_message[key]
        if key in response_check_result_message and key == "result":
            result = response_check_result_message[key]
        if key in response_check_result_message and key == "error":
            print(f"В ответе вернулась ошибка: '{response_check_result_message[key]}'")
        if key not in response_check_result_message:
            print(f"Ключа {key} в тексте ответе нет")
    if status == "Job is ready" and result is not None:
        print(f"Final result: job is ready with the following result: '{result}'")
    else:
        print(f"The error occurred: '{error}'")
else:
    print(f"Wrong status '{tmp_status}' or/and error occurred: '{tmp_error}")
