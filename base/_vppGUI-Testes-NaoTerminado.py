# py-dss-interface é um pacote que fornece acesso às bibliotecas dll do OpenDSS para Windows
# PySimpleGUI é um pacote para implementação de interface gráfica no Python
import py_dss_interface
import PySimpleGUI as sg

class VPP:

    def janelaPrinc(self):
        # Escolha do tema da GUI
        sg.theme('DefaultNoMoreNagging')
        # Dados da janela
        layout = [  [sg.Text('Escolha quais subgrupos estarão ativados e a capacidade de geração solar')],
                    [sg.Text('SUBGRUPO A1')],
                    [sg.Radio('Ativado', 'sgrupo_a1_ativacao', key='sgrupo_a1_ativacao')],
                    [sg.Radio('Desativado', 'sgrupo_a1_ativacao', key='sgrupo_a1_ativacao')],
                    [sg.Text('Geração solar:', size=(6, 0)), sg.Input(size=(6, 0), key=('sgrupo_a1_gdsolar'))],
                    [sg.Slider(range=(0, 255), default_value=0, orientation='h', size=(12, 20),
                               key='sgrupo_a1_gdsolar_variacao')],
                    [sg.Button('Carregar configurações'), sg.Button('Rodar o OpenDSS'), sg.Button('Sair do programa')],
                    [sg.Output(size=(30,20))]
                ]

        # Cria a janela
        window = sg.Window('VPP', layout)

        # Laço para processar "eventos" e "valores" de entrada
        while True:
            event, values = window.read()

            print(values)
            # Faz a separação de cada variável
            sgrupo_a1_ativacao = values['sgrupo_a1_ativacao']
            sgrupo_a1_gdsolar = values['sgrupo_a1_gdsolar']
            sgrupo_a1_gdsolar_variacao = values['sgrupo_a1_gdsolar_variacao']
            # print(f'nomeDaVar: {Valor}')
            print(f'sgrupo_a1_ativacao: {sgrupo_a1_ativacao}')
            print(f'sgrupo_a1_gdsolar: {sgrupo_a1_gdsolar}')
            print(f'sgrupo_a1_gdsolar_variacao: {sgrupo_a1_gdsolar_variacao}')

            # Evento para fechamento da janela do programa
            if event == sg.WIN_CLOSED or event == 'Sair do programa':
                break
            
            if event == 'Rodar o OpenDSS':
                vpp.funcVersaoDSS()
                vpp.funcSolve()
                vpp.funcExibeTensoes()

        # Fecha a janela
        window.close()

    # Função que exibe a versão do programa OpenDSS
    def funcVersaoDSS(self):
        print(dss.dss_version())
        print('RODOU DENTRO DO METODO')

    # Função que define o diretorio de saida
    def funcDirDeSaida(self):
        ultimabarra = dss_arquivo.rfind('\\')
        dss_pastaarq = dss_arquivo[:ultimabarra]
        dss_saida = str(dss_pastaarq + "\saida")
        dss.text("set datapath=[" + dss_saida + "]")
        print("Arquivos de saída salvos em: " + dss_saida)
        print()

    # Função Solve que resolve o arquivo OpenDSS
    def funcSolve(self):
        dss.solution_solve()
                
    # Função que exibe as tensões dos elementos
    def funcExibeTensoes(self):
        dss.text("show voltage elements")
        #self.dssText.Command = "show voltage elements"

    # Função que exibe as potências dos elementos
    def funcExibePotencias(self):
        dss.text("show power elements")
        #self.dssText.Command = "show power elements"

# Objeto OpenDSS
dss = py_dss_interface.DSSDLL()

# Limpa a memória do programa
dss.text("clear")

# Caminho do arquivo DSS
# dss_arquivo = str(r"D:\projetos\opendss\arquivo.dss").strip()
dss_arquivo = str(r"D:\Projetos\opendss\VPP-PPGES-UPE\Cenarios05\vppbase.dss").strip()

# Compila o arquivo DSS
dss.text("compile {}".format(dss_arquivo))
print("Compilando arquivo DSS localizado em: " + dss_arquivo)

# Objeto VPP
vpp = VPP()
vpp.funcDirDeSaida()
vpp.funcSolve()
vpp.funcExibeTensoes()
vpp.funcExibePotencias()
vpp.funcVersaoDSS()

# Chama a função que exibe a versão do programa OpenDSS
print(dss.dss_version())
print('RODOU FORA DO METODO')

# Chama a janela do programa
vpp.janelaPrinc()

# Daqui em diante não roda
print(dss.dss_version())
print('RODOU FORA DO METODO2')
print(dss.dss_version())
print('RODOU FORA DO METODO3')


#Linhas principais e cargas
# dss.text("Export monitors LinhaA_potencia")
# dss.text("Plot monitor object=LinhaA_potencia channels=(1 3 5)")
# dss.text("Export monitors LinhaA_tensao")
# dss.text("Plot monitor object=LinhaA_tensao channels=(1 3 5)")
# dss.text("Export monitors CargaDistrib_potencia")
# dss.text("Plot monitor object=CargaDistrib_potencia channels=(1 3 5)")
# dss.text("Export monitors CargaDistrib_tensao")
# dss.text("Plot monitor object=CargaDistrib_potencia channels=(1 3 5)")

#Subgrupo A1
# dss.text("Export monitors linhaA1_potencia")
# dss.text("Plot monitor object=linhaA1_potencia channels=(1 3 5)")
# dss.text("Export monitors linhaA1_tensao")
# dss.text("Plot monitor object=linhaA1_tensao channels=(1 3 5)")
# dss.text("Export monitors cargaA1_potencia")
# dss.text("Plot monitor object=cargaA1_potencia channels=(1 3 5)")
# dss.text("Export monitors cargaA1_tensao")
# dss.text("Plot monitor object=cargaA1_tensao channels=(1 3 5)")
#Subgrupo A1-1
# dss.text("Export monitors barraA1-1_potencia")
# dss.text("Plot monitor object=barraA1-1_potencia channels=(1 3 5)")

#Subgrupo A2
# dss.text("Export monitors linhaA2_potencia")
# dss.text("Plot monitor object=linhaA2_potencia channels=(1 3 5)")
# dss.text("Export monitors linhaA2_tensao")
# dss.text("Plot monitor object=linhaA2_tensao channels=(1 3 5)")
# dss.text("Export monitors cargaA2_potencia")
# dss.text("Plot monitor object=cargaA2_potencia channels=(1 3 5)")
# dss.text("Export monitors cargaA2_tensao")
# dss.text("Plot monitor object=cargaA2_tensao channels=(1 3 5)")