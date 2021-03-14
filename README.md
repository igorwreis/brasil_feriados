# brasil_feriados
Funções cujo objetivo é auxiliar no tratamento de datas de acordo com o calendário de feriados do mercado financeiro brasileiro,
especialmente para fins de precificação de ativos.

As funções presentes em 'feriados_brasil.py' já utilizam uma lista de feriados (presente na função 'feriados_lista()').
As datas desta relação podem ser encontradas em https://www.anbima.com.br/feriados/feriados.asp

Já as funções em 'feriados_usuario.py' trabalham com uma relação de feriados informada pelo usuário,
o que deve ser feito a partir de um arquivo em formato .csv, em que as informações de feriados já
estejam em formato de data e devem constar obrigatoriamente na primeira coluna do arquivo. É importante também
observar que qualquer outra informação neste arquivo que não sejam as datas poderá afetar o funcionamento das funções.


