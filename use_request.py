import requests

url = 'https://detik.com'
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'succes response = {response.status_code}')
        print(f'Content {response.text}')
    else:
        print(f'Wjops, Ada Kesalahan Request {response.status_code}')
except Exception as e:
    print('There is an Error', {e})
print('Program ended')
