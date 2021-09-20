from datetime import datetime

dia = datetime.today().day
hora = datetime.today().hour
ano = datetime.today().year
mes_atual = datetime.today().month


def mes():

    if mes_atual == 1:
        return 'Janeiro'
    elif mes_atual == 2:
        return 'Fevereiro'
    elif mes_atual == 3:
        return 'Março'
    elif mes_atual == 4:
        return 'Abril'
    elif mes_atual == 5:
        return 'Maio'
    elif mes_atual == 6:
        return 'Junho'
    elif mes_atual == 7:
        return 'Julho'
    elif mes_atual == 8:
        return 'Agosto'
    elif mes_atual == 9:
        return 'Setembro'
    elif mes_atual == 10:
        return 'Outubro'
    elif mes_atual == 11:
        return 'Novembro'
    elif mes_atual == 12:
        return 'Dezembro'


data_criação = f'{dia} de {mes()} de {ano}'


def data_completa_atual():
    return f'Hoje é {dia} de {mes()} de {ano} \n{hora} hora(s)'
