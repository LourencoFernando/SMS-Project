import PySimpleGUI as sg
import interface, arquivo
import webbrowser
from fpdf import FPDF

janela_boas_vindas, janela_principal, janela_salas, janela_professores, janela_alunos, janela_cursos, janela_mensagem = interface.janela_de_boas_vinda(), None, None, None, None, None, None
while True:
    window, event, values = sg.read_all_windows()

    # Lógica da janela de boas vindas
    if window == janela_boas_vindas:
        if event == '-ICONE_FACEBOOK-':
            webbrowser.open('https://www.facebook.com/profile.php?id=100006375421653')
        elif event == '-ICONE_INSTAGRAM-':
            webbrowser.open('https://www.instagram.com/lourencofernando1/')
        elif event == '-ICONE_YOUTUBE-':
            webbrowser.open('https://www.youtube.com/channel/UCDshuKtYFwsgnUwQI647S1g')
        elif event == '-BOTAO_ENTRAR_SISTEMA-':
            # sg.popup_timed('Janela de Sistema ainda em Desenvolvimeno')
            janela_boas_vindas.hide()
            janela_principal = interface.janela_menu_casa()
        elif event == '-BOTAO_FECHAR-' or event == sg.WIN_CLOSED:
            break

    # Lógica da jannela Principal
    if window == janela_principal:
        if event == '-BOTAO REGISTRAR NOME DA ESCOLA-':
            try:
                if values['-NOME DA ESCOLA-'] == '':
                    sg.theme('DarkRed1')
                    sg.Popup('Não deve deixar o campo em Branco', title='SMS - ERRO')
                else:
                    try:
                        nome = 'arquivostxt\\Nome da Escola.txt'
                        arquivo.criarArquivo(nome, values['-NOME DA ESCOLA-'])
                        janela_principal.close()
                        janela_principal = interface.janela_menu_casa()
                    except:
                        sg.theme('DarkRed1')
                        sg.Popup('ERRO ao Registar', title='SMS - ERRO')
            except:
                sg.theme('DarkRed1')
                sg.Popup('Impossíveç proseguir', title='SMS - ERRO')
        if event == '-ICONE_SALA-':
            janela_principal.hide()
            janela_salas = interface.janela_menu_salas()
        elif event == '-ICONE_PROFESSORES-':
            janela_principal.hide()
            janela_professores = interface.janela_menu_docentes()
        elif event == '-ICONE_ALUNOS-':
            janela_principal.hide()
            janela_alunos = interface.janela_menu_aluno()
        elif event == '-ICONE_CURSOS-':
            janela_principal.hide()
            janela_cursos = interface.janela_menu_cursos()
        elif event == '-ICONE_MENSAGEM-':
            janela_principal.hide()
            janela_mensagem = interface.janela_menu_mensagem()
        elif event == sg.WIN_CLOSED:
            break

    # Lógica da jannela das Salas
    if window == janela_salas:
        if event == '-BOTAO_CADASTRAR_NOVA_SALA-':
            if values['-NOME DA SALA-'] == '':
                sg.theme('DarkRed1')
                sg.Popup('Não deve deixar o campo em Branco', title='SMS - ERRO')
            else:
                try:
                    salas_cadastradas = 'arquivostxt\\Salas Cadastradas.txt'
                    arquivo.criarArquivoSala(salas_cadastradas, values['-NOME DA SALA-'])
                    arquivo_salas = open(salas_cadastradas, 'rt', encoding='utf-8')
                    ler_salas = arquivo_salas.read()
                    window['-MOSTRAR_SALAS-'].update(ler_salas)
                    arquivo_salas.close()
                    arquivo_salas = open(salas_cadastradas, 'rt', encoding='utf-8')
                    ler_salas = arquivo_salas.readlines()
                    cont_salas = 0
                    for salss in ler_salas:
                        cont_salas += 1
                    numero_de_salas = cont_salas
                    window['-SALAS_NUMERO_SALAS-'].update(f'{numero_de_salas} Salas Cdastradas')
                    window['-NOME DA SALA-'].update('')
                except:
                    sg.theme('DarkRed1')
                    sg.Popup('ERRO ao Cadastrar', title='SMS - ERRO')
                else:
                    sg.theme('DefaultNoMoreNagging')
                    sg.popup_timed('Cadastro efetuado com SUCESSO!')

        elif event == '-ICONE_CASA-':
            janela_salas.hide()
            janela_principal = interface.janela_menu_casa()
        elif event == '-ICONE_SALA-':
            janela_salas.hide()
            janela_salas = interface.janela_menu_salas()
        elif event == '-ICONE_PROFESSORES-':
            janela_salas.hide()
            janela_professores = interface.janela_menu_docentes()
        elif event == '-ICONE_ALUNOS-':
            janela_salas.hide()
            janela_alunos = interface.janela_menu_aluno()
        elif event == '-ICONE_CURSOS-':
            janela_salas.hide()
            janela_cursos = interface.janela_menu_cursos()
        elif event == '-ICONE_MENSAGEM-':
            janela_salas.hide()
            janela_mensagem = interface.janela_menu_mensagem()
        elif event == sg.WIN_CLOSED:
            break

    # Lógica da jannela Professores
    if window == janela_professores:
        if event == '-BOTAO_CADASTRAR_NOVO_DOCENTE-':
            if  values['-NOME DO DOCENTE-'] == '':
                sg.theme('DarkRed1')
                sg.Popup('Não deve deixar o campo \"Nome Docente\" em Branco', title='SMS - ERRO')
            elif values['-DOCENTE_DISCIPLINAS-'] == '':
                sg.theme('DarkRed1')
                sg.Popup('Não deve deixar o campo \"Disciplina a lecionar\" em Branco', title='SMS - ERRO')
            else:
                try:
                    docentes_cadastrados = 'arquivostxt\\Docentes Cadastrados.txt'
                    arquivo.criarArquivoDocente(docentes_cadastrados, values['-NOME DO DOCENTE-'], values['-DOCENTE_DISCIPLINAS-'])
                    arquivo_docentes = open(docentes_cadastrados, 'rt', encoding='utf-8')
                    ler_docentes = arquivo_docentes.read()
                    window['-MOSTRAR DOCENTES-'].update(ler_docentes)
                    arquivo_docentes.close()
                    arquivo_docentes = open(docentes_cadastrados, 'rt', encoding='utf-8')
                    ler_docentes = arquivo_docentes.readlines()
                    cont_docentes = 0
                    for salss in ler_docentes:
                        cont_docentes += 1
                    numero_de_docentes = cont_docentes
                    window['-DOCENTES_NUMERO_DOCENTES-'].update(f'{numero_de_docentes} Docentes Cadastrados')
                except:
                    sg.theme('DarkRed1')
                    sg.Popup(f'Ocorreu um erro ao Cadastrar o Docentes \"{values["-NOME DO DOCENTE-"]}\" :(',
                             title='SMS - ERRO')
                else:
                    sg.theme('DefaultNoMoreNagging')
                    sg.popup_timed(f'Cadastro de \"{values["-NOME DO DOCENTE-"]}\" efetuado com SUCESSO!')

        if event == '-BOTAO_GERAR_PDF_DOCENTE-':
            if values['-NOME DO DOCENTE-'] == '':
                sg.theme('DarkRed1')
                sg.Popup('Deve preencher corretamente TODOS os Campos!!', title='SMS - ERRO')
            elif values['-DOCENTE_DISCIPLINAS-'] == '':
                sg.theme('DarkRed1')
                sg.Popup('Deve preencher corretamente TODOS os Campos!!', title='SMS - ERRO')
            elif values['-SALÁRIO_BASE_DOCENTE-'] == '':
                sg.theme('DarkRed1')
                sg.Popup('Deve preencher corretamente TODOS os Campos!!', title='SMS - ERRO')
            elif values['-TURMAS_DOCENTE-'] == '':
                sg.theme('DarkRed1')
                sg.Popup('Deve preencher corretamente TODOS os Campos!!', title='SMS - ERRO')
            else:
                try:
                    arquivo.GerarPDF(values['-NOME DO DOCENTE-'], values['-SALÁRIO_BASE_DOCENTE-'], values['-TURMAS_DOCENTE-'], values['-DOCENTE_DISCIPLINAS-'])
                except UnicodeEncodeError:
                    sg.theme('DarkRed1')
                    sg.popup('ERRO ao gerar pdf!! :(\nCausa: UnicodeEncodeError\nPossível solução:\nPor favor não introduza o simbolo monetário no campo \"Salário Base\"', title='SMS - ERRO')
                except:
                    sg.theme('DarkRed1')
                    sg.popup('ERRO ao gerar pdf!! :(\nCausa: fpdf.errors.FPDFException\nPossível Solução\nTroque o conteúdo do Campo \"Nome do Docente\", clique no botão \"update\"(para que a tela seja atualizada) ou REINICIE o programa\nMotivo: Já existe um pdf com esse mesmo nome\nContent cannot be added on a closed document :(', title='SMS - ERRO')
                else:
                    sg.theme('DefaultNoMoreNagging')
                    sg.popup(f'PDF gerado com SUCESSO!\n O ficheiro encontra-se arquivado na pasta\"arquivospdf\Docente\" do SMS. :)')
        elif event == '-atualizar_docentes-':
            janela_professores.hide()
            janela_professores = interface.janela_menu_docentes()
        elif event == '-ICONE_CASA-':
            janela_professores.hide()
            janela_principal = interface.janela_menu_casa()
        elif event == '-ICONE_SALA-':
            janela_professores.hide()
            janela_salas = interface.janela_menu_salas()
        elif event == '-ICONE_PROFESSORES-':
            janela_professores.hide()
            janela_professores = interface.janela_menu_docentes()
        elif event == '-ICONE_ALUNOS-':
            janela_professores.hide()
            janela_alunos = interface.janela_menu_aluno()
        elif event == '-ICONE_CURSOS-':
            janela_professores.hide()
            janela_cursos = interface.janela_menu_cursos()
        elif event == '-ICONE_MENSAGEM-':
            janela_professores.hide()
            janela_mensagem = interface.janela_menu_mensagem()
        elif event == sg.WIN_CLOSED:
            break

    # Lógica da jannela Alunos
    if window == janela_alunos:
        if event == '-BOTAO_CADASTRAR_NOVO_ALUNO-':
            if values['-NOME DO ALUNO-'] == '':
                sg.theme('DarkRed1')
                sg.Popup('Não deve deixar o campo \"Nome do Aluno\" em Branco', title='SMS - ERRO')
            elif values['-IDADE_ALUNO-'] == '':
                sg.theme('DarkRed1')
                sg.Popup('Não deve deixar o campo \"Idade\" em Branco', title='SMS - ERRO')
            elif arquivo.leiaint(values['-IDADE_ALUNO-']) is False:
                sg.theme('DarkRed1')
                sg.popup('ERRO: Por favor digite um número inteiro válido')
            else:
                try:
                    alunos_cadastrados = 'arquivostxt\\Alunos Cadastrados.txt'
                    arquivo.criarArquivoAlunos(alunos_cadastrados, values['-NOME DO ALUNO-'], values['-IDADE_ALUNO-'])
                    arquivo_alunos = open(alunos_cadastrados, 'rt', encoding='utf-8')
                    ler_alunos = arquivo_alunos.read()
                    window['-MOSTRAR ALUNOS-'].update(ler_alunos)
                    arquivo_alunos.close()
                    arquivo_alunos = open(alunos_cadastrados, 'rt', encoding='utf-8')
                    ler_alunos = arquivo_alunos.readlines()
                    cont_alunos = 0
                    for alunos in ler_alunos:
                        cont_alunos += 1
                    numero_de_alunos = cont_alunos
                    window['-ALUNOS_NUMERO_ALUNOS-'].update(f'{numero_de_alunos} Alunos Cadastrados')
                except:
                    sg.theme('DarkRed1')
                    sg.Popup(f'Ocorreu um erro ao Cadastrar o aluno \"{values["-NOME DO ALUNO-"]}\" :(', title='SMS - ERRO')
                else:
                    sg.theme('DefaultNoMoreNagging')
                    sg.popup_timed(f'Cadastro de \"{values["-NOME DO ALUNO-"]}\" efetuado com SUCESSO!')

        if event == '-BOTAO_GERAR_PDF_ALUNOS-':
            if values['-NOME DO ALUNO-'] == '':
                sg.theme('DarkRed1')
                sg.Popup('Deve preencher corretamente TODOS os Campos!!\n Campo\"Nome do Aluno\"', title='SMS - ERRO')
            elif values['-DATA_NASCIMENTO_ALUNO-'] == '':
                sg.theme('DarkRed1')
                sg.Popup('Deve preencher corretamente TODOS os Campos!! \n Campo\"Data de Nascimento\"', title='SMS - ERRO')
            elif values['-DATA_NASCIMENTO_ALUNO-'] =='d-m-a':
                sg.theme('DarkRed1')
                sg.Popup('Deve preencher corretamente TODOS os Campos!! \n Campo\"Data de Nascimento\"',
                         title='SMS - ERRO')
            elif arquivo.leiaint(values['-IDADE_ALUNO-']) is False:
                sg.theme('DarkRed1')
                sg.popup('ERRO: Por favor digite um número inteiro válido.\n Campo\"Idade\"')
            elif values['-IDADE_ALUNO-'] == '':
                sg.theme('DarkRed1')
                sg.Popup('Deve preencher corretamente TODOS os Campos!!\n Campo\"Idade\"', title='SMS - ERRO')
            elif values['-DOCUMENTO_IDENTIFICAÇÃO_ALUNO-'] == '':
                sg.theme('DarkRed1')
                sg.Popup('Deve preencher corretamente TODOS os Campos!!\n Campo\"Nº Documento de Identificação\"', title='SMS - ERRO')
            elif values['-MORADA_ALUNO-'] == '':
                sg.theme('DarkRed1')
                sg.Popup('Deve preencher corretamente TODOS os Campos!!\n Campo\"Morada\"', title='SMS - ERRO')
            elif values['-POSTAL1-'] == '':
                sg.theme('DarkRed1')
                sg.Popup('Deve preencher corretamente TODOS os Campos!!\n Campo\"Código postal\"', title='SMS - ERRO')
            elif values['-POSTAL2-'] == '':
                sg.theme('DarkRed1')
                sg.Popup('Deve preencher corretamente TODOS os Campos!!\n Campo\"Código postal\"', title='SMS - ERRO')
            elif values['-TELEFONE_ALUNO-'] == '':
                sg.theme('DarkRed1')
                sg.Popup('Deve preencher corretamente TODOS os Campos!!\n Campo\"Telefone\"', title='SMS - ERRO')
            else:
                try:
                    arquivo.GerarPdfAlunos(values['-NOME DO ALUNO-'], values['-DATA_NASCIMENTO_ALUNO-'], values['-IDADE_ALUNO-'], values['-DOCUMENTO_IDENTIFICAÇÃO_ALUNO-'], values['-TELEFONE_ALUNO-'], values['-MORADA_ALUNO-'], values['-POSTAL1-'], values['-POSTAL2-'])
                except:
                    sg.theme('DarkRed1')
                    sg.popup('ERRO ao gerar pdf!! :(\nCausa: fpdf.errors.FPDFException\nPossível Solução\nTroque o conteúdo do Campo \"Nome do Docente\", clique no botão \"update\"(para que a tela seja atualizada) ou REINICIE o programa\nMotivo: Já existe um pdf com esse mesmo nome\nContent cannot be added on a closed document :(', title='SMS - ERRO')
                else:
                    sg.theme('DefaultNoMoreNagging')
                    sg.popup(f'PDF gerado com SUCESSO!\n O ficheiro encontra-se arquivado na pasta\"arquivospdf\ alunos\" do SMS. :)')
        elif event == '-atualizar_alunos-':
            janela_alunos.hide()
            janela_alunos = interface.janela_menu_aluno()
        elif event == '-ICONE_CASA-':
            janela_alunos.hide()
            janela_principal = interface.janela_menu_casa()
        elif event == '-ICONE_SALA-':
            janela_alunos.hide()
            janela_salas = interface.janela_menu_salas()
        elif event == '-ICONE_PROFESSORES-':
            janela_alunos.hide()
            janela_professores = interface.janela_menu_docentes()
        elif event == '-ICONE_ALUNOS-':
            janela_alunos.hide()
            janela_alunos = interface.janela_menu_aluno()
        elif event == '-ICONE_CURSOS-':
            janela_alunos.hide()
            janela_cursos = interface.janela_menu_cursos()
        elif event == '-ICONE_MENSAGEM-':
            janela_alunos.hide()
            janela_mensagem = interface.janela_menu_mensagem()
        elif event == sg.WIN_CLOSED:
            break

    # Lógica da jannela Cursos
    if window == janela_cursos:
        if event == '-BOTAO_CADASTRAR_NOVO_CURSO-':
            if values['-NOME_DO_CURSO-'] == '':
                sg.theme('DarkRed1')
                sg.Popup('Não deve deixar o campo \"Curso\" em Branco', title='SMS - ERRO')
            elif values['-TURNO_DO_CURSO-'] == '':
                sg.theme('DarkRed1')
                sg.Popup('Não deve deixar o campo \"Turnos\" em Branco', title='SMS - ERRO')
            else:
                try:
                    cursos_cadastrados = 'arquivostxt\\Cursos Cadastrados.txt'
                    arquivo.criarArquivoCursos(cursos_cadastrados, values['-NOME_DO_CURSO-'], values['-TURNO_DO_CURSO-'])
                    arquivo_cursos = open(cursos_cadastrados, 'rt', encoding='utf-8')
                    ler_cursos = arquivo_cursos.read()
                    window['-MOSTRAR_CURSOS-'].update(ler_cursos)
                    arquivo_cursos.close()
                    arquivo_cursos = open(cursos_cadastrados, 'rt', encoding='utf-8')
                    ler_cursos = arquivo_cursos.readlines()
                    cont_cursos = 0
                    for cursos in ler_cursos:
                        cont_cursos += 1
                    numero_de_cursos = cont_cursos
                    window['-CURSOS_NUMERO_CURSOS-'].update(f'{numero_de_cursos} Cursos Cadastrados')
                except:
                    sg.theme('DarkRed1')
                    sg.Popup(f'Ocorreu um erro ao Cadastrar o Curso \"{values["-NOME_DO_CURSO-"]}\" :(', title='SMS - ERRO')
                else:
                    sg.theme('DefaultNoMoreNagging')
                    sg.popup_timed(f'Cadastro efetuado com SUCESSO!')

        elif event == '-ICONE_CASA-':
            janela_cursos.hide()
            janela_principal = interface.janela_menu_casa()
        elif event == '-ICONE_SALA-':
            janela_cursos.hide()
            janela_salas = interface.janela_menu_salas()
        elif event == '-ICONE_PROFESSORES-':
            janela_cursos.hide()
            janela_professores = interface.janela_menu_docentes()
        elif event == '-ICONE_ALUNOS-':
            janela_cursos.hide()
            janela_alunos = interface.janela_menu_aluno()
        elif event == '-ICONE_CURSOS-':
            janela_cursos.hide()
            janela_cursos = interface.janela_menu_cursos()
        elif event == '-ICONE_MENSAGEM-':
            janela_cursos.hide()
            janela_mensagem = interface.janela_menu_mensagem()
        elif event == sg.WIN_CLOSED:
            break

    # Lógica da jannela Mensagens
    if window == janela_mensagem:
        if event =='-BOTAO_ENVIAR_MENSAGEM-':
            if values['-NOME_DA_PESSOA-'] == '':
                sg.theme('DarkRed1')
                sg.Popup('Não deve deixar o campo \"Nome\" em Branco', title='SMS - ERRO')
            elif values['-CAMPO_EMAIL-'] == '':
                sg.theme('DarkRed1')
                sg.Popup('Não deve deixar o campo \"E-mail\" em Branco', title='SMS - ERRO')
            elif values['-CAMPO_AASUNTO-'] == '':
                sg.theme('DarkRed1')
                sg.Popup('Não deve deixar o campo \"Assunto\" em Branco', title='SMS - ERRO')
            elif values['-CAMPO_MENSAGEM-'] == '':
                sg.theme('DarkRed1')
                sg.Popup('Não deve deixar o campo \"Mensagem\" em Branco', title='SMS - ERRO')
            else:
                try:
                    arquivo.criarArquivoMensagens(values['-NOME_DA_PESSOA-'], values['-CAMPO_EMAIL-'], values['-CAMPO_AASUNTO-'], values['-CAMPO_MENSAGEM-'])
                except:
                    sg.theme('DarkRed1')
                    sg.Popup('Ocorreu um erro ao enviar a Mensagem :(', title='SMS - ERRO')
                else:
                    sg.theme('DefaultNoMoreNagging')
                    sg.popup(f'A sua mensagem foi enviada com SUCESSO!!\nEncontra-se arquivada na pasta\"arquivostxt\mensagensSMS\" do SMS.')

        elif event == '-ICONE_CASA-':
            janela_mensagem.hide()
            janela_principal = interface.janela_menu_casa()
        elif event == '-ICONE_SALA-':
            janela_mensagem.hide()
            janela_salas = interface.janela_menu_salas()
        elif event == '-ICONE_PROFESSORES-':
            janela_mensagem.hide()
            janela_professores = interface.janela_menu_docentes()
        elif event == '-ICONE_ALUNOS-':
            janela_mensagem.hide()
            janela_alunos = interface.janela_menu_aluno()
        elif event == '-ICONE_CURSOS-':
            janela_mensagem.hide()
            janela_cursos = interface.janela_menu_cursos()
        elif event == '-ICONE_MENSAGEM-':
            janela_mensagem.hide()
            janela_mensagem = interface.janela_menu_mensagem()
        elif event == sg.WIN_CLOSED:
            break
window.close()
