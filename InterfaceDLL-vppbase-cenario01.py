# py-dss-interface é um pacote que fornece acesso às bibliotecas dll do OpenDSS para Windows
import py_dss_interface

# Objeto OpenDSS 
dss = py_dss_interface.DSSDLL()

# Limpa a memória do programa
dss.text("clear")

# Caminho do arquivo DSS
# dss_arquivo = str(r"D:\projetos\opendss\arquivo.dss").strip()
dss_arquivo = str(r"D:\Projetos\opendss\VPP-PPGES-UPE\vppbase-cenario01.dss").strip()

# Compila o arquivo DSS
dss.text("compile {}".format(dss_arquivo))
print("Compilando arquivo DSS localizado em: " + dss_arquivo)

# Configura o diretório de saída com os resultados
ultimabarra = dss_arquivo.rfind('\\')
dss_pastaarq = dss_arquivo[:ultimabarra]
dss_saida = str(dss_pastaarq + "\saida")
dss.text("set datapath=[" + dss_saida + "]")
print("Arquivos de saída salvos em: " + dss_saida)
print()

# Comando solve
#dss.text("solve")
dss.solution_solve()
		
# Mostra os relatórios
dss.text("show power elements")
dss.text("show voltage elements")
dss.text("show current elements")
dss.text("show meters")

#Linhas principais e cargas
dss.text("Export monitors LinhaDistrib_potencia")
dss.text("Plot monitor object=LinhaDistrib_potencia channels=(1 3 5)")
dss.text("Export monitors LinhaDistrib")
dss.text("Plot monitor object=LinhaDistrib channels=(1 3 5)")
dss.text("Plot monitor object=LinhaDistrib channels=(7 9 11)")

dss.text("Export monitors linhaA_potencia")
dss.text("Plot monitor object=linhaA_potencia channels=(1 3 5)")
dss.text("Export monitors linhaA")
dss.text("Plot monitor object=linhaA channels=(1 3 5)")
dss.text("Plot monitor object=linhaA channels=(7 9 11)")

dss.text("Export monitors CargaDistrib_potencia")
dss.text("Plot monitor object=CargaDistrib_potencia channels=(1 3 5)")
dss.text("Export monitors CargaDistrib")
dss.text("Plot monitor object=CargaDistrib channels=(1 3 5)")
dss.text("Plot monitor object=CargaDistrib channels=(9 11 13)")

# Estudo de curto-circuito
dss.text("set mode = faultstudy")
dss.solution_solve()
dss.text("Export fault")
dss.text("Export seqz")
dss.text("show fault")


