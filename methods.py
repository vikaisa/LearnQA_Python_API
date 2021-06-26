import requests

response1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
response2 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
response3 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "POST"})

payload = ["GET", "POST", "PUT", "DELETE"]
for item in payload:
    response_get = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": item})
    response_post = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": item})
    response_put = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": item})
    response_delete = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": item})
    print(f"Param 'method' value: {item}\nResponse GET status code: {response_get.status_code}; Response GET text: {response_get.text}")
    print("____________\n")
    print(f"Param 'method' value: {item}\nResponse POST status code: {response_post.status_code}; Response POST text: {response_post.text}")
    print("____________\n")
    print(f"Param 'method' value: {item}\nResponse PUT status code: {response_put.status_code}; Response PUT text: {response_put.text}")
    print("____________\n")
    print(f"Param 'method' value: {item}\nResponse DELETE status code: {response_delete.status_code}; Response DELETE text: {response_delete.text}")
    print("\n*****************end******************\n")

print(f"Response 1 status code: {response1.status_code}; Response 1 text: {response1.text}")
print(f"Response 2 status code: {response2.status_code}; Response 2 text: {response2.text}")
print(f"Response 3 status code: {response3.status_code}; Response 3 text: {response3.text}")
