import json
import requests

json_file_name = 'test_file.json'
binary_file_name = 'test_file.bin'
url = 'https://api.frankfurter.app/latest'


def save_json_file(filename):
    with open(filename, 'a') as json_file:
        content = input("Napisz co chcesz dopisać do pliku: ")
        json.dump(content, json_file)


def save_byte_file(filename):
    file = open(filename, 'ab')
    content = input("Napisz co chcesz dopisać do pliku: ")
    file.write(content.encode())
    file.close()


def sort_request(url):
    response = requests.get(url)
    response = response.json()
    response = response['rates']
    print(response)
    response = {s: n for s, n in sorted(response.items(), key=lambda item: item[1])}
    print(response)

save_json_file(json_file_name)
save_byte_file(binary_file_name)
sort_request(url)
