from operator import truediv


def password():
    """
    Ejercicio 10 - Validador de Contraseña

    Leer una contraseña mediante input(). Validar que cumpla con los siguientes requisitos:
    1. Debe tener al menos 8 caracteres de longitud
    2. Debe contener al menos un número (usar el operador in para verificar cada dígito del 0 al 9)

    Si cumple ambos requisitos, imprimir "Contraseña valida".
    Si no cumple, imprimir cuál requisito falta.

    Ejemplo:
        Para la entrada "abc12345", la salida esperada es:
        Contraseña valida

        Para la entrada "abc123", la salida esperada es:
        Contraseña muy corta

        Para la entrada "abcdefgh", la salida esperada es:
        Debe contener un numero

        Para la entrada "abc", la salida esperada es:
        Contraseña muy corta
        Debe contener un numero
    """
    contra = input()

    if len(contra) >= 8 and ('1' in contra or '2' in contra or '3' in contra or '4' in contra or '5' in contra or '6' in contra or '7' in contra or '8' in contra or '9' in contra or '0' in contra):
        print("Contraseña valida")
    elif len(contra) < 8 and ('1' in contra or '2' in contra or '3' in contra or '4' in contra or '5' in contra or '6' in contra or '7' in contra or '8' in contra or '9' in contra or '0' in contra):
        print("Contraseña muy corta")
    elif len(contra) >= 8 and not ('1' in contra or '2' in contra or '3' in contra or '4' in contra or '5' in contra or '6' in contra or '7' in contra or '8' in contra or '9' in contra or '0' in contra):
        print("Debe contener un numero")
    else:
        print("Contraseña muy corta")
        print("Debe contener un numero")
