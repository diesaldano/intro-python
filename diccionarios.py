def run():
    diccionario_uno = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }

    # print(diccionario_uno['llave1'])
    # print(diccionario_uno['llave2'])
    # print(diccionario_uno['llave3'])

    poblacion_paises = {
        'Argentina': 44940000,
        'Brasil':   211000000,
        'Uruguay': 3462000
    }

    # print(poblacion_paises['Argentina'])

    # # Recorre y devuelve keys
    # for p in poblacion_paises.keys():
    #     print(p)

    # # Recorre y devuelve values
    # for pais in poblacion_paises.values():
    #     print(pais)

    # Recorre y devuelve keys and values
    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' hablitantes ')


if __name__ == '__main__':
    run()