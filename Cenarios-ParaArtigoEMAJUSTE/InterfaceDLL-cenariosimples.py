import py_dss_interface

# Objeto OpenDSS 
dss = py_dss_interface.DSSDLL()

# Limpa a memória do programa
dss.text("clear")

# Caminho do arquivo DSS
# dss_arquivo = str(r"D:\projetos\opendss\arquivo.dss").strip()
dss_arquivo = str(r"D:\Projetos\opendss\VPP-PPGES-UPE\CenarioSimples\vppbase.dss").strip()

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
dss.text("show voltage elements")
dss.text("show power elements")

# Exibe gráficos    
dss.text("Export monitors linhaA1_potencia")
dss.text("Plot monitor object=linhaA1_potencia channels=(1 3 5)")
dss.text("Export monitors linhaA1_tensao")
dss.text("Plot monitor object=linhaA1_tensao channels=(1 3 5)")
dss.text("Export monitors cargaA1_potencia")
dss.text("Plot monitor object=cargaA1_potencia channels=(1 3 5)")
dss.text("Export monitors cargaA1_tensao")
dss.text("Plot monitor object=cargaA1_tensao channels=(1 3 5)")
