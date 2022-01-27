"""
Un palindromo es una palabra o frase que
se lee igual de izquierda a derecha
que de derecha a izquierda.
"""


def palindromo_check(palabra):
    """[summary]

    Args:
        palabra ([type]): [description]

    Returns:
        [type]: [description]
    """
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()

    return palabra == palabra[::-1]


def run():
    """
      Main function
    """
    word = input('Escribe una palabra: ')
    is_palindromo = palindromo_check(word)

    if is_palindromo:
        print(f'{word} es un palindromo')
    else:
        print(f'{word} no es un palindromo')


if __name__ == '__main__':
    run()
