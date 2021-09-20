import PySimpleGUI as sg
from lib import icones, arquivo
from lib.data import data_completa_atual


sg.set_global_icon('img\\logo_canto.ico')


def janela_de_boas_vinda():
    sg.theme('DefaultNoMoreNagging')

    coluna_imagem = [
        [sg.Image('img\\imagem de boas vindasescalada.png')]
    ]
    coluna_dos_icones_links = [
        [sg.Button('', image_data=icones.icone_facebook, button_color=(sg.theme_background_color(), sg.theme_background_color()), key='-ICONE_FACEBOOK-', border_width=2, enable_events=True)],
        [sg.Button('', image_data=icones.icone_intragram, button_color=(sg.theme_background_color(), sg.theme_background_color()), key='-ICONE_INSTAGRAM-', border_width=2, enable_events=True)],
        [sg.Button('', image_data=icones.icone_youtube, button_color=(sg.theme_background_color(), sg.theme_background_color()), key='-ICONE_YOUTUBE-', border_width=2, enable_events=True)]
    ]
    coluna_dos_botoes = [
        [sg.Button('Entrar no Sistema', button_color=('', 'blue'), font='Quicksand', key='-BOTAO_ENTRAR_SISTEMA-', border_width=0, enable_events=True),
         sg.Button('Fechar', button_color=('', 'red'), font='Quicksand', key='-BOTAO_FECHAR-', border_width=0, enable_events=True)]
    ]

    layout = [
        [sg.Column(coluna_imagem), sg.Column(coluna_dos_icones_links)],
        [sg.HorizontalSeparator()],
        [coluna_dos_botoes],
    ]
    return sg.Window('SMS - School Management System', layout=layout, finalize=True)


def janela_menu_casa():
    sg.theme('DefaultNoMoreNagging')
    nome = 'arquivostxt\\Nome da Escola.txt'
    if arquivo.arquivoExiste(nome):
        '''
        Tabelas dos Cursos e Alunos Cadastrados
        '''

        # Tabela dos Cursos
        cursos_cadastrados = 'arquivostxt\\Cursos Cadastrados.txt'
        if arquivo.arquivoExiste(cursos_cadastrados):
            arquivo_cursos = open(cursos_cadastrados, 'rt', encoding='utf-8')
            ler_cursos = arquivo_cursos.readlines()
        else:
            ler_cursos = 'Sem Cursos Cadastrados'

        # Tabela dos Alunos
        alunos_cadastrados = 'arquivostxt\\Alunos Cadastrados.txt'
        if arquivo.arquivoExiste(alunos_cadastrados):
            arquivo_alunos = open(alunos_cadastrados, 'rt', encoding='utf-8')
            ler_alunos = arquivo_alunos.readlines()
        else:
            ler_alunos = 'Sem Alunos Cadastrados'

        '''
        Contador dos Cursos, Professores, alunos e salas Cadastradas,
         se não houver nenhum ficheiro, o resultado será '0' 
        '''

        # Número de salas cadastradas
        salas_cadastradas = 'arquivostxt\\Salas Cadastradas.txt'
        if arquivo.arquivoExiste(salas_cadastradas):
            arquivo_salas = open(salas_cadastradas, 'rt', encoding='utf-8')
            ler_salas = arquivo_salas.readlines()
            cont_salas = 0
            for salss in ler_salas:
                cont_salas += 1
            numero_de_salas = cont_salas
        else:
            numero_de_salas = 0

        # Número de Cursos Cadastrados
        if arquivo.arquivoExiste(cursos_cadastrados):
            arquivo_cursos = open(cursos_cadastrados, 'rt', encoding='utf-8')
            ler_cursos = arquivo_cursos.readlines()
            cont_cursos = 0
            for cursos in ler_cursos:
                cont_cursos += 1
            numero_de_cursos = cont_cursos
        else:
            numero_de_cursos = 0

        # Número de Estudantes Cadastrados
        alunos_cadastrados = 'arquivostxt\\Alunos Cadastrados.txt'
        if arquivo.arquivoExiste(alunos_cadastrados):
            arquivo_alunos = open(alunos_cadastrados, 'rt', encoding='utf-8')
            ler_alunos = arquivo_alunos.readlines()
            cont_alunos = 0
            for alunos in ler_alunos:
                cont_alunos += 1
            numero_de_alunos = cont_alunos
        else:
            numero_de_alunos = 0

        # Número de Docentes Cadastrados
        docentes_cadastrados = 'arquivostxt\\Docentes Cadastrados.txt'
        if arquivo.arquivoExiste(docentes_cadastrados):
            arquivo_docentes = open(docentes_cadastrados, 'rt', encoding='utf-8')
            ler_docentes = arquivo_docentes.readlines()
            cont_docentes = 0
            for docentes in ler_docentes:
                cont_docentes += 1
            numero_de_docentes = cont_docentes
        else:
            numero_de_docentes = 0


        arquivo_escola = open('arquivostxt\\Nome da Escola.txt', 'rt', encoding='utf-8')
        nome_da_escola = arquivo_escola.read()
        coluna_menu = [
            [sg.Button('', image_data=icones.menu_casa,
                       button_color=(sg.theme_background_color(), sg.theme_background_color()), key='-ICONE_CASA-',
                       border_width=0, enable_events=True)],
            [sg.Button('', image_data=icones.menu_sala,
                       button_color=(sg.theme_background_color(), sg.theme_background_color()), key='-ICONE_SALA-',
                       border_width=2, enable_events=True)],
            [sg.Button('', image_data=icones.menu_professores,
                       button_color=(sg.theme_background_color(), sg.theme_background_color()),
                       key='-ICONE_PROFESSORES-', border_width=2, enable_events=True)],
            [sg.Button('', image_data=icones.menu_alunos,
                       button_color=(sg.theme_background_color(), sg.theme_background_color()), key='-ICONE_ALUNOS-',
                       border_width=2, enable_events=True)],
            [sg.Button('', image_data=icones.menu_cursos,
                       button_color=(sg.theme_background_color(), sg.theme_background_color()), key='-ICONE_CURSOS-',
                       border_width=2, enable_events=True)],
            [sg.Button('', image_data=icones.menu_mensagem,
                       button_color=(sg.theme_background_color(), sg.theme_background_color()), key='-ICONE_MENSAGEM-',
                       border_width=2, enable_events=True)],
            [sg.Button('', image_data=icones.menu_financiamento,
                       button_color=(sg.theme_background_color(), sg.theme_background_color()),
                       key='-ICONE_FINANCIAMENTO-', border_width=2, enable_events=True)],
            [sg.Button('', image_data=icones.menu_ferramentas,
                       button_color=(sg.theme_background_color(), sg.theme_background_color()),
                       key='-ICONE_FERRAMENTAS-', border_width=2, enable_events=True)]
        ]
        coluna_tabelas_cursos = [
            [sg.Text('Cursos Disponíveis:', font=('Aria', 12))],
            [sg.Multiline(ler_cursos, text_color='white', size=(78, 20), background_color='#44475a',
                          key='-MOSTRAR_CURSOS-')]
        ]
        coluna_tabelas_alunos = [
            [sg.Text('Alunos Cadastrados:', font=('Aria', 12))],
            [sg.Multiline(ler_alunos, text_color='white', size=(75, 20), background_color='#44475a',
                          key='-MOSTRAR ALUNOS-')]
        ]
        coluna_numeros = [
            [sg.Frame('Salas:', [[sg.Image('img\\sala.png'), sg.Text(f'{numero_de_salas} Salas Cadastradas')]]),
             sg.Text(f'{"":>38}'),
             sg.Frame('Cursos:', [[sg.Image('img\\cursos.png'), sg.Text(f'{numero_de_cursos} Cursos Cadastrados')]])],
            [sg.HorizontalSeparator()],
            [sg.Frame('Estudantes:', [[sg.Image('img\\alunos.png'), sg.Text(f'{numero_de_alunos} Estudantes Cadastrados')]]),
             sg.Text(f'{"":>30}'),
             sg.Frame('Comentários:', [[sg.Image('img\\msg.png'), sg.Text(f' Comentários Cadastrados')]])],
            [sg.HorizontalSeparator()],
            [sg.Frame('Docentes', [[sg.Image('img\\docentes.png'), sg.Text(f'{numero_de_docentes} Docentes Cadastrados')]])]
        ]
        coluna_conteudo = [
            [sg.Text(f'Escola:  {nome_da_escola}', font='Arial')],
            [sg.HorizontalSeparator()],
            [sg.Frame('', [[sg.Image('img\\principal.png')]]), sg.VSep(), sg.Column(coluna_tabelas_cursos)],
            [sg.Column(coluna_numeros), sg.Column(coluna_tabelas_alunos)]
        ]
        layout = [
            [sg.Image('img\\logo_canto.png'), sg.VerticalSeparator(), sg.Text(data_completa_atual(), font='Arial')],
            [sg.HorizontalSeparator()],
            [sg.Column(coluna_menu), sg.VerticalSeparator(), sg.Column(coluna_conteudo, scrollable=True, size=(2000, 1000))]
        ]
        return sg.Window('SMS - School Management System - Janela Principal', layout=layout, auto_size_text=True,
                   auto_size_buttons=True, resizable=True, finalize=True)
    else:
        layout = [
            [sg.Text(
                'Bem-vindo ao SMS!\nAntes de entrar no sistema principal pela primeira vez,\nprimeiro é necessário registar o nome da Instituição de ensino (Escola)', font=('', 11))],
            [sg.Text('Registe aqui: '), sg.Input(key='-NOME DA ESCOLA-'), sg.Button('Registar', key='-BOTAO REGISTRAR NOME DA ESCOLA-', button_color=('', 'blue'))]
        ]
        return sg.Window('SMS - Registar Instituição de Ensino', layout=layout, finalize=True)


def janela_menu_salas():
    sg.theme('DefaultNoMoreNagging')
    coluna_menu = [
        [sg.Button('', image_data=icones.menu_casa,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()), key='-ICONE_CASA-',
                   border_width=2, enable_events=True)],
        [sg.Button('', image_data=icones.menu_sala,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()), key='-ICONE_SALA-',
                   border_width=0, enable_events=True)],
        [sg.Button('', image_data=icones.menu_professores,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()),
                   key='-ICONE_PROFESSORES-', border_width=2, enable_events=True)],
        [sg.Button('', image_data=icones.menu_alunos,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()), key='-ICONE_ALUNOS-',
                   border_width=2, enable_events=True)],
        [sg.Button('', image_data=icones.menu_cursos,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()), key='-ICONE_CURSOS-',
                   border_width=2, enable_events=True)],
        [sg.Button('', image_data=icones.menu_mensagem,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()), key='-ICONE_MENSAGEM-',
                   border_width=2, enable_events=True)],
        [sg.Button('', image_data=icones.menu_financiamento,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()),
                   key='-ICONE_FINANCIAMENTO-', border_width=2, enable_events=True)],
        [sg.Button('', image_data=icones.menu_ferramentas,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()),
                   key='-ICONE_FERRAMENTAS-', border_width=2, enable_events=True)]
    ]
    salas_cadastradas = 'arquivostxt\\Salas Cadastradas.txt'
    if arquivo.arquivoExiste(salas_cadastradas):
        arquivo_salas = open(salas_cadastradas, 'rt', encoding='utf-8')
        ler_salas = arquivo_salas.readlines()
        cont_salas = 0
        for salss in ler_salas:
            cont_salas += 1
        numero_de_salas = cont_salas
    else:
        numero_de_salas = 0

    if arquivo.arquivoExiste(salas_cadastradas):
        coluna_conteudo = [
            [sg.Frame('', [[sg.Image('img\\sala.png'), sg.Text(f'{numero_de_salas} Salas Cadastradas', font=('Helvetica', 20), key='-SALAS_NUMERO_SALAS-')]])],
            [sg.Frame('Cadastro de Salas', [[sg.Text('Nome da Sala:'), sg.Input(key='-NOME DA SALA-'), sg.Button('Cadastrar nova sala', key='-BOTAO_CADASTRAR_NOVA_SALA-', button_color=('', 'blue'))]])],
            [sg.Text('Dados cadastrados no Ficheiro:', font=('Helvetica', 15))],
            [sg.Text('Sala:'), sg.Text(f'{"":>110}'), sg.Text('Data de Criação:')],
            [sg.HorizontalSeparator()],
            [sg.Multiline(ler_salas, text_color='white', size=(100, 30), background_color='#44475a', key='-MOSTRAR_SALAS-')]
        ]
    else:
        coluna_conteudo = [
            [
                sg.Frame('', [[sg.Image('img\\sala.png'), sg.Text(f'{numero_de_salas} Salas Cdastradas', font=('Helvetica', 20), key='-SALAS_NUMERO_SALAS-')]]), sg.Text(f'{"":>25}'),
             sg.Frame('Observação:', [[sg.Text('Alguns dados na tela só serão\natualizados após o reinício do programa\n ou aba correspondente.', text_color='red')]])
            ],
            [sg.Frame('Cadastro de Salas', [[sg.Text('Nome da Sala:'), sg.Input(key='-NOME DA SALA-'),
                                             sg.Button('Cadastrar nova sala', key='-BOTAO_CADASTRAR_NOVA_SALA-', button_color=('', 'blue'))]])],
            [sg.Text('Ainda não foi Cadastrado Nenhuma Sala:', font=('Helvetica', 15))],
            [sg.Text('Sala:'), sg.Text(f'{"":>110}'), sg.Text('Data de Criação:')],
            [sg.HorizontalSeparator()],
            [sg.Multiline(size=(100, 30), background_color='#44475a', key='-MOSTRAR_SALAS-', text_color='white')],
        ]
    layout = [
        [sg.Image('img\\logo_canto.png'), sg.VerticalSeparator(), sg.Text(data_completa_atual(), font='Arial')],
        [sg.HorizontalSeparator()],
        [sg.Column(coluna_menu), sg.VerticalSeparator(), sg.Column(coluna_conteudo, scrollable=True, size=(2000, 1000))]
    ]
    return sg.Window('SMS - School Management System - Salas', layout=layout, auto_size_text=True,
                     auto_size_buttons=True, resizable=True, finalize=True)


def janela_menu_docentes():
    sg.theme('DefaultNoMoreNagging')
    coluna_menu = [
        [sg.Button('', image_data=icones.menu_casa,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()), key='-ICONE_CASA-',
                   border_width=2, enable_events=True)],
        [sg.Button('', image_data=icones.menu_sala,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()), key='-ICONE_SALA-',
                   border_width=2, enable_events=True)],
        [sg.Button('', image_data=icones.menu_professores,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()),
                   key='-ICONE_PROFESSORES-', border_width=0, enable_events=True)],
        [sg.Button('', image_data=icones.menu_alunos,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()), key='-ICONE_ALUNOS-',
                   border_width=2, enable_events=True)],
        [sg.Button('', image_data=icones.menu_cursos,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()), key='-ICONE_CURSOS-',
                   border_width=2, enable_events=True)],
        [sg.Button('', image_data=icones.menu_mensagem,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()), key='-ICONE_MENSAGEM-',
                   border_width=2, enable_events=True)],
        [sg.Button('', image_data=icones.menu_financiamento,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()),
                   key='-ICONE_FINANCIAMENTO-', border_width=2, enable_events=True)],
        [sg.Button('', image_data=icones.menu_ferramentas,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()),
                   key='-ICONE_FERRAMENTAS-', border_width=2, enable_events=True)]
    ]
    coluna_form_docente = [
        [sg.Text('Nome do Docente:'), sg.Input(key='-NOME DO DOCENTE-')],
        [sg.Text(f'{"":>10}'), sg.Text('Salário Base:'), sg.Input(key='-SALÁRIO_BASE_DOCENTE-', size=(11, 10)), sg.Text('Turmas Atribuidas:'), sg.Input(key='-TURMAS_DOCENTE-', size=(11, 10))],
        [sg.Text('Disciplina a Lecionar:'), sg.Input(key='-DOCENTE_DISCIPLINAS-', size=(43, 10))],
        [sg.Text('')],
        [sg.Button('Gerar pdf', key='-BOTAO_GERAR_PDF_DOCENTE-', button_color=('', 'red')), sg.Button('update', key='-atualizar_docentes-'), sg.Text(f'{"":>37}'), sg.Button('Cadastrar novo Docente', key='-BOTAO_CADASTRAR_NOVO_DOCENTE-', button_color=('', 'blue'))]
    ]
    docentes_cadastrados = 'arquivostxt\\Docentes Cadastrados.txt'
    if arquivo.arquivoExiste(docentes_cadastrados):
        arquivo_docentes = open(docentes_cadastrados, 'rt', encoding='utf-8')
        ler_docentes = arquivo_docentes.readlines()
        cont_docentes = 0
        for docentes in ler_docentes:
            cont_docentes += 1
        numero_de_docentes = cont_docentes
    else:
        numero_de_docentes = 0

    if arquivo.arquivoExiste(docentes_cadastrados):
        coluna_conteudo = [
            [sg.Frame('', [
                [sg.Image('img\\docentes.png'), sg.Text(f'{numero_de_docentes} Docentes Cadastrados', font=('Helvetica', 20), key='-DOCENTES_NUMERO_DOCENTES-')]])],
            [sg.Frame('Cadastro de Docentes', coluna_form_docente)],
            [sg.Text('Dados cadastrados no Ficheiro:', font=('Helvetica', 15))],
            [sg.Text('Docentes:'), sg.Text(f'{"":>110}'), sg.Text('Disciplina a Lecionar:')],
            [sg.HorizontalSeparator()],
            [sg.Multiline(ler_docentes, text_color='white', size=(100, 30), background_color='#44475a', key='-MOSTRAR DOCENTES-')]
        ]
    else:
        coluna_conteudo = [
            [
                sg.Frame('', [[sg.Image('img\\docentes.png'), sg.Text(f'{numero_de_docentes} Docentes Cadastrados', font=('Helvetica', 20), key='-DOCENTES_NUMERO_DOCENTES-')]]), sg.Text(f'{"":>25}'),
             sg.Frame('Observação:', [[sg.Text('Alguns dados na tela só serão\natualizados após o reinício do programa\n ou aba correspondente.', text_color='red')]])
            ],
            [sg.Frame('Cadastro de Docentes', coluna_form_docente)],
            [sg.Text('Ainda não foi Cadastrado Nenhum Docente:', font=('Helvetica', 15))],
            [sg.Text('Docentes:'), sg.Text(f'{"":>110}'), sg.Text('Disciplina a Lecionar:')],
            [sg.HorizontalSeparator()],
            [sg.Multiline(size=(100, 30), background_color='#44475a', key='-MOSTRAR DOCENTES-', text_color='white')]
        ]
    layout = [
        [sg.Image('img\\logo_canto.png'), sg.VerticalSeparator(), sg.Text(data_completa_atual(), font='Arial')],
        [sg.HorizontalSeparator()],
        [sg.Column(coluna_menu), sg.VerticalSeparator(), sg.Column(coluna_conteudo, scrollable=True, size=(2000, 1000))]
    ]
    return sg.Window('SMS - School Management System - Docentes', layout=layout, auto_size_text=True,
                     auto_size_buttons=True, resizable=True, finalize=True)


def janela_menu_aluno():
    sg.theme('DefaultNoMoreNagging')
    coluna_menu = [
        [sg.Button('', image_data=icones.menu_casa,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()), key='-ICONE_CASA-',
                   border_width=2, enable_events=True)],
        [sg.Button('', image_data=icones.menu_sala,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()), key='-ICONE_SALA-',
                   border_width=2, enable_events=True)],
        [sg.Button('', image_data=icones.menu_professores,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()),
                   key='-ICONE_PROFESSORES-', border_width=2, enable_events=True)],
        [sg.Button('', image_data=icones.menu_alunos,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()), key='-ICONE_ALUNOS-',
                   border_width=0, enable_events=True)],
        [sg.Button('', image_data=icones.menu_cursos,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()), key='-ICONE_CURSOS-',
                   border_width=2, enable_events=True)],
        [sg.Button('', image_data=icones.menu_mensagem,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()), key='-ICONE_MENSAGEM-',
                   border_width=2, enable_events=True)],
        [sg.Button('', image_data=icones.menu_financiamento,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()),
                   key='-ICONE_FINANCIAMENTO-', border_width=2, enable_events=True)],
        [sg.Button('', image_data=icones.menu_ferramentas,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()),
                   key='-ICONE_FERRAMENTAS-', border_width=2, enable_events=True)]
    ]
    coluna_form_aluno = [
        [sg.Text('Nome do Aluno:'), sg.Input(key='-NOME DO ALUNO-', size=(43, 10))],
        [sg.Text(f'{"":>10}'), sg.Text('Data de Nascimento:'), sg.Input('da-mm-aaaa', key='-DATA_NASCIMENTO_ALUNO-', size=(11, 10)), sg.Text('Idade:'), sg.Input(key='-IDADE_ALUNO-', size=(11, 10))],
        [sg.Text('Nº Documento de identificação:'), sg.Input(key='-DOCUMENTO_IDENTIFICAÇÃO_ALUNO-', size=(30, 10))],
        [sg.Text('Morada:'), sg.Input(key='-MORADA_ALUNO-',  size=(49, 10))],
        [sg.Text('Código Postal:'), sg.Input(key='-POSTAL1-', size=(11, 10)), sg.Input(key='-POSTAL2-', size=(10, 10))],
        [sg.Text('Distrito:'), sg.Input(key='DISTRITO_ALUNO', size=(30, 10))],
        [sg.Text('Telefone:'), sg.Input(key='-TELEFONE_ALUNO-', size=(29, 10))],
        [sg.Text('')],
        [sg.Button('Gerar pdf', key='-BOTAO_GERAR_PDF_ALUNOS-', button_color=('', 'red')), sg.Button('update', key='-atualizar_alunos-'), sg.Text(f'{"":>33}'), sg.Button('Cadastrar novo Aluno', key='-BOTAO_CADASTRAR_NOVO_ALUNO-', button_color=('', 'blue'))]
    ]
    alunos_cadastrados = 'arquivostxt\\Alunos Cadastrados.txt'
    if arquivo.arquivoExiste(alunos_cadastrados):
        arquivo_alunos = open(alunos_cadastrados, 'rt', encoding='utf-8')
        ler_alunos = arquivo_alunos.readlines()
        cont_alunos = 0
        for alunos in ler_alunos:
            cont_alunos += 1
        numero_de_alunos = cont_alunos
    else:
        numero_de_alunos = 0

    if arquivo.arquivoExiste(alunos_cadastrados):
        coluna_conteudo = [
            [sg.Frame('', [
                [sg.Image('img\\alunos.png'), sg.Text(f'{numero_de_alunos} Alunos Cadastrados', font=('Helvetica', 20), key='-ALUNOS_NUMERO_ALUNOS-')]])],
            [sg.Frame('Cadastro de Aluno', coluna_form_aluno)],
            [sg.Text('Dados cadastrados no Ficheiro:', font=('Helvetica', 15))],
            [sg.Text('Alunos:'), sg.Text(f'{"":>130}'), sg.Text('Idade:')],
            [sg.HorizontalSeparator()],
            [sg.Multiline(ler_alunos, text_color='white', size=(100, 30), background_color='#44475a', key='-MOSTRAR ALUNOS-')]
        ]
    else:
        coluna_conteudo = [
            [
                sg.Frame('', [[sg.Image('img\\alunos.png'), sg.Text(f'{numero_de_alunos} Alunos Cadastrados', font=('Helvetica', 20), key='-ALUNOS_NUMERO_ALUNOS-')]]), sg.Text(f'{"":>25}'),
             sg.Frame('Observação:', [[sg.Text('Alguns dados na tela só serão\natualizados após o reinício do programa\n ou aba correspondente.', text_color='red')]])
             ],
            [sg.Frame('Cadastro de Alunos', coluna_form_aluno)],
            [sg.Text('Ainda não foi Cadastrado Nenhum Aluno:', font=('Helvetica', 15))],
            [sg.Text('Alunos:'), sg.Text(f'{"":>130}'), sg.Text('Idade:')],
            [sg.HorizontalSeparator()],
            [sg.Multiline(size=(100, 30), background_color='#44475a', key='-MOSTRAR ALUNOS-', text_color='white')]
        ]
    layout = [
        [sg.Image('img\\logo_canto.png'), sg.VerticalSeparator(), sg.Text(data_completa_atual(), font='Arial')],
        [sg.HorizontalSeparator()],
        [sg.Column(coluna_menu), sg.VerticalSeparator(), sg.Column(coluna_conteudo, scrollable=True, size=(2000, 1000))]
    ]
    return sg.Window('SMS - School Management System - Alunos', layout=layout, auto_size_text=True,
                     auto_size_buttons=True, resizable=True, finalize=True)


def janela_menu_cursos():
    sg.theme('DefaultNoMoreNagging')
    coluna_menu = [
        [sg.Button('', image_data=icones.menu_casa,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()), key='-ICONE_CASA-',
                   border_width=2, enable_events=True)],
        [sg.Button('', image_data=icones.menu_sala,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()), key='-ICONE_SALA-',
                   border_width=2, enable_events=True)],
        [sg.Button('', image_data=icones.menu_professores,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()),
                   key='-ICONE_PROFESSORES-', border_width=2, enable_events=True)],
        [sg.Button('', image_data=icones.menu_alunos,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()), key='-ICONE_ALUNOS-',
                   border_width=2, enable_events=True)],
        [sg.Button('', image_data=icones.menu_cursos,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()), key='-ICONE_CURSOS-',
                   border_width=0, enable_events=True)],
        [sg.Button('', image_data=icones.menu_mensagem,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()), key='-ICONE_MENSAGEM-',
                   border_width=2, enable_events=True)],
        [sg.Button('', image_data=icones.menu_financiamento,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()),
                   key='-ICONE_FINANCIAMENTO-', border_width=2, enable_events=True)],
        [sg.Button('', image_data=icones.menu_ferramentas,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()),
                   key='-ICONE_FERRAMENTAS-', border_width=2, enable_events=True)]
    ]
    coluna_form_cursos = [
        [sg.Text('Curos:'), sg.Input(key='-NOME_DO_CURSO-')],
        [sg.Text('Turno:'), sg.Input(key='-TURNO_DO_CURSO-', size=(20, 10))],
        [sg.Text('')],
        [sg.Text(f'{"":>70}'), sg.Button('Cadastrar novo Curso', key='-BOTAO_CADASTRAR_NOVO_CURSO-', button_color=('', 'blue'))]
    ]
    cursos_cadastrados = 'arquivostxt\\Cursos Cadastrados.txt'
    if arquivo.arquivoExiste(cursos_cadastrados):
        arquivo_cursos = open(cursos_cadastrados, 'rt', encoding='utf-8')
        ler_cursos = arquivo_cursos.readlines()
        cont_cursos = 0
        for cursos in ler_cursos:
            cont_cursos += 1
        numero_de_cursos = cont_cursos
    else:
        numero_de_cursos = 0

    if arquivo.arquivoExiste(cursos_cadastrados):
        coluna_conteudo = [
            [sg.Frame('', [
                [sg.Image('img\\cursos.png'), sg.Text(f'{numero_de_cursos} Cursos Cadastrados', font=('Helvetica', 20), key='-CURSOS_NUMERO_CURSOS-')]])],
            [sg.Frame('Cadastro de Cursos', coluna_form_cursos)],
            [sg.Text('Dados cadastrados no Ficheiro:', font=('Helvetica', 15))],
            [sg.Text('Cursos:'), sg.Text(f'{"":>130}'), sg.Text('Turnos:')],
            [sg.HorizontalSeparator()],
            [sg.Multiline(ler_cursos, text_color='white', size=(100, 30), background_color='#44475a', key='-MOSTRAR_CURSOS-')]
        ]
    else:
        coluna_conteudo = [
            [sg.Frame('', [[sg.Image('img\\cursos.png'), sg.Text(f'{numero_de_cursos} Cursos Cadastrados', font=('Helvetica', 20), key='-CURSOS_NUMERO_CURSOS-')]]), sg.Text(f'{"":>25}'),
             sg.Frame('Observação:', [[sg.Text('Alguns dados na tela só serão\natualizados após o reinício do programa\n ou aba correspondente.', text_color='red')]])],
            [sg.Frame('Cadastro de Cursos', coluna_form_cursos)],
            [sg.Text('Ainda não foi Cadastrado Nenhum Curso', font=('Helvetica', 15))],
            [sg.Text('Cursos:'), sg.Text(f'{"":>130}'), sg.Text('Turnos:')],
            [sg.HorizontalSeparator()],
            [sg.Multiline(size=(100, 30), background_color='#44475a', key='-MOSTRAR_CURSOS-', text_color='white')]
        ]
    layout = [
        [sg.Image('img\\logo_canto.png'), sg.VerticalSeparator(), sg.Text(data_completa_atual(), font='Arial')],
        [sg.HorizontalSeparator()],
        [sg.Column(coluna_menu), sg.VerticalSeparator(), sg.Column(coluna_conteudo, scrollable=True, size=(2000, 1000))]
    ]
    return sg.Window('SMS - School Management System - Cursos', layout=layout, auto_size_text=True,
                     auto_size_buttons=True, resizable=True, finalize=True)


def janela_menu_mensagem():
    sg.theme('DefaultNoMoreNagging')
    coluna_menu = [
        [sg.Button('', image_data=icones.menu_casa,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()), key='-ICONE_CASA-',
                   border_width=2, enable_events=True)],
        [sg.Button('', image_data=icones.menu_sala,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()), key='-ICONE_SALA-',
                   border_width=2, enable_events=True)],
        [sg.Button('', image_data=icones.menu_professores,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()),
                   key='-ICONE_PROFESSORES-', border_width=2, enable_events=True)],
        [sg.Button('', image_data=icones.menu_alunos,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()), key='-ICONE_ALUNOS-',
                   border_width=2, enable_events=True)],
        [sg.Button('', image_data=icones.menu_cursos,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()), key='-ICONE_CURSOS-',
                   border_width=2, enable_events=True)],
        [sg.Button('', image_data=icones.menu_mensagem,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()), key='-ICONE_MENSAGEM-',
                   border_width=0, enable_events=True)],
        [sg.Button('', image_data=icones.menu_financiamento,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()),
                   key='-ICONE_FINANCIAMENTO-', border_width=2, enable_events=True)],
        [sg.Button('', image_data=icones.menu_ferramentas,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()),
                   key='-ICONE_FERRAMENTAS-', border_width=2, enable_events=True)]
    ]
    coluna_form_mensagens = [
        [sg.Text('Nome:'), sg.Text(f'{"":>3}'), sg.Input(key='-NOME_DA_PESSOA-')],
        [sg.Text('E-mail:'), sg.Text(f'{"":>2}'), sg.Input(key='-CAMPO_EMAIL-')],
        [sg.Text('Assunto:'), sg.Text(''), sg.Input(key='-CAMPO_AASUNTO-')],
        [sg.Text('Mensagem:'), sg.Multiline(size=(45, 10), key='-CAMPO_MENSAGEM-')],
        [sg.Text('')],
        [sg.Text(f'{"":>35}'), sg.Button('Enviar Mensagem', key='-BOTAO_ENVIAR_MENSAGEM-', button_color=('', 'blue'))]
    ]
    coluna_conteudo = [
            [sg.Frame('', [
                [sg.Image('img\\msg.png'), sg.Text(f'Mensagens', font=('Helvetica', 20))]])],
            [sg.Frame('Cadastro de mensagens', coluna_form_mensagens)],
        ]
    layout = [
        [sg.Image('img\\logo_canto.png'), sg.VerticalSeparator(), sg.Text(data_completa_atual(), font='Arial')],
        [sg.HorizontalSeparator()],
        [sg.Column(coluna_menu), sg.VerticalSeparator(), sg.Column(coluna_conteudo, scrollable=True, size=(2000, 1000))]
    ]
    return sg.Window('SMS - School Management System - Mensagens', layout=layout, auto_size_text=True,
                     auto_size_buttons=True, resizable=True, finalize=True)
