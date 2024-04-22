import requests

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ3ZWlnaHQiOjkuMDgsInBvaW50X2lkIjoxLCJpYXQiOjE3MTA0OTc5Mjh9.EkeireB8pAYu7UYzCcZo11EaNt6rrlZlmfbxaXNTIZM'

url = f'https://icoleta.netlify.app/descarte/{token}'

# Neste exemplo específico, você não está usando os headers na requisição, então essa parte foi comentada.
# Se a sua intenção é enviar o token também no cabeçalho Authorization (o que é uma prática comum), você deve descomentar.
# headers = {
#     'Authorization': f'Bearer {token}'
# }

response = requests.get(url)
print(url)

if response.status_code == 200:
    try:
        # Tentativa de decodificar o JSON
        print(response.json())
    except ValueError:
        # Caso a resposta não seja um JSON válido
        print("A resposta não contém um corpo JSON.")
else:
    print(f'Erro na requisição: {response.status_code}')
    # Imprime o corpo da resposta para ajudar na depuração, se houver algum
    if response.text:
        print("Resposta do servidor:", response.text)
