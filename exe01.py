class Livro:
    def __init__(self, titulo='', autor='', paginas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f'{self.titulo} por {self.autor} - {self.paginas} páginas'

    @property
    def titulo_autor(self):
        return f'{self.titulo} por {self.autor}'

    def aumentar_paginas(self, quantidade):
        self.paginas += quantidade


class Pessoa:
    def __init__(self, nome='', idade='', profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome} | {self.idade} | {self.profissao}'

    def aniversario(self):
        self.idade += 1

    def saudacao(self):
        return f'ola boa tarde sua profissao e {self.profissao}'

livro = Livro(titulo='Senhor dos aneis', autor='pablo marcal', paginas=100)
print(livro)
livro.aumentar_paginas(quantidade= 10)
print(livro)

pessoa = Pessoa(nome='calebe', idade='20', profissao='eletrecista')
print(pessoa)
print(pessoa.saudacao())
pessoa.aniversario()
print(pessoa)