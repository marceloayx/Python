produto={}
atualizar={}
atualizar[0]=0
codig={}
total_saldo={}
total_saldo[0]=0
cliente=0
clientes={}
arquivo=open("codigos.txt","a")
arquivo.close()
def rep(nome,codigo):
    cod=1
    codi={}
    while cod==1:
        u=0
        arquivo=open("codigos.txt","r")
        codi=arquivo.readlines()
        for p in range(len(codi)):
            lincod=int(codi[p])
            if codigo == lincod:
                print("Esse codigo ja esta cadastrado em outro produto")
                codigo=int(input(f"DIGITE O CODIGO DO(a) {nome}: "))
                u+=1
        arquivo.close()
        if u !=1:
            codig[1+len(codig)]=(codigo)
            cod+=1
            arquivo=open("codigos.txt","a")
            arquivo.write(f"{codigo}\n")
            arquivo.close()


def linha():
    print("--------------------------------------------")


def cadastro(codigo,nome,preco,quantidade,massa):
    if massa==1:
        produto[len(produto)+1]=(f"codigo: {codigo} / preço: {preco} / quantidade: {quantidade}L / produto: {nome} ")
        arquivo=open("nome.txt","a")
        arquivo.write(f"{nome}\n")
        arquivo.close()
        arquivo=open("quantidade.txt","a")
        arquivo.write(f"{quantidade}\n")
        arquivo.close()
        arquivo=open("preco.txt","a")
        arquivo.write(f'{preco}\n')
        arquivo.close()
        arquivo=open("codigis1.txt","a")
        arquivo.write(f'{codigo}\n')
        arquivo.close()
        atualizar[0]=1
    if massa==2:
        produto[len(produto)+1]=(f"codigo: {codigo} / preço: {preco} / quantidade: {quantidade}KG / produto: {nome} ")
        arquivo=open("nome.txt","a")
        arquivo.write(f"{nome}\n")
        arquivo.close()
        arquivo=open("quantidade.txt","a")
        arquivo.write(f"{quantidade}\n")
        arquivo.close()
        arquivo=open("preco.txt","a")
        arquivo.write(f'{preco}\n')
        arquivo.close()
        arquivo=open("codigis1.txt","a")
        arquivo.write(f'{codigo}\n')
        arquivo.close()
        atualizar[0]=1
    if massa==3:
        produto[len(produto)+1]=(f"codigo: {codigo} / preço: {preco} / quantidade: {quantidade} uni / produto: {nome} ")
        arquivo=open("nome.txt","a")
        arquivo.write(f"{nome}\n")
        arquivo.close()
        arquivo=open("quantidade.txt","a")
        arquivo.write(f"{quantidade}\n")
        arquivo.close()
        arquivo=open("preco.txt","a")
        arquivo.write(f'{preco}\n')
        arquivo.close()
        arquivo=open("codigis1.txt","a")
        arquivo.write(f'{codigo}\n')
        arquivo.close()
        atualizar[0]=1
    if massa==0:
        massa=0
    

def arqui():
    for j in range (1,len(produto)+1):
        arquivo=open("estoque.txt","a")
        arquivo.write(f"{produto[j]}\n")
        arquivo.close()
    atualizar[0]=0


def menu():
    print("")
    linha()
    print("1-CADASTRAR PRODUTO")
    linha()
    print("2-MOSTRAR TABELA DOS PRODUTOS")
    linha()
    print('3-SALVAR O ESTOQUE EM UM ARQUIVO')
    linha()
    print('4-FAZER UMA COMPRA')
    linha()
    print("5-FINALIZAR O DIA")
    linha()

def cadastrar_produto():
    if opcao==1:
        print("")
        linha()
        print("CADASTRAR PRODUTO")
        linha()
        print("")
        nome=input("DIGITE O NOME DO PRODUTO: ")
        codigo=int(input(f"DIGITE O CODIGO DO(a) {nome}: "))
        rep(nome,codigo)
        codigo=codig[len(codig)]
        print("A quantidade será em volume(mL),massa(g) ou em unidade(uni)?")
        massa=int(input("Digite 1 para volume(mL),2 para massa(g) ou 3 para unidade(uni): "))
        arquivo=open("massa.txt","a")
        arquivo.write(f"{massa}\n")
        arquivo.close()
        while massa !=1 and massa!=2 and massa!=3:
            print("Opção inválida")
            massa=int(input("Digite 1 para volume(mL),2 para massa(g) ou 3 para unidade(uni): "))
        if massa==1:
            quantidade=int(input("DIGITE A QUANTIDADE EM VOLUME(L): "))
            preco=float(input(f"DIGITE O PREÇO DO(a) {nome} por Litro: "))
        if massa==2:
            quantidade=int(input("DIGITE A QUANTIDADE EM MASSA (KG): "))
            preco=float(input(f"DIGITE O PREÇO DO(a) {nome} POR QUILORAMA: "))
        if massa==3:
            quantidade=int(input("DIGITE A QUANTIDADE EM UNIDADE: "))
            preco=float(input(f"DIGITE O PREÇO DO(a) {nome} POR UNIDADE: "))
        cadastro(codigo,nome,preco,quantidade,massa)
        print(f"{nome} cadastrado com sucesso")

        
def pagamento(somatotal):
    form=0
    while form == 0:
        forma=int(input("digite 1 para dinheiro ou 2 para cartao: "))
        if forma!= 1 and forma!=2:
            print("opcao invalida, tente novamente")
            forma=int(input("digite 1 para dinheiro ou 2 para cartao: "))
        else:
            form = 1
    if forma==1:
        dinheiro=int(input("digite quanto foi pago: "))
        troco=dinheiro-somatotal
        print(f"troco do cliente: R${troco}")
        print("Compra realizada com sucesso")
    if forma==2:
        parcelas=int(input("quantas vezes será parcelado? "))
        if parcelas<1 or parcelas>4:
            print("opcao invalida, tente novamente")
            parcelas=int(input("quantas vezes será parcelado? "))
        else:
            totalcartao=somatotal+somatotal*0.0357
            cadaparcela=totalcartao/parcelas
            print(f"total da compra: R${totalcartao:.2f}")
            print(f"Valor de cada parcela: R${cadaparcela:.2f} ")
            print("Compra realizada com sucesso")


def compra(cliente):
    clientes[len(clientes)]=(cliente)
    compr=0
    soma=0
    somatotal=0
    acu=0
    agu=0
    acu=0
    while compr==0:
        codigo=int(input("Codigo do produto: "))
        while acu==0:
            agu=0
            arquivo=open("codigis1.txt","r")
            procurar=arquivo.readlines()
            for linha in procurar:
                if str(codigo) in linha:
                    acu+=1
                    aqui=agu   
                agu+=1
            arquivo.close()
            if acu==0:
                print("Esse código ainda não foi cadastrado, tente novamente")
                codigo=int(input("Codigo do produto: "))
        arquivo=open("massa.txt","r")
        massas=arquivo.readlines()
        if int(massas[aqui])==3:
            tipo=("uni")
            quant=int(input("Quantidade do produto: "))
            arquivo=open("quantidade.txt","r")
            linhas=arquivo.readlines()
            if len(linhas)>0:
                prodquant=int(linhas[aqui])-quant
            arquivo.close()
        if int(massas[aqui])==2:
            item=("KG")
            quant=float(input("Quantidade do produto: "))
            arquivo=open("quantidade.txt","r")
            linhas=arquivo.readlines()
            if len(linhas)>0:
                prodquant=float(linhas[aqui])-quant
            arquivo.close()
        if int(massas[aqui])==1:
            item=("L")
            quant=float(input("Quantidade do produto: "))
            arquivo=open("quantidade.txt","r")
            linhas=arquivo.readlines()
            if len(linhas)>0:
                prodquant=float(linhas[aqui])-quant
            arquivo.close()
        arquivo.close()
        arquivo=open("quantidade.txt","r")
        linhas=arquivo.readlines()
        if len(linhas)>0:
            linhas[aqui]=(f"{prodquant}\n")
        arquivo=open("quantidade.txt","w")
        for linha in linhas:
            arquivo.write(linha)
        arquivo.close()
        arquivo.close()
        nome1=[]
        arquivo=open("nome.txt","r")
        linhas=arquivo.readlines()
        if len(linhas)>0:
            nome1=str(linhas[aqui])
        arquivo.close()
        arquivo=open("preco.txt","r")
        linhas=arquivo.readlines()
        if len(linhas)>0:
            preco1=float(linhas[aqui])
        arquivo.close()
        soma=preco1*quant
        somatotal=somatotal+soma
        novostok=(f"codigo: {codigo} / preço: {preco1} / quantidade: {prodquant}{item} \ produto: {nome1}")
        arquivo=open("estoque.txt","r")
        linhas=arquivo.readlines()
        if len(linhas)>0:
            linhas[aqui]= novostok
        arquivo=open("estoque.txt","w")
        for linha in linhas:
            arquivo.write(linha)
        arquivo.close()
        arquivo.close()
        continuar=int(input("digite 1 para continuar comprando e 2 para parar de comprar: "))
        if continuar!= 1 and continuar!=2:
            print("opcao invalida, tente novamente")
            continuar=int(input("digite 1 para continuar comprando e 2 para parar de comprar: "))
        if continuar==2:
            compr=1
            print(f"total da compra: R${somatotal}")
        if continuar==1:
            acu=0
    total_saldo[0]=total_saldo[0]+somatotal
    pagamento(somatotal)


def finalizar_dia():
        dia=int(input("Informe o dia de hoje: "))
        mes=int(input("Informe o mes de hoje: "))
        ano=int(input("Informe o ano de hoje: "))
        finalizar=(f"{dia}/{mes}/{ano}: total de clientes: {len(clientes)} e saldo total do dia: R${total_saldo[0]}")
        arquivo=open("dados_de_venda.txt","a")
        arquivo.write(f"{finalizar}"+"\n")
        arquivo.close()


opcao=1    #Codigo principal
tabela=[]
while opcao!=0:
    menu()
    opcao=int(input("ESCOLHA UMA DAS OPÇÕES ACIMA: "))
    if opcao==1:
        cadastrar_produto()
        while opcao==1:
            cont=(int(input("Digite 1 para continuar cadastrando porodutos e 2 para voltar pro menu anterior: ")))
            if cont <=0 or opcao>2:
                print("Opção inválida")
            if cont==1:
                cadastrar_produto()
            if cont==2:
                opcao=7
    if opcao==2:
        print("")
        linha()
        print("TABELA DE PRODUTO")
        linha()
        print("")
        arquivo=open("estoque.txt","r")
        estok=arquivo.readlines()
        for estok in estok:
            print(estok)
        arquivo.close()
    if opcao==3:
        print("")
        linha()
        print("ESTOQUE SALVO NO ARQUIVO")
        linha()
        print("")
        if atualizar[0]==1:
            arqui()
            produto={}
        else:
            produto={}
    if opcao==4:
        print("")
        linha()
        print("FAZER UMA COMPRA")
        linha()
        print("")
        compra(cliente)
    if opcao==5:
        print("")
        linha()
        print("FINAIZAR DIA")
        linha()
        print("")
        finalizar_dia()
        opcao=0