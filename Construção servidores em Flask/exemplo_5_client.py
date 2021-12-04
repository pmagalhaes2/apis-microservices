import requests
a = input("Digite o valor de a: ")
b = input("Digite o valor de b: ")
url_div = f"http://localhost:5000/{a}/divide/{b}"
url_soma = f"http://localhost:5000/{a}/soma/{b}"

x = requests.get(url_div)
if x.status_code != 200:
    print(f"[{x.status_code}] {x.text}")
else:
    print(f"{a} dividido por {b} é igual a {x.text}.")


y = requests.get(url_soma)
if y.status_code != 200:
    print(f"[{y.status_code}] {y.text}")
else:
    print(f"{a} somado com {b} é igual a {y.text}.")

