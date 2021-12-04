import requests

def entradaDados():
    nome = input("Digite seu nome: ")
    sexo = input("Digite seu sexo: ")
    cabelo = input("Digite a cor do seu cabelo: ")
    
    dados = {"nome": nome, "sexo": sexo, "cabelo": cabelo}
    
    return dados


def testePost():
    dados = entradaDados()
    x = requests.post("http://localhost:5003/pessoa", json = dados)
    if x.status_code != 200:
        print(f"[{x.status_code}], {x.text}")
    else:
        print(x.text)
        
def testePut():
    id_pessoa = input("Digite um id para realizar a alteração: ")
    x = requests.put(f"http://localhost:5003/pessoa/{id_pessoa}")
    if x.status_code != 200:
        print(f"[{x.status_code}], {x.text}")
    else:
        print(x.text)
        
def testeGetID():
    id_pessoa = input("Digite o id da pessoa que deseja consultar: ")
    x = requests.get(f"http://localhost:5003/pessoa/{id_pessoa}")
    if x.status_code != 200:
        print(f"[{x.status_code}], {x.text}")
    else:
        print(x.text)
        
def testeDelete():
    id_pessoa = input("Digite um id para realizar a exclusão: ")
    x = requests.delete(f"http://localhost:5003/pessoa/{id_pessoa}")
    if x.status_code != 200:
        print(f"[{x.status_code}], {x.text}")
    else:
        print(x.text)

      
print('------------------------------------------\n')		
print('Tentando a rota /pessoa com POST\n')
testePost()

print('------------------------------------------\n')	
print('Tentando a rota /pessoa com POST novamente \n')	
testePost()

print('------------------------------------------\n')	
print('Tentando a rota /pessoa com PUT \n')	
testePut()

print('------------------------------------------\n')	
print('Tentando a rota /pessoa com GET com ID \n')	
testeGetID()

print('------------------------------------------\n')	
print('Tentando a rota /pessoa com DELETE \n')	
testeDelete()

    