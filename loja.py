import copy
from datetime import datetime

# Mensagens de texto que serão mostradas ao usuário

nome_vendedor_loja = 'Albert Einstein'
nome_loja = 'GUIDO VAN ROSSUM'
mensagem_boas_vindas = 'Olá, seja bem vindo(a)!\nEsta é a loja ' + nome_loja + '.\n'\
                       'Eu me chamo ' + nome_vendedor_loja + ' e vou lhe atender durante a sua compra.'

texto_input_cargo = 'Informe o cargo na empresa em que está trabalhando: '
texto_input_salario = 'Informe o salário refente ao seu cargo atual: '
texto_input_ano_nasc = 'Informe o ano do seu nascimento: '

mensagem_erro_cargo = 'Valor errado! Digite um texto que possua mais de 4 e menos de 20 caracteres. Tente novamente.'
mensagem_erro_salario = 'Valor errado! O salário precisa ser um número positivo, podendo ser decimal. Tente novamente.'
mensagem_erro_idade = 'Valor errado! A idade precisa ser um nº inteiro, positivo e maior do que 18. Tente novamente.'

mensagem_dados_cliente = '\nEstas são as informações do seu cadastro:\n' \
                         'Seu cargo atual é: {0}\nSeu salário atual é: {1}\n' \
                         'O ano do seu nascimento é {2}\nSua idade é de aproximadamente {3} anos\n' \
                         'O seu limite para compras é de {4} reais.'

texto_nome_produto = '\nInforme o nome do produto que deseja comprar: '
texto_valor_produto = 'Informe o preço do produto que acabou de informar: '
mensagem_erro_nome_produto = 'Valor errado! Tem que ser string, ser maior do que 4 e menor do que 20. Tente novamente'
mensagem_erro_valor_produto = 'Valor errado! Tem que ser float e positivo. Tente novamente'
mensagem_produto_liberado = 'Produto liberado! '
mensagem_produto_liberado2 = 'Produto liberado para parcelar em até 2 vezes. '
mensagem_produto_liberado3 = 'Produto liberado para parcelar em 3 ou mais vezes. '
mensagem_produto_bloqueado = 'Produto bloqueado! '

texto_qtde_produto = 'Quantos produtos deseja comprar? '
mensagem_erro_qtde_produto = 'Valor errado! A quantidade de produtos precisa ser um nº inteiro, positivo ' \
                            'e no máximo 20 produtos por vez. Tente novamente.'
mensagem_limite = 'Limite atualizado: {0} reais'

mensagem_dados_compra = '\nEstas são as informações da sua compra:\n' \
                        'Você informou sua intenção de comprar {0} produto(s)\n' \
                        'Preencha as informações de cada produto para realizar sua compra.\n' \
                        'A cada produto, será avaliada a liberação ou não conforme seu limite, ' \
                        'bem como a possibilidade ou não de desconto.\n'

mensagem_valor_produto = 'Valor do produto: {0} reais'

mensagem_desconto = 'Você ganhou um desconto de {0}%.\n' \
                    'O valor do produto com desconto ficou em {1} reais'

mensagem_valor_total_compra = '\nValor total da compra = R$ {0}\n'

mensagem_varios_produtos_comprados = 'Pressione qualquer tecla para concluir a compra dos produtos liberados.'
mensagem_um_produto_comprado = 'Pressione qualquer tecla para concluir a compra do produto liberado.'
mensagem_nenhum_produto_comprado = 'Nenhum produto comprado. Pressione qualquer tecla para encerrar o processo.'
mensagem_despedida = '\nObrigado por comprar na loja ' + nome_loja + '. Volte sempre!'


# classe Loja
class Loja:
    def __init__(self):
        print(mensagem_boas_vindas)


# classe Cliente
class Cliente:

    def __init__(self, cargo, salario, ano_nascimento):
        self.cargo = self.valida_cargo(cargo)
        self.salario = self.valida_salario(salario)
        self.ano_nascimento = self.valida_ano_nascimento(ano_nascimento, self.get_ano_atual())
        self.idade = self.get_idade(self.ano_nascimento)
        self.limite = self.obter_limite(self.salario, self.idade)

    def obter_limite(self, salario, idade):
        self.limite = (salario * (idade / 1000)) + 100
        return self.limite

    def get_ano_atual(self):
        return int(datetime.now().strftime("%Y"))

    def get_idade(self, ano_nascimento):
        return self.get_ano_atual() - ano_nascimento

    def valida_cargo(self, value):
        if len(value) < 4 or len(value) > 20:
            raise ValueError(mensagem_erro_cargo)
        else:
            return value

    def valida_salario(self, value):
        if value < 0:
            raise ValueError(mensagem_erro_salario)
        else:
            return value

    def valida_ano_nascimento(self, value, ano_atual):
        if (ano_atual - value) < 18:
            raise ValueError(mensagem_erro_idade)
        else:
            return value

    @classmethod
    def get_cargo(cls):
        while True:
            try:
                cls.cargo = cls.valida_cargo(cls, str(input(texto_input_cargo)))
            except ValueError:
                print(mensagem_erro_cargo)
                continue
            else:
                break
        return cls.cargo

    @classmethod
    def get_salario(cls):
        while True:
            try:
                cls.salario = cls.valida_salario(cls, float(input(texto_input_salario)))
            except ValueError:
                print(mensagem_erro_salario)
                continue
            else:
                break
        return cls.salario

    @classmethod
    def getidade(cls):
        while True:
            try:
                cls.ano_nascimento = \
                    cls.valida_ano_nascimento(cls, int(input(texto_input_ano_nasc)), cls.get_ano_atual(cls))
            except ValueError:
                print(mensagem_erro_idade)
                continue
            else:
                break
        return cls.ano_nascimento

    def mostrar_dados_cliente(self):
        print(mensagem_dados_cliente.format(self.cargo, self.salario, self.ano_nascimento, self.idade, self.limite))


# classe Produto
class Produto:
    def __init__(self, nome_produto, valor_produto):
        self.nome_produto = self.valida_nome_produto(nome_produto)
        self.valor_produto = self.valida_valor_produto(valor_produto)
        self.valor_produto_com_desconto = copy.copy(self.valor_produto)

    def valida_nome_produto(self, value):
        if len(value) < 4 or len(value) > 20:
            raise ValueError(mensagem_erro_nome_produto)
        else:
            return value

    def valida_valor_produto(self, value):
        if value < 0:
            raise ValueError(mensagem_erro_valor_produto)
        else:
            return value

    # verifica se há limite para o produto informado, liberando-o ou não
    def verificar_produto(self, limite, idade_cliente):
        liberado = True
        if self.valor_produto <= limite * 0.6:
            mensagem = mensagem_produto_liberado
        elif self.valor_produto < limite * 0.9:
            mensagem = mensagem_produto_liberado2
        elif self.valor_produto < limite:
            mensagem = mensagem_produto_liberado3
        else:
            liberado = False
            mensagem = mensagem_produto_bloqueado
        libera_desconto, mensagem_des = self.libera_desconto(liberado, idade_cliente)
        if libera_desconto:
            mensagem += mensagem_des
        else:
            mensagem += mensagem_valor_produto.format(self.valor_produto)
        return liberado, mensagem

    # verifica se há desconto ou não para o produto informado
    def libera_desconto(self, produto_liberado, idade_cliente):
        libera_desconto = False
        mensagem_desc = ''
        primeiro_nome = (nome_vendedor_loja.split()[0])
        qtde_char_prim_nome = len(primeiro_nome)
        if produto_liberado and \
                (qtde_char_prim_nome < self.valor_produto < idade_cliente
                 or idade_cliente < self.valor_produto < qtde_char_prim_nome):
            self.valor_produto_com_desconto = self.valor_produto - ((self.valor_produto * qtde_char_prim_nome) / 100)
            mensagem_desc = mensagem_desconto.format(qtde_char_prim_nome, self.valor_produto_com_desconto)
            libera_desconto = True
        return libera_desconto, mensagem_desc

    @classmethod
    def get_nome_produto(cls):
        while True:
            try:
                cls.nome_produto = cls.valida_nome_produto(cls, str(input(texto_nome_produto)))
            except ValueError:
                print(mensagem_erro_nome_produto)
                continue
            else:
                break
        return cls.nome_produto

    @classmethod
    def get_valor_produto(cls):
        while True:
            try:
                cls.valor_produto = cls.valida_valor_produto(cls, int(input(texto_valor_produto)))
            except ValueError:
                print(mensagem_erro_valor_produto)
                continue
            else:
                break
        return cls.valor_produto


# classe Compra
class Compra(Cliente):
    def __init__(self, cargo, salario, ano_nascimento, qtde_produtos):
        super().__init__(cargo, salario, ano_nascimento)
        self.qtde_produtos = self.valida_qtde_produtos(qtde_produtos)

    def valida_qtde_produtos(self, value):
        # print('validando qtde produtos ...')
        if value < 0 or value > 20:
            raise ValueError(mensagem_erro_qtde_produto)
        else:
            return value

    @classmethod
    def getcompra(cls):
        while True:
            try:
                cls.qtde_produtos = cls.valida_qtde_produtos(cls, int(input(texto_qtde_produto)))
            except ValueError:
                print(mensagem_erro_qtde_produto)
                continue
            else:
                break
        return cls.qtde_produtos

    def mostrar_dados_compra(self):
        print(mensagem_dados_compra.format(self.qtde_produtos))

    def realizar_compra(self):
        total_produtos_liberados = 0
        valor_total_compra = 0
        for i in range(self.qtde_produtos):
            produto = Produto(Produto.get_nome_produto(), Produto.get_valor_produto())
            produto_liberado, mensagem_produto = produto.verificar_produto(compra.limite, compra.idade)
            if produto_liberado:
                self.limite -= produto.valor_produto_com_desconto
                total_produtos_liberados += 1
                valor_total_compra += produto.valor_produto_com_desconto
            print(mensagem_produto)
            print(mensagem_limite.format(compra.limite))
        print(mensagem_valor_total_compra.format(valor_total_compra))
        if total_produtos_liberados > 1:
            input(mensagem_varios_produtos_comprados)
        elif total_produtos_liberados == 1:
            input(mensagem_um_produto_comprado)
        else:
            input(mensagem_nenhum_produto_comprado)
        print(mensagem_despedida)


# "abre a loja"
Loja()

# inicia a compra solicitando o cadastro do cliente, a quantidade de produtos e, para cada produto, o nome e preço
compra = Compra(Cliente.get_cargo(), Cliente.get_salario(), Cliente.getidade(), Compra.getcompra())

# mostra os dados do cliente
compra.mostrar_dados_cliente()

# mostra os dados da compra
compra.mostrar_dados_compra()

# realiza a compra
compra.realizar_compra()
