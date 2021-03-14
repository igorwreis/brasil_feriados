def diatrabalho_u(arquivo, p=0, d=0):

    """
    -->> Retorna data util de acordo com relacao de feriados,
         periodo e data-base informados pelo usuario. <<--

    Args:
        arquivo ([string]): Informar caminho do diretorio mais arquivo CSV com feriados
        p (int, optional): Intervalo desejado em DIAS UTEIS (numero inteiro)
        d (int, optional): Data-Base desejada; Manter nulo para data atual

    # IMPORTANTE 1: informar todo o caminho do diretorio, acrescido
    do nome do arquivo e formato (csv). Utilizar barras invertidas (\)
    # IMPORTANTE 2: as informacoes de DATA deverao constar SEMPRE na primeira coluna do arquivo

    Returns:
        [date]
    """

    import pandas as pd
    from datetime import datetime, date, timedelta
    
    try:
        if d == 0:
            d = datetime.now().date()
            
        if type(d) == str:
            d = datetime.strptime(d, '%d/%m/%Y').date()
        
        if type(d) == datetime:
            d = d.date()
            
        if p % 1 != 0:
            print('[ERRO!] Informe um período em número INTEIRO. Mantenha os campos nulos para\n'
            'data atual e período = 0. Variáveis são aceitas desde que no formato adequado.')
            return False
        
        p = int(p)
            
        feriados = pd.read_csv(arquivo, sep=";", encoding='cp1252')
        Datas = feriados.columns[0]
        feriados[Datas] = pd.to_datetime(feriados[Datas], format='%d/%m/%Y', errors='coerce')
        
        while d in feriados.values or datetime.weekday(d) > 4:
            d = d + timedelta(days=-1)
            
        while p != 0:
            a = p/abs(p)
            d = d + timedelta(days=a)

            if d in feriados.values or datetime.weekday(d) > 4:
                p += 0
            else:
                p -= a
        
    except (ValueError, TypeError, AttributeError):
        print('[ERRO!] Insira uma data no formato DD/MM/AAAA (com barras e entre aspas) e um período em número INTEIRO.\n'
        'Mantenha os campos nulos para data atual e período = 0. Variáveis são aceitas desde que no formato adequado.')

    except FileNotFoundError:
        print('Diretório e Arquivo não encontrados!')
        
    else:
        return d

def contdiastrab_u(arquivo, f=0, i=0, u=0):

    """
    -->> Retorna quantidade de dias-uteis entre duas datas de acordo com relacao de feriados 
         informada pelo usuario em arquivo CSV, data final informada pelo
         usuario (obrigatoria) e data-base (opcional, igual a data atual se ausente) <<--

    Args:
        arquivo ([string]): Informar caminho do diretorio mais arquivo CSV com feriados
        f (data dd/mm/aaaa): data-final, obrigatoria
        i (data dd/mm/aaaa, opcional): Data-Base desejada; Manter nulo para data atual
        u (int, 0 ou 1): incluir ultima dia no calculo

    # IMPORTANTE 1: se a data-base (seja a informada ou a atual) for um dia nao-util,
        a funcao iniciara a contagem a partir do primeiro dia util anterior a esta;
        O mesmo vale para a data-final
    # IMPORTANTE 2: informar todo o caminho do diretorio, acrescido
    do nome do arquivo e formato (csv). Utilizar barras invertidas (\)
    # IMPORTANTE 3: as informacoes de DATA deverao constar SEMPRE na primeira coluna do arquivo

    Returns:
        Numero de dias uteis entre as duas datas, int
    """
    import pandas as pd
    from datetime import datetime, date, timedelta

    try:
        if f == '' or f == 0:
            print('[ERRO] INFORME PELO MENOS UMA DATA! UTILIZAR FORMATO DD/MM/AAAA ENTRE ASPAS SIMPLES')
            return False

        if type(f) == str:
            f = datetime.strptime(f, '%d/%m/%Y').date()

        if type(f) == datetime:
            f = f.date()

        if i == '' or i == 0:
            i = datetime.now().date()
    
        if type(i) == str:
            i = datetime.strptime(i, '%d/%m/%Y').date()

        if type(i) == datetime:
            i = i.date()
        
        if u not in [0, 1]:
            print('[ERRO] Utilize 1 para considerar o último dia-útil no cálculo, ou mantenha nulo.')
            return False
    
        feriados = pd.read_csv(arquivo, sep=";", encoding='cp1252')
        Datas = feriados.columns[0]
        feriados[Datas] = pd.to_datetime(feriados[Datas], format='%d/%m/%Y', errors='coerce')

        if i in feriados.values or datetime.weekday(i) > 4:
            i = i + timedelta(days=-1)

        if f in feriados.values or datetime.weekday(f) > 4:
            f = f + timedelta(days=-1)

        if f > i:
            freal = f
            ireal = i
        else:
            freal = i
            ireal = f

        cont = 0

        while ireal != freal:
            ireal = ireal + timedelta(days=1)
            if ireal in feriados.values or datetime.weekday(ireal) > 4:
                cont += 0
            else:
                cont += 1

    except (ValueError, TypeError, AttributeError):
        print('[ERRO!] Insira a data no formato DD/MM/AAAA (com barras e entre aspas).\n'
        'Mantenha data inicial nula ou 0 para data atual.')

    else:
        return cont + u
