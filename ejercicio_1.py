while True:
    try:
        numero=int(input('ingresa un numero (0 para salir):'))
        if numero==0:
            print('espero verte pronto')
            break
        if numero %2==0: 
            print('es un numero par')
        else:
            print('es un nunmero impar')
    except ValueError:
        print('no te hagas el vivo sabes que eso no es un numero') 
               
                      