import requests

def get_api_response(text):
    url = f"https://hercai.onrender.com/v3/hercai?question={text}"
    response = requests.get(url)
    if response.status_code == 200:
        try:
            data = response.json()
            return data.get('reply', 'API bir yanıt döndürmedi.')
        except ValueError:
            return 'API yanıtı işlenemedi.'
    return f"API'den bir hata alındı: {response.status_code}"
