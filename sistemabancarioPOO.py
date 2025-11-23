
TAXA_TRANSFERENCIA = 3.0
conta_logada = None

class Sistema:
    def __init__(self):
        self.contas = []

    def cadastrar(self, nome, senha, cpf, datadenascimento):
        conta_nova = Conta(nome, senha, cpf, datadenascimento)
        self.contas.append(conta_nova)

    def login(self,nome,senha):
        global conta_logada
        for conta in self.contas:
            if conta.senha == senha and conta.nome == nome:
                conta_logada = conta
                return

class Conta:
    def __init__(self, nome, senha, cpf, datadenascimento):
        self.nome = nome
        self.senha = senha
        self.cpf = cpf
        self.datadedascimento = datadenascimento
        self.saldo = 0
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realiado.")
        else:
            print("Saque insuficiente.")
            
    def depositar(self, valor):
        self.saldo += valor

    def Saldo(self):
        return self.saldo

    def transferencia(self, valor, conta_receptora):
        if valor <= self.saldo:
            self.saldo -= valor
            conta_receptora.saldo += valor
            print("Transferência realizada.")
        else:
            print("Valor insuficiente para realizar a transferência.")

sistema = Sistema()

while True:
    if conta_logada == None:
        print('''Seja Bem-Vindo!
Digite 1 para Cadastrar;
Digite 2 para fazer um login;
Digite 3 para Sair.''')
        
        escolha = input(" O que deseja fazer?: ")
        if escolha == "1":
            nome = input(" Insira seu nome:")
            senha = input(" Crie sua Senha:")
            cpf = input(" Insira seu CPF:")
            datadenascimento = input(" Insira sua data de nacimento:")
            sistema.cadastrar(nome,senha,cpf,datadenascimento)
        elif escolha == "2":
            nome = input(" Digite o nome: ")
            senha = input(" Digite a senha: ")
            sistema.login(nome, senha)
        elif escolha == "3":
            print(" Você saiu")
            quit()
    else:
        print(f'''Bem vindo {conta_logada.nome}
Qual ação deseja realizar agora?
Se deseja sacar digite 1
Se deseja depósito digite 2.
Se deseja realizar uma tranferência digite 3.
Se deseja consultar o saldo digite 4.
Digite 5 para sair da conta''')
        escolha = int(input(" O que deseja fazer?"))
        if escolha == 1:
            valor = float(input("Valor do saque: "))
            conta_logada.sacar(valor) 
        elif escolha == 2:
            valor = float(input("Valor do depósito: "))
            conta_logada.depositar( valor)
        elif escolha == 3:
            destino_nome = input("Nome da conta destino: ")
            destino_cpf = input("CPF da conta destino: ")
            valor = float(input("Valor da transferência: "))

            conta_para_transferir = None
            for conta in sistema.contas:
                if conta.nome == destino_nome and conta.cpf == destino_cpf:
                    conta_para_transferir = conta
                    break
                
            if conta_para_transferir == None:
                print("Conta não encontrada.")
            else:
                conta_logada.transferencia(valor, conta_para_transferir)
                
        elif escolha == 4:
            print(f"Seu saldo é de: R$ {conta_logada.Saldo():.2f} ")
        elif escolha == 5:
            conta_logada = None
