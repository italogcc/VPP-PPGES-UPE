#Universidade de Pernambuco - UPE
#Escola Politécnica de Pernambuco - POLI
#Programa de Pós Graduação Engenharia de Sistemas - PPGES
#Aluno: Italo Garcia Campos do Canto
#Tema: Plataforma Computacional em OpenDSS para simulação de Agregadores
#	   e Usinas Virtuais de Microrredes Urbanas
#	   Recife-PE, 2022
# ------------------------------------------------------------------
# Localizar a linha: if __name__ == '__main__' e inserir o caminho do arquivo DSS
# conforme exemplo: objeto = DSS("D:\Projetos\opendss\arquivo.dss","D:\Projetos\opendss")
# ------------------------------------------------------------------

# PyWin32 para criar objetos previamente existentes (clientes) criados em outras linguagens ou componentes para servidores
# win32com é o "Common Object Model" do pywin32
import win32com.client

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
        dssSaida = str(dssCaminho + "\saida")
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
    
    # Funcao para exibir os monitores do OpenDSS
    def funcMonitor(self):
        self.dssText.Command = "Export monitors linhaA1_potencia"
        self.dssText.Command = "Plot monitor object=linhaA1_potencia channels=(1 3 5)"
        self.dssText.Command = "Export monitors linhaA1_tensao"
        self.dssText.Command = "Plot monitor object=linhaA1_tensao channels=(1 3 5)"
        self.dssText.Command = "Export monitors cargaA1_potencia"
        self.dssText.Command = "Plot monitor object=cargaA1_potencia channels=(1 3 5)"
        self.dssText.Command = "Export monitors cargaA1_tensao"
        self.dssText.Command = "Plot monitor object=cargaA1_tensao channels=(1 3 5)"
        self.dssText.Command = "Export monitors linhaA2_potencia"
        self.dssText.Command = "Plot monitor object=linhaA2_potencia channels=(1 3 5)"
        self.dssText.Command = "Export monitors linhaA2_tensao"
        self.dssText.Command = "Plot monitor object=linhaA2_tensao channels=(1 3 5)"
        self.dssText.Command = "Export monitors cargaA2_potencia"
        self.dssText.Command = "Plot monitor object=cargaA2_potencia channels=(1 3 5)"
        self.dssText.Command = "Export monitors cargaA2_tensao"
        self.dssText.Command = "Plot monitor object=cargaA2_tensao channels=(1 3 5)"

if __name__ == '__main__':
    # Cria um objeto da classe DSS
    # Tem como parâmetros o caminho completo do arquivo DSS principal e o caminho do diretório onde o arquivo DSS se encontra
    # Exemplo: objeto = DSS(r"D:\Projetos\opendss\arquivo.dss",r"D:\Projetos\opendss")
    objeto = DSS(r"D:\Projetos\opendss\Cenarios05\vppbase.dss",r"D:\Projetos\opendss\Cenarios05")
    
    # Comando solve
    # Realizando o comando pelo Python e o comando no OpenDSS deve estar desativado
    objeto.funcSolve()
    
    # Chama a função para plotar monitores
    objeto.funcMonitor()
   
    # Chama a função para exibir a tabela com as tensões
    objeto.funcExibeTensoes()
    
    # Chama a função para exibir a tabela com as potências
    objeto.funcExibePotencias()
            
    # Chama a função para exibição da versão em uso do OpenDSS
    versaoOpenDSS = objeto.funcVersaoDSS()
    print(versaoOpenDSS)