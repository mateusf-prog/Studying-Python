def new_user(nome, sobrenome, **infos):
    perfil = {}
    perfil['nome'] = nome
    perfil['sobrenome'] = sobrenome
    for chave, valor in infos.items():
        perfil[chave] = valor
    return perfil