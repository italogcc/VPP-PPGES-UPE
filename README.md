## VPP-PPGES-UPE

Instruções para utilização:

1. Baixar o programa OpenDSS disponível em: https://sourceforge.net/projects/electricdss/

2. Baixar o Python disponível em: https://www.python.org/downloads/

3. Instalar via linha de comando os módulos para Python a seguir:
   * DSS Interface (preferencial) - Disponível por "pip install py-dss-interface" ou https://pypi.org/project/py-dss-interface/
   * win32com - Disponível por "pip install pypiwin32" ou https://pypi.org/project/pypiwin32/
   
4. Baixar o código deste repositório clicando no botão "Code">"Download ZIP" ou https://github.com/italogcc/VPP-PPGES-UPE/archive/refs/heads/main.zip

5. Editar o arquivo "InterfaceDLL-vppbase.py" ou "InterfaceCOM-vppbase.py" inserindo o caminho *path* do arquivo "vppbase.dss", ou seja, o caminho onde os arquivos foram salvos.

-----------------------------------------------------

Recomendações:

1. Para edição dos arquivos .dss, fazer as modificações em programas editores de texto para em seguida reabrí-los no OpenDSS. O objetivo é evitar erros estranhos na abertura dos arquivos.

-----------------------------------------------------

Outros programas de apoio:

1. Notepad++ - Disponível em: https://notepad-plus-plus.org/downloads/
   * Plugin para sintaxe do OpenDSS: https://sourceforge.net/p/electricdss/code/HEAD/tree/trunk/Distrib/Examples/SyntaxFiles/OpenDSS_syntax_NotepadPlusPlus.xml
