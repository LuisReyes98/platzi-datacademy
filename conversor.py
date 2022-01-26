"""
Ejercicio
"""
VALORES_MONEDAS = {
  'BOLIVAR': 4.58,
  'PESO_COLOMBIANO': 3959.60
}


def convert_colombian_pesos_to_usd(_pesos):
    """[summary]

    Args:
        _pesos ([float]): [description]

    Returns:
        [float]: [description]
    """
    valor_dolar = 3959.60
    return round(_pesos / valor_dolar, 2)


def convert_bolivar_to_usd(_bolivares):
    """[summary]

    Args:
        _pesos ([float]): [description]

    Returns:
        [float]: [description]
    """
    valor_dolar = 4.58
    return round(_bolivares / valor_dolar, 2)


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
    if opcion == 1:
        valor_moneda = input("¿Cuantos pesos colombianos tienes?: ")
        valor_moneda = float(valor_moneda)
        print(f'Tienes {convert_colombian_pesos_to_usd(valor_moneda)} dolares')
    elif opcion == 2:
        valor_moneda = input("¿Cuantos bolivares tienes?: ")
        valor_moneda = float(valor_moneda)
        print(f'Tienes {convert_bolivar_to_usd(valor_moneda)} dolares')
