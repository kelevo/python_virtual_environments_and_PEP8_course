import urllib.request
import urllib.parse
import json

"""
Sistema de analisis de noticias con APIs multiples
"""

# PEP 8: Configuracion centralizada - constantes en MAYUSCULAS con guiones bajos
API_TIMEOUT = 30
MAX_RETRIES = 3
DEFAULT_LANGUAGE = "es" # PEP 8: Comillas dobles para strings 
API_KEY = "9b2fdaebec964dc6b24a516d32f79070"
BASE_URL = "https://newsapi.org/v2/everything"

# PEP 8: Utilidades comunes del proyecto - funciones en snake_case
def clean_text(text):
    # PEP 8: 4 espacios por identacion, no tabs
    """Limpia y normaliza el texto de entrada.""" # PEP 8: Docstrsings en comillas dobles triples
    if not text:
        return ""
    return text.strip().lower()


# PEP 8: Doble linea en blanco entre gunciones para separar logicamente
def validate_api_key(api_key):
    """Valida que el API key tenga formato correcto."""
    return len(api_key) == 10 and api_key.isalnum()


# PEP 8: Funciones principales - agrupadas despues de utilidades
def fetch_news_from_api(api_name, query):
    """Obtiene noticias de un API especifico."""
    pass


def process__article_data(raw_data):
    """Procesa datos crudos de articulos."""
    pass


def guardian_client(api_key, section, from_date, timeout = 30, retries = 4):
    return f"Guardian {section} desde {from_date} con timeout {timeout}"


def ejemplo_args(api_key, *args):
    print(f"API KEY: {api_key}")
    print(f"Todos los args {args}")
    print(f"{type(args)}")


def add_all_numbers(*args):
    total = sum(
        arg
        for arg in args
        if isinstance(arg, (int, float))
    )

    print(f"La suma total de los argumentos es: {total}")

# ejemplo_args("API_KEY_VALUE", "Este", "parametro", "aca")
# ejemplo_args("API_KEY_VALUE", "Hola", "mundo")

# print()

# add_all_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)


def ejemplo_kwargs(**kwargs):
    print(f"kwargs: {type(kwargs)}")
    print(f"{kwargs}")
    print("=========")

# ejemplo_kwargs(key="value", llave="valor")

class NewsSystemError(Exception):
    """Error general en la app"""
    pass

class APIKeyError(NewsSystemError):
    """Error para API Key invalida"""
    pass

def news_api_client(api_key, query, timeout = 30, retries = 4):
    query_string = urllib.parse.urlencode({"q": query, "apiKey": api_key})
    url = f"{BASE_URL}?{query_string}"

    try:
        with urllib.request.urlopen(url, timeout = timeout) as response:
            data = response.read().decode("utf-8")
            return json.loads(data)
    except urllib.error.HTTPError:
        raise APIKeyError("Ocurrio un error, el API Key es invalido")

    return f"NewsAPI: {query} con timeout {timeout}"


def fetch_news(api_name, *args, **kwargs):
    """
        Funcion flexible para conectar con la API
    """

    base_config = {
        "timeout": 30,
        "retries": 4
    }

    config = {
        **base_config,
        **kwargs
    }

    api_clients = {
        "newapi": news_api_client,
        "guardian": guardian_client
    }
    
    client = api_clients[api_name]
    return client(*args, **config)


response_data = None

try:
    response_data = fetch_news("newapi", api_key = API_KEY, query = "Python")
except APIKeyError as e:
    print(f"{e}")

if response_data:
    for article in response_data["articles"]:
        print(article["title"])