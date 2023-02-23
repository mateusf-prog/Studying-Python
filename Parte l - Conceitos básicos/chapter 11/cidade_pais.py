def cidade_e_pais(cidade, pais, population=''):
    '''Retorna a cidade, país de um modo elegante'''
    if population:
        full_name = cidade + ', ' + pais + ' - ' + str(population)
    else:
        full_name = cidade + ', ' + pais
    return full_name.title()


