import lib.data
from fpdf import FPDF


def arquivoExiste(nome):
    try:
        arquivo = open(nome, 'rt', encoding='utf-8')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome, nome_escola):
    arquivo = open(nome, 'wt+', encoding='utf-8')
    arquivo.write(nome_escola)
    arquivo.close()


def criarArquivoSala(nome, nome_sala):
    arquivo = open(nome, 'a+', encoding='utf-8')
    arquivo.write(f'{nome_sala}{lib.data.data_criação.rjust(130, ".")}\n')
    arquivo.close()


def criarArquivoDocente(nome_arquivo, nome_docente, disciplina):
    arquivo = open(nome_arquivo, 'a+', encoding='utf-8')
    arquivo.write(f'{nome_docente}{disciplina.rjust(130, ".")}\n')
    arquivo.close()


def criarArquivoAlunos(nome_arquivo, nome_alunos, idade):
    arquivo = open(nome_arquivo, 'a+', encoding='utf-8')
    arquivo.write(f'{nome_alunos}{idade.rjust(130, ".")} Anos\n')
    arquivo.close()


def criarArquivoCursos(nome_arquivo, nome_do_curso, turno):
    arquivo = open(nome_arquivo, 'a+', encoding='utf-8')
    arquivo.write(f'{nome_do_curso}{turno.rjust(130, ".")}\n')
    arquivo.close()


def criarArquivoMensagens(nome_da_pessoa, e_mail, assunto, mensagem):
    arquivo = open(f'arquivostxt\\mensagensSMS\\{assunto}.txt', 'w', encoding='utf-8')
    arquivo.write(f'Assunto: {assunto}\nNome: {nome_da_pessoa}\nE-mail:{e_mail}\nConteúdo da Mensagem:\n{mensagem}')
    arquivo.close()


# Para fazer validação de um número inteiro
def leiaint(msg):
    try:
        n1 = int(msg)
    except (ValueError, TypeError):
        # print('ERRO: Por favor digite um número inteiro válido')
        return False
    else:
        return True


# função para Gerar pdf (Docente)

pdf = FPDF('P', 'mm', 'Letter')
pdf.add_page()


def GerarPDF(nome_do_docente, salario_base, turmas_atribuidas, disciplinas_lecionar):
    # Corpo
    pdf.line(-15, 90, 210 - 105, 90)
    pdf.set_font('helvetica', '', 14)
    pdf.cell(-10, 180, 'Nome do(a) Docente:', align='L')
    pdf.cell(-10, 200, f'{"Salário Base:":>20}  {salario_base}(Euros)', align='L')
    pdf.cell(-10, 220, f'{"Turmas Atribuidas:":>31}  {turmas_atribuidas} turmas atribuidas', align='L')
    pdf.cell(-10, 240, f'{"Disciplina a Lecionar:":>42}  {disciplinas_lecionar}{"":>10}Data de Emissão: {lib.data.data_criação}', border=1,
             align='L')

    #Cabeçalho
    pdf.set_font('helvetica', 'BIU', 14)
    pdf.cell(0, 180, f'{nome_do_docente}', align='C')
    pdf.line(-15, 140, 210 - 105, 140)

    pdf.image('img\\para_pdf.png', 78, 10)
    pdf.set_font('times', '', 14)
    nome = 'Sistema de Gerenciamento Escolar'
    nome_baixo = '- Cadastro de Docentes'
    title_w = pdf.get_string_width(nome) + 6
    doc_w = pdf.w
    pdf.set_x((doc_w - title_w) / 2)
    pdf.cell(80, 75, nome, align='C')

    pdf.set_font('times', 'I', 14)
    title_w = pdf.get_string_width(nome_baixo) + 6
    doc_w = pdf.w
    pdf.set_x((doc_w - title_w) / 2)
    pdf.cell(55, 87, nome_baixo, align='C')
    pdf.set_font('helvetica', 'BIU', 14)
    docente = f'Dados do Docente {nome_do_docente}'
    title_w = pdf.get_string_width(docente) + 6
    doc_w = pdf.w
    pdf.set_x((doc_w - title_w) / 2)
    pdf.cell(85, 120, docente, align='C')

    pdf.output(f'arquivospdf\\Docentes\\{nome_do_docente} (Dados do Docente).pdf')
    pdf.close()


# Função Gerar PDF Estudantes
def GerarPdfAlunos(nome_aluno, data_nascimento, iade_do_aluno, documento_identificacao, numero_telefone, morada_aluno, c_n1, c_n2):
    # Corpo
    pdf.line(-15, 90, 210 - 105, 90)
    pdf.set_font('helvetica', '', 14)
    pdf.cell(-10, 180, f'Nome do(a) Aluno     :', align='L')
    pdf.cell(-10, 200, f'{"Data de Nascimento:":>26}  {data_nascimento}{"":>7}Idade: {iade_do_aluno} anos', align='L')
    pdf.cell(-10, 220, f'{"Nº Documento de Identificação:":>44}  {documento_identificacao}{"":>2}Telefone: {numero_telefone}', align='L')
    pdf.cell(-10, 240, f'{"Morada:":>29}  {morada_aluno}{"":>2}{c_n1}-{c_n2}', border=1,
             align='L')

    #Cabeçalho
    pdf.set_font('helvetica', 'BIU', 14)
    pdf.cell(0, 180, f'{nome_aluno}', align='C')
    pdf.line(-15, 140, 210 - 105, 140)

    pdf.image('img\\para_pdf.png', 78, 10)
    pdf.set_font('times', '', 14)
    nome = 'Sistema de Gerenciamento Escolar'
    nome_baixo = '- Cadastro de Alunos'
    title_w = pdf.get_string_width(nome) + 6
    doc_w = pdf.w
    pdf.set_x((doc_w - title_w) / 2)
    pdf.cell(80, 75, nome, align='C')

    pdf.set_font('times', 'I', 14)
    title_w = pdf.get_string_width(nome_baixo) + 6
    doc_w = pdf.w
    pdf.set_x((doc_w - title_w) / 2)
    pdf.cell(55, 87, nome_baixo, align='C')
    pdf.set_font('helvetica', 'BIU', 14)
    docente = f'Dados do Aluno {nome_aluno}'
    title_w = pdf.get_string_width(docente) + 6
    doc_w = pdf.w
    pdf.set_x((doc_w - title_w) / 2)
    pdf.cell(85, 120, docente, align='C')

    pdf.output(f'arquivospdf\\alunos\\{nome_aluno} (Dados do Aluno).pdf')
    pdf.close()


'''
def lerArquivo(nome):
    try:
        arquivo = open(nome, 'rt', encoding='utf-8')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho('LISTA DE PESSIAS CADASTRADAS')
        try:
            for linha in arquivo:
                dado = linha.split(';')
                dado[1] = dado[1].replace('\n', '')
                print(f'{dado[0]:<30}{dado[1]:>3} Anos')
        except UnicodeError:
            print('Houve um erro no Loop por causa do UTF-8')
        arquivo.close()'''


'''def leiaint(msg):
    while True:
        try:
            n1 = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: Por favor digite um número inteiro válido')
        except KeyboardInterrupt:
            print('O Usuário interrompeu a operação')
            return 0
        else:
            return n1


def leiafloat(msg):
    while True:
        try:
            n2 = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: Por favor digite um número real válido')
        else:
            return n2'''