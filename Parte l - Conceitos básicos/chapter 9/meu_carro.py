from carros import Carro

meu_novo_carro = Carro('ford','Mustang', 2020)
print(meu_novo_carro.Informações_carro())
meu_novo_carro.leitura_odometro()
meu_novo_carro.atualizar_odometro(1000)
meu_novo_carro.leitura_odometro()
meu_novo_carro.incrementar_odometro(500)
meu_novo_carro.leitura_odometro()