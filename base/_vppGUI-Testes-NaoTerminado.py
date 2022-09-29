# py-dss-interface é um pacote que fornece acesso às bibliotecas dll do OpenDSS para Windows
# PySimpleGUI é um pacote para implementação de interface gráfica no Python
import py_dss_interface
import PySimpleGUI as sg

class VPP:

    def janelaPrinc(self):
        # Escolha do tema da GUI
        sg.theme('DefaultNoMoreNagging')
        # Dados da janela

        coluna_A1 = [
                    [sg.Text('SUBGRUPO A1')],
                    [sg.Radio('Ativado', 'sgrupo_a1_ativacao', key='sgrupo_a1_ativacao')],
                    [sg.Radio('Desativado', 'sgrupo_a1_ativacao', key='sgrupo_a1_ativacao')],
                    [sg.Text('GD-Solar:', size=(8, 0)), sg.Input(size=(6, 0), key=('sgrupo_a1_gdsolar'))],
                    [sg.Slider(range=(0, 300), default_value=0, orientation='h', size=(12, 20),
                               key='sgrupo_a1_gdsolar_variacao')],
                    [sg.Text('AD-Bateria:', size=(8, 0)), sg.Input(size=(6, 0), key=('sgrupo_a1_adbateria'))],
                    [sg.Slider(range=(0, 10), default_value=0, orientation='h', size=(12, 20),
                               key='sgrupo_a1_adbateria_variacao')],
        ]

        coluna_A2 = [
                    [sg.Text('SUBGRUPO A2')],
                    [sg.Radio('Ativado', 'sgrupo_a2_ativacao', key='sgrupo_a2_ativacao')],
                    [sg.Radio('Desativado', 'sgrupo_a2_ativacao', key='sgrupo_a2_ativacao')],
                    [sg.Text('GD-Solar:', size=(8, 0)), sg.Input(size=(6, 0), key=('sgrupo_a2_gdsolar'))],
                    [sg.Slider(range=(0, 300), default_value=0, orientation='h', size=(12, 20),
                               key='sgrupo_a2_gdsolar_variacao')],
                    [sg.Text('AD-Bateria:', size=(8, 0)), sg.Input(size=(6, 0), key=('sgrupo_a2_adbateria'))],
                    [sg.Slider(range=(0, 10), default_value=0, orientation='h', size=(12, 20),
                               key='sgrupo_a2_adbateria_variacao')],
        ]

        coluna_A3 = [
                    [sg.Text('SUBGRUPO A3')],
                    [sg.Radio('Ativado', 'sgrupo_a3_ativacao', key='sgrupo_a3_ativacao')],
                    [sg.Radio('Desativado', 'sgrupo_a3_ativacao', key='sgrupo_a3_ativacao')],
                    [sg.Text('GD-Solar:', size=(8, 0)), sg.Input(size=(6, 0), key=('sgrupo_a3_gdsolar'))],
                    [sg.Slider(range=(0, 300), default_value=0, orientation='h', size=(12, 20),
                               key='sgrupo_a3_gdsolar_variacao')],
                    [sg.Text('AD-Bateria:', size=(8, 0)), sg.Input(size=(6, 0), key=('sgrupo_a3_adbateria'))],
                    [sg.Slider(range=(0, 10), default_value=0, orientation='h', size=(12, 20),
                               key='sgrupo_a3_adbateria_variacao')],
        ]
        
        coluna_A4 = [
                    [sg.Text('SUBGRUPO A4')],
                    [sg.Radio('Ativado', 'sgrupo_a4_ativacao', key='sgrupo_a4_ativacao')],
                    [sg.Radio('Desativado', 'sgrupo_a4_ativacao', key='sgrupo_a4_ativacao')],
                    [sg.Text('GD-Solar', size=(8, 0)), sg.Input(size=(6, 0), key=('sgrupo_a4_gdsolar'))],
                    [sg.Slider(range=(0, 300), default_value=0, orientation='h', size=(12, 20),
                               key='sgrupo_a4_gdsolar_variacao')],
                    [sg.Text('AD-Bateria:', size=(8, 0)), sg.Input(size=(6, 0), key=('sgrupo_a4_adbateria'))],
                    [sg.Slider(range=(0, 10), default_value=0, orientation='h', size=(12, 20),
                               key='sgrupo_a4_adbateria_variacao')],
        ]

        layout = [
            [sg.Text('Escolha quais subgrupos estarão ativados e a capacidade de GD e AD de cada um:')],
            [
                sg.Column(coluna_A1),
                sg.VSeperator(),
                sg.Column(coluna_A2),
                sg.VSeperator(),
                sg.Column(coluna_A3),
                sg.VSeperator(),
                sg.Column(coluna_A4),
            ],
            [sg.Button('Carregar configurações'), sg.Button('Rodar o OpenDSS'), sg.Button('Sair do programa')],
            [sg.Output(size=(80, 15))]
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
            sgrupo_a1_adbateria = values['sgrupo_a1_adbateria']
            sgrupo_a1_adbateria_variacao = values['sgrupo_a1_adbateria_variacao']

            sgrupo_a2_ativacao = values['sgrupo_a2_ativacao']
            sgrupo_a2_gdsolar = values['sgrupo_a2_gdsolar']
            sgrupo_a2_gdsolar_variacao = values['sgrupo_a2_gdsolar_variacao']
            sgrupo_a2_adbateria = values['sgrupo_a2_adbateria']
            sgrupo_a2_adbateria_variacao = values['sgrupo_a2_adbateria_variacao']

            sgrupo_a3_ativacao = values['sgrupo_a3_ativacao']
            sgrupo_a3_gdsolar = values['sgrupo_a3_gdsolar']
            sgrupo_a3_gdsolar_variacao = values['sgrupo_a3_gdsolar_variacao']
            sgrupo_a3_adbateria = values['sgrupo_a3_adbateria']
            sgrupo_a3_adbateria_variacao = values['sgrupo_a3_adbateria_variacao']

            sgrupo_a4_ativacao = values['sgrupo_a4_ativacao']
            sgrupo_a4_gdsolar = values['sgrupo_a4_gdsolar']
            sgrupo_a4_gdsolar_variacao = values['sgrupo_a4_gdsolar_variacao']
            sgrupo_a4_adbateria = values['sgrupo_a4_adbateria']
            sgrupo_a4_adbateria_variacao = values['sgrupo_a4_adbateria_variacao']

            # print(f'nomeDaVar: {Valor}')
            print(f'sgrupo_a1_ativacao: {sgrupo_a1_ativacao}')
            print(f'sgrupo_a1_gdsolar: {sgrupo_a1_gdsolar}')
            print(f'sgrupo_a1_gdsolar_variacao: {sgrupo_a1_gdsolar_variacao}')
            print(f'sgrupo_a1_adbateria: {sgrupo_a1_adbateria}')
            print(f'sgrupo_a1_adbateria_variacao: {sgrupo_a1_adbateria_variacao}')

            print(f'sgrupo_a2_ativacao: {sgrupo_a2_ativacao}')
            print(f'sgrupo_a2_gdsolar: {sgrupo_a2_gdsolar}')
            print(f'sgrupo_a2_gdsolar_variacao: {sgrupo_a2_gdsolar_variacao}')
            print(f'sgrupo_a2_adbateria: {sgrupo_a2_adbateria}')
            print(f'sgrupo_a2_adbateria_variacao: {sgrupo_a2_adbateria_variacao}')

            print(f'sgrupo_a3_ativacao: {sgrupo_a3_ativacao}')
            print(f'sgrupo_a3_gdsolar: {sgrupo_a3_gdsolar}')
            print(f'sgrupo_a3_gdsolar_variacao: {sgrupo_a3_gdsolar_variacao}')
            print(f'sgrupo_a3_adbateria: {sgrupo_a3_adbateria}')
            print(f'sgrupo_a3_adbateria_variacao: {sgrupo_a3_adbateria_variacao}')

            print(f'sgrupo_a4_ativacao: {sgrupo_a4_ativacao}')
            print(f'sgrupo_a4_gdsolar: {sgrupo_a4_gdsolar}')
            print(f'sgrupo_a4_gdsolar_variacao: {sgrupo_a4_gdsolar_variacao}')
            print(f'sgrupo_a4_adbateria: {sgrupo_a4_adbateria}')
            print(f'sgrupo_a4_adbateria_variacao: {sgrupo_a4_adbateria_variacao}')

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
dss_arquivo = str(r"D:\Projetos\opendss\VPP-PPGES-UPE\vppbase-cenario08.dss").strip()

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