class MaquinaNorma:

    def __init__(self, valorA, valorB, valorC, valorD):
        # Inicializa os registradores
        self.registradores = {'A': valorA, 'B': valorB, 'C': valorC, 'D': valorD}
        self.pc = 1

    def add(self, registrador):
        self.registradores[registrador] += 1

    def soma(self):
        # Soma o valor de um registrador a outro
        self.registradores["C"] = self.registradores["A"] + self.registradores["B"]
        self.registradores["A"] = 0
        self.registradores["B"] = 0

    def mult(self):
        self.registradores["A"] = self.registradores["A"] * self.registradores["B"]
        self.registradores["C"] = 0
        self.registradores["D"] = 0

    def sub(self, registrador):
        self.registradores[registrador] -= 1

    def subtrair(self, destino, origem):
        # Subtrai o valor de um registrador de outro
        self.registradores[destino] -= self.registradores[origem]

    def zer(self, registrador):
        return self.registradores[registrador] == 0
    
    def desvio(self, destino):
        self.pc = destino

    def executar_instrucoes_arquivo(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'r') as arquivo:
                linhas = arquivo.readlines()
                while self.pc <= len(linhas):
                    linha_atual = linhas[self.pc - 1].strip().split()

                    rotulo = int(linha_atual[0])
                    operacao = linha_atual[1]
                    registrador = linha_atual[2]

                    if operacao == 'ADD':
                        self.add(registrador)
                    elif operacao == 'JUMP':
                        destino = int(linha_atual[3])
                        self.desvio(destino)
                    else:
                        print(f'Operação desconhecida: {operacao}')

                    self.mostrar_registradores()
                    self.pc += 1

        except FileNotFoundError:
            print(f'O arquivo {nome_arquivo} não foi encontrado.')
    
    def mostrar_registradores(self):
        # Mostra os valores atuais dos registradores
        for registro, valor in self.registradores.items():
            print(f'{registro}: {valor}', end='  ')
        print()


def main():
    a = int(input("Digite o valor para o registrador A: "))
    b = int(input("Digite o valor para o registrador B: "))
    c = int(input("Digite o valor para o registrador C: "))
    d = int(input("Digite o valor para o registrador D: ")),

    maquina = MaquinaNorma(a,b,c,d)

    # maquina.add("A")
    # assert maquina.registradores["A"] == 1
    # maquina.mostrar_registradores()

    # maquina.sub("B")
    # assert maquina.registradores["B"] == 0
    # maquina.mostrar_registradores()

    # # assert maquina.zero("A") is False
    # # assert maquina.zero("B") is True
    # maquina.mostrar_registradores()
    # maquina.soma()
    # maquina.mostrar_registradores()

    maquina.executar_instrucoes_arquivo('programa.txt')
    maquina.mostrar_registradores()


if __name__ == "__main__":
    main()