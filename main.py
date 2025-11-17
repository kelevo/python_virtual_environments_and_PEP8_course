# main.py - Todo el codigo en un solo archivo

"""
Sistema de analisis de noticias con APIs multiples
"""

# PEP 8: Configuracion centralizada - constantes en MAYUSCULAS con guiones bajos
API_TIMEOUT = 30
MAX_RETRIES = 3
DEFAULT_LANGUAGE = 'es' # PEP 8: Comillas dobles para strings 

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


def news_api_client(api_key, query, timeout = 30, retries = 4):
    return f"NewsAPI: {query} con timeout {timeout}"


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

ejemplo_args("API_KEY_VALUE", "Este", "parametro", "aca")
ejemplo_args("API_KEY_VALUE", "Hola", "mundo")

print()

add_all_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

