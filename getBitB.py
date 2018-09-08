import requests

# 比特币API
bitcoin_api_url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'

response = requests.get(bitcoin_api_url)

response_json = response.json()

#The API returns a list
print(type(response_json))

#Bitcoin data is the first element of the list
print(response_json[0]["price_usd"])

#等有VPN了再玩下一步
