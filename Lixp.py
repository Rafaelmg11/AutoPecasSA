import requests

Token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiYzRkMjJhMTlhZDczOTI3ZTU0YmU1ODNhZTQxNDgwMGJhMTg0YzVjNTkzMTQ2MWQ5YWY2YWM2MDE3MDc4MjExNjVhZjc1NmY5NWQ0N2EwOGQiLCJpYXQiOjE3NDc1NTMxNDMuMDY3NTgzLCJuYmYiOjE3NDc1NTMxNDMuMDY3NTg1LCJleHAiOjE3NzkwODkxNDMuMDU3MDksInN1YiI6IjllZjA1Zjc1LTQ1MmYtNGUyYy04ZDEwLTdhYmNmMjQ0MmRiOCIsInNjb3BlcyI6WyJzaGlwcGluZy1jYWxjdWxhdGUiXX0.VPVHqCnnopIPMwRSqVGUZesPFICuwsEtnCOMb3PIhIMY-9lS5HFv0dpWfB5JXsZ4dcYVzfPT0CWAPoCUmJ1IJWnTYfNeNp-enB7LsTEhsT_NXT9S3KK1CdSv5Y6xlczZWC7sqUprfGjcnq2uVrTFsUNHG64p_E1_lyBzXo-oqUql8_BtLrP6xvB0sT9cWszJ6ygox3kVs2HYpnMBOBQ1SH2eb25VNAm8ZKrIdDiYoIfwZ5MPHO6ziKgz0xAgJi7LWv-TgUgdK2wV8GlX_x4aA9qAiOTkqW7Yv6Xtzdi-MFzq3mkmNBZY-F1TZL4AOvLSN2NA867JHQSMRsANlmllFdIp47rSzdNibr4fLXeJYVl-cXaLPwZ_lRs_75gEoQ6-cLJIoVuhT4XrT-GrEaQdLVlU2KJwhpAtceaMUai-0H6Mo4YyQcEn5WRnvCyh1g7l-pbAZYHQfET2HjYl4oB7O9Xr_8mO2CIirxbV7ECcIKTqWKKJhe9swm0QMBBUfA_dHPzcO-sZFTZhEsP2Lx8HS9uIRSfRfnu-Iz4bxq4HpgWjSDmzk0xFaXtkd4_FozdNCgO7lr6Og5PyilB0TvAeZwyv4LYHPqIhFbchx38robYGjdGMhPP8pW0CUtub6Gdx0ekMl6ctlugyq_06t1baZGnWEoQfR58F7KuYu06DaJg"

# Headers obrigatórios
headers = {
"Accept": "application/json",
"Content-Type": "application/json",
"Authorization": f"Bearer {Token}"
}
# Dados da simulação
data = {
"from": {
"postal_code": "01001-000"  # CEP de origem
},
"to": {
"postal_code": "20040-020"  # CEP de destino
},
"products": [
{
"weight": 1,  # em kg
"width": 11,  # em cm
"height": 17, # em cm
"length": 20, # em cm
"insurance_value": 100.00  # valor do seguro
}
],
"services": ["1", "2"],  # IDs dos serviços (ex: 1 = PAC, 2 = SEDEX)
"options": {
"receipt": False,
"own_hand": False,
"reverse": False,
"non_commercial": True
}
}

# Requisição para cálculo de frete
response = requests.post(
"https://www.melhorenvio.com.br/api/v2/me/shipment/calculate",
headers=headers,
json=data
)
        

prazo_pac = None
preco_pac = None
prazo_sedex = None
prazo_sedex = None

# Exibe o resultado
if response.status_code == 200:
    for result in response.json():
        nometransportadora = result['name'].lower()
        if nometransportadora == 'pac':
            pac_preco = result['price']
            pac_prazo = result['delivery_time']
        elif nometransportadora == 'sedex':
            sedex_preco = result['price']
            sedex_prazo = result['delivery_time']
         


else:
    print("Erro:", response.status_code)
    print(response.json())

print(f"PAC: Preço: {pac_preco} | Prazo: {pac_prazo} dias")
print(f"SEDEX: Preço: {sedex_preco} | Prazo: {sedex_prazo} dias")
