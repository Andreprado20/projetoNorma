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
        self.pc = destino - 1

    def executar_instrucoes_arquivo(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'r') as arquivo:
                linhas = arquivo.readlines()
                while self.pc <= len(linhas):
                    linha_atual = linhas[self.pc - 1].strip().split()
                    if(len(linha_atual) <= 3):
                        print(f"Fim do Programa!")
                        break
                    rotulo = int(linha_atual[0])
                    operacao = linha_atual[1]
                    registrador = linha_atual[2]
                    destino1 = int(linha_atual[3])
                    if operacao == 'ADD':
                        self.add(registrador)
                        self.desvio(destino1)
                    elif operacao == 'SUB':
                        self.sub(registrador)
                        self.desvio(destino1)
                    elif operacao == 'ZER':                        
                        self.zer(registrador)
                        destino2 = int(linha_atual[4])
                        if (self.zer(registrador) == True):
                            self.desvio(destino1)
                        else:
                            self.desvio(destino2)
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
    # a = int(input("Digite o valor para o registrador A: "))
    # b = int(input("Digite o valor para o registrador B: "))
    # c = int(input("Digite o valor para o registrador C: "))
    # d = int(input("Digite o valor para o registrador D: "))

    a = 4
    b = 0
    c = 0
    d = 0


    # arquivo = input("Digite o nome do arquivo a ser usado como input: ")

    arquivo = "fat.txt"

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

    maquina.executar_instrucoes_arquivo(arquivo)
    # maquina.mostrar_registradores()
    # maquina.zer("B")
    # maquina.mostrar_registradores()


if __name__ == "__main__":
    main()