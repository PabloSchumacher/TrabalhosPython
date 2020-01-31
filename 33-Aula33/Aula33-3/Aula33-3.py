from pessoa_db import listar_todos
from pessoa_converte import converter_tabela_dicionario
from pessoa_exporta import exportar_txt
from endereco_db import listar_todos
from endereco_converte import converter_tabela_dicionario
from endereco_exporta import exportar_txt


lpt = listar_todos()
lpd = converter_tabela_dicionario(lpt)
exportar_txt(lpd)
let = listar_todos()
led = converter_tabela_dicionario(let)
exportar_txt(led)