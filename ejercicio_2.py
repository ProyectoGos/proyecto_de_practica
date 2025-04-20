while True:
    try:
        años = int ( input ( 'ingrese su edad, solo numeros ' ))
        nombre = input ( 'ingrese su nombre' ).strip()
        if nombre.isdigit():
            print('solo letras no creo que su nombre tenga numeros ')
            continue
        nombre = nombre.lower()
        dias=años *365
        if años >= 18:
            print(f'{nombre} ud tiene {años} años que son {dias} dias por lo tanto es mayor de edad')
        else:
            print(f'{nombre} ud tiene {años} años que son {dias} dias por lo tanto es menor de edad')
        break
    except ValueError:
        print('elija una opcion correcta ')

    