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
    selecionado = 0
    while(selecionado < 8):
        a = int(input("Digite o valor para o registrador A: "))
        b = int(input("Digite o valor para o registrador B: "))
        c = 0
        d = 0

        maquina = MaquinaNorma(a,b,c,d)

        print(f"--------------------")
        print(f"Menu")
        print(f"1 - Função ADD" f"2 - Função Soma" f"")
        selecionado = int(input(f"Digite a opção desejada: "))

        match selecionado:
            case 1:
                maquina.add(input("Digite o Registrador a ser incrementado "))
            case 2:
                maquina.soma()
            case 3:
                maquina.mult()
            case 4:
                maquina.sub(input("Digite o Registrador a ser decrementado "))
            case 5:
                maquina.subtrair()
            case 6:
                maquina.zer(input("Digite o Registrador a ser verificado "))
            case 7:
                maquina.executar_instrucoes_arquivo(input("Digite o nome do arquivo a ser usado como input: "))
            case 8:
                print(f"Saindo...")
                break

if __name__ == "__main__":
    main()