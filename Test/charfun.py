import unicodedata

def esPalindromo(cadena):

    if not isinstance(cadena, str):
        raise ValueError("El argumento debe ser una cadena de texto.")
    
    # Convertir la cadena a minúsculas
    cadena = cadena.lower()
    
    # Quitar tildes
    cadena = unicodedata.normalize('NFKD', cadena)
    cadena = ''.join(c for c in cadena if unicodedata.category(c) != 'Mn')
    
    # Eliminar caracteres no alfabéticos (números, espacios y caracteres especiales)
    cadena = ''.join(c for c in cadena if c.isalpha())
    
    return cadena == cadena[::-1]
