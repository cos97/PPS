from charfun import esPalindromo

def main():
    print("Programa que verifica si una frase es palíndroma.")
    terminar = True
    
    while terminar:
        frase = input("Introduce una frase (o escribe 'salir' para terminar): ")
        
        if frase.lower() == "salir":
            print("Programa finalizado.")
            terminar = False

        elif esPalindromo(frase):
            print("La frase es palíndroma.")
        else:
            print("La frase no es palíndroma.")

if __name__ == "__main__":
    main()
