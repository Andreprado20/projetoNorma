# projetoNorma

## Descrição:

 - [ ] Este Repositório contém um projeto de um simulador de uma Máquina Norma feito na linguagem Python

 - [ ] Este projeto contém dois conjuntos de arquivos: um conjunto contendo apenas um arquivo Python chamado maquinaNorma.py com o código de funcionamento do programa e um outro conjunto de arquivos .txt contendo:

 - [ ] **soma.txt** --> um arquivo de texto contendo as instruções em formato de um programa monolítico que faz a soma dos valores contidos nos registradores "A" e "B" e armazena o resultado da soma no Registrador "C", deixando os Registradores "A" e "B" zerados após a operação.

 - [ ] **mult.txt** --> um arquivo de texto contendo as instruções em formato de um programa monolítico que faz a multiplicação dos valores contidos nos registradores "A" e "B" e armazena o produto no Registrador "A", deixando os Registradores "C" e "D" zerados após a operação.

 - **fat.txt** --> um arquivo de texto contendo as instruções em formato de um programa monolítico que faz o cáculo fatorial do valor contido no registrador "A" e armazena o resultado no Registrador "A".
 **OBS: Para que essa função funcione corretamente o usuário deve informar o valor 0 (zero) no Registrador B**
 
 - [ ] O programa em Python vai inicializar os registradores A e B com valores informados pelo usuário e os Registradores C e D com valor igual a 0(zero) e vai executar as instruções contidas no arquivo de Texto escolhido e de acordo com a lógica do programa monolítico contido nele.

 ## Como usar:

 - [ ] Para Rodar esse Programa é necessário baixar esse projeto em um sistema operacional que contenha o Python (de preferência na Versão 3) baixado localmente.

- Ao rodar o programa no Terminal será impressa uma mensagem para que o usuário informe o valor desejado para inicializar os registradores "A" e "B"

- Em seguida, será impressa uma mensagem pedindo para escolher qual a operação desejada. As 6 primeiras opções são feitas no próprio terminal para testar as funções da Máquina Norma. O ponto chave deste projeto está na opção 7 desse Menu, que vai pedir para o usuário inserir o nome do arquivo de texto (contendo a extensão do arquivo) que contenha o código do Programa Monolítico a ser executado pela máquina.

- Para sair do Programa, basta digitar a opção 8 do Menu.

 ## Funcionamento:

 - [ ] Essa Máquina Norma executa todas as suas Funções Macro em programas monolíticos baseado apenas em 3 operações básicas: 
 
    | Função |  Descrição  |
    |-------------|--------|
    |     ADD     |  Incrementa o valor de um dado Registrador em uma unidade  |
    |     SUB    | Decrementa o valor de um dado Registrador em uma unidade |
    |     ZER     | Verifica se o valor de um dado Registrador é igual a Zero ou não |

 ## Future Features:

 - [ ] Em breve vamos acrescentar na documentação deste projeto o passo a passo de instalação do Python e da configuração do Pythone de Git/GitHub para conseguir executar esse programa. Por enquanto, segue a orientação de instalação de Python no Windows nesse [link](https://python.org.br/instalacao-windows/)
 - [ ] Mais para frente esse programa será integrado a um código de frontend usando o framework [PyScript](https://pyscript.net/)
