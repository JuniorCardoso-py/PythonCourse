from pessoa_db import listar_todos
from pessoa_converte import converter_tabela_dicionario
from pessoa_exporta import exportar_txt


lpt = listar_todos()
lpd = converter_tabela_dicionario(lpt)
exportar_txt(lpd)