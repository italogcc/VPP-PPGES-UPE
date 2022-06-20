# ------------------------------------------------------------------
# Sistema fotovoltaico para simulacao de Recursos Energeticos Distribuidos em edificios
# Rede eletrica convencional, carga, geracao solar e bateria
# ------------------------------------------------------------------
# Localizar a linha: if __name__ == '__main__' e inserir o caminho do arquivo DSS
# conforme exemplo: objeto = DSS("D:\Projetos\opendss\arquivo.dss","D:\Projetos\opendss")
# ------------------------------------------------------------------

# PyWin32 para criar objetos previamente existentes (clientes) criados em outras linguagens ou componentes para servidores
# win32com é o "Common Object Model" do pywin32
import win32com.client
# matplolib - biblioteca abrangente para criar visualizações estáticas, animadas e interativas em Python
import matplotlib.pyplot as plt
# pylab - módulo da linguagem Python que permite gerar gráficos de duas dimensões
from pylab import *
# Opções para fonte pequena no matplotlib
from matplotlib.font_manager import FontProperties

# Atributos para uso no comando da legenda do gráfico
fontProp = FontProperties()
fontProp.set_size("small")

# Classe DSS
class DSS(object):

    # Construtor
    def __init__(self,dssArquivo,dssCaminho):

        # Cria uma nova instância do OpenDSS
        # Pode simplesmente fazer: self.dssObj = win32com.client.Dispatch("OpenDSSengine.DSS")
        # Fazendo uso de try/except para tratar exceções

        # Cria uma nova instância do OpenDSS
        try:
            self.dssObj = win32com.client.Dispatch("OpenDSSengine.DSS")
        except:
            print("Não foi possível iniciar o OpenDSS Engine")
            raise SystemExit

        # Inicia o OpenDSS
        if not self.dssObj.Start(0):
            print("OpenDSS falhou ao inicializar")
        else:
            # Atribui uma variável para cada interface
            self.dssText = self.dssObj.Text
            self.dssCircuit = self.dssObj.ActiveCircuit
            self.dssSolution = self.dssCircuit.Solution
            self.dssCktElement = self.dssCircuit.ActiveCktElement
            self.dssBus = self.dssCircuit.ActiveBus

        # Limpa a memória do OpenDSS ao carregar um novo circuito
        self.dssObj.ClearAll()

        # Carregar o circuito no OpenDSS
        self.dssText.Command = "Compile " + dssArquivo
        print("Compilando arquivo DSS localizado em: " + dssArquivo)

        # Configura o diretório de saída com resultados
        dssSaida = str(dssCaminho + "\Saida")
        self.dssText.Command = "set datapath=[" + dssSaida + "]"
        print("Arquivos de saída salvos em: " + dssSaida)
        print()
    
    # Função "solve" do OpenDSS
    def funcSolve(self):
        self.dssSolution.Solve()
    
    # Função da versão do OpenDSS
    def funcVersaoDSS(self):
        version = self.dssObj.Version
        return version

    # Função que exibe as tensões dos elementos
    def funcExibeTensoes(self):
        self.dssText.Command = "show voltage elements"

    # Função que exibe as potências dos elementos
    def funcExibePotencias(self):
        self.dssText.Command = "show power elements"

    # Função para plotar gráficos
    # TESTE DE PLOTAGEM VIA PYTHON
    def plot_profile(self):
        Nomes = self.dssCircuit.AllBusNames
        Vmag = self.dssCircuit.AllBusVmag
        print(Nomes)
        print(Vmag)

        # POR HORA EXIBINDO GRÁFICO EM BRANCO
        # Gráficos numa única figura
        plt.subplot(1, 1, 1)
        # Título do gráfico
        plt.title("POR HORA EXIBINDO GRÁFICO EM BRANCO")
        # Apresentação do gráfico (eixoX, eixoY, cor/tipo, rótulo)
        #plt.plot(Nomes, Vmag, "k*", label="VA")
        # Rótulo do eixo da abcissa e ordenada no gráfico
        #plt.xlabel("Barras")
        #plt.ylabel("Volt")
        # Legenda do gráfico
        # matplotlib > bbox_to_anchor - controle para o posicionamento manual da legenda
        #legend(bbox_to_anchor=(0, 0.96, 1, .102), loc=3, ncol=4, borderaxespad=0, shadow=True, fancybox=True, prop=fontProp)
        # Exibição da grade do gráfico
        grid(True)
        # Plotar gráfico
        plt.show()
      
    # Funcao para exibir os monitores do OpenDSS
    def funcMonitor(self):
        self.dssText.Command = "Export monitors linhaA1_potencia"
        self.dssText.Command = "Plot monitor object=linhaA1_potencia channels=(1 3 5)"
        self.dssText.Command = "Export monitors linhaA1_tensao"
        self.dssText.Command = "Plot monitor object=linhaA1_tensao channels=(1 3 5)"
        self.dssText.Command = "Export monitors carga_potencia"
        self.dssText.Command = "Plot monitor object=carga_potencia channels=(1 3 5)"
        self.dssText.Command = "Export monitors carga_tensao"
        self.dssText.Command = "Plot monitor object=carga_tensao channels=(1 3 5)"

if __name__ == '__main__':
    # Cria um objeto da classe DSS
    # Tem como parâmetros o caminho completo do arquivo DSS principal e o caminho do diretório onde o arquivo DSS se encontra
    # Exemplo: objeto = DSS("D:\Projetos\opendss\arquivo.dss","D:\Projetos\opendss")
    objeto = DSS("D:\Projetos\opendss\MestradoPOLI\subgrupoA1.dss","D:\Projetos\opendss\MestradoPOLI")
    
    # Comando solve
    # Realizando o comando pelo Python e o comando no OpenDSS deve estar desativado
    objeto.funcSolve()
    
    # Chama a função para plotar monitores
    objeto.funcMonitor()
        
    # Chama a função para plotar gráfico
    objeto.plot_profile()
   
    # Chama a função para exibir a tabela com as tensões
    objeto.funcExibeTensoes()
    
    # Chama a função para exibir a tabela com as potências
    objeto.funcExibePotencias()
            
    # Chama a função para exibição da versão em uso do OpenDSS
    versaoOpenDSS = objeto.funcVersaoDSS()
    print(versaoOpenDSS)