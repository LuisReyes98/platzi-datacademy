"""
Ejercicio
"""

VALORES_MONEDAS = {
  'BOLIVAR': 4.58,
  'PESO_COLOMBIANO': 3959.60
}

COIN_NAMES = {
  'BOLIVAR': 'Bolivares',
  'PESO_COLOMBIANO': 'Pesos Colombianos'
}

SUPPORTED_COINS = [
  'PESO_COLOMBIANO',
  'BOLIVAR',
]


def convert_coin_to_usd(coin, usd_value):
    """[summary]

    Args:
        coin ([type]): [description]
        usd_value ([type]): [description]

    Returns:
        [type]: [description]
    """
    return round(coin / usd_value, 2)


if __name__ == '__main__':
    print('Conversor de Monedas')
    print("Que moneda quieres convertir?")
    MENU = """
    Opciones
    1 - Pesos Colombianos
    2 - Bolivares
    """
    opcion = input(MENU)
    opcion = int(opcion)

    current_coin = SUPPORTED_COINS[opcion - 1]
    valor_moneda = input(f"¿Cuantos {COIN_NAMES[current_coin]} tienes?: ")
    valor_moneda = float(valor_moneda)
    resultado = convert_coin_to_usd(
      valor_moneda,
      VALORES_MONEDAS[current_coin]
    )
    print(f'''Tienes {resultado} dolares''')
