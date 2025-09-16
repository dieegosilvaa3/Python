import random
import re
from datetime import datetime #biblioteca de data de nascimento

def nome_completo():
  while True:
    nome = input("Nome Completo: ")
    if all(char.isalpha() or char.isspace() for char in nome): #duas funções para validade espaço e chars(letras do alfabeto)
      nome_formatado = nome.title()
      return nome_formatado
    else:
      print("Campo não pode ser preenchido com números e figuras, tente novamente:")
def data_nascimento(validacao):
    try:  #conversor de inteiros
      nascimento = datetime.strptime(validacao, "%d/%m/%Y")
      return nascimento
    except ValueError: #retornar valor errado
      return 0
def numero_cpf():
  while True:
    cpf = input("CPF (digite somente os números: ): ")
    if len(cpf) == 11:
      if all(int.isnumeric() for int in cpf):
        return cpf
      elif len(cpf) != 11:
        return False
    print("CPF inválido, tente novamente: ")
def numero_telefone():
    while True:
        telefone = input("Número de telefone com DDD (somente números): ")
        if re.match(r"^\d{11}$", telefone):  #
            telefone = f"({telefone[:2]}){telefone[2:7]}-{telefone[7:]}"
            return telefone
        else:
            print("Número de telefone inválido. Por favor, digite novamente.")
def email_1():
    while True:
        email = input("Endereço de e-mail: ")
        if "@" in email and "." in email:
            email_formatado = email.lower()
            return email_formatado
        else:
            print("Endereço de e-mail inválido. Por favor, digite novamente.")
def mae_1():
    while True:
        mae = input("Nome da mãe: ")
        if all(char.isalpha() or char.isspace() for char in mae):
            mae_formatada = mae.title()
            return mae_formatada
        else:
            print("Campo não pode ser preenchido com números e figuras, tente novamente.")
def endereço_completo():
    endereço = [] #para que a função seja realizada, o vetor deve ser adicionado dentro da função, assim todas as informações serão validadas quando o def for concluído.
    while True:
        rua = input("Rua: ").strip()
        if rua and all(char.isalpha() or char.isspace() or char.isdigit() for char in rua):
            rua = rua.title()
            break
        else:
            print("Informação incorreta, por favor tente novamente.")
            continue
    while True:
        numero_casa = input("Número: ").strip()
        if numero_casa.isdigit():
            numero_casa = numero_casa
            break
        else:
            print("Informação incorreta, por favor tente novamente.")
            continue
    while True:
        bairro = input("Bairro: ").strip()
        if bairro and all(char.isalpha() or char.isspace() for char in bairro):
            bairro = bairro.title()
            break
        else:
            print("Informação incorreta, por favor tente novamente.")
            continue
    while True:
        cidade = input("Cidade: ").strip()
        if cidade and all(char.isalpha() or char.isspace() for char in cidade):
            cidade = cidade.title()
            break
        else:
            print("Informação incorreta, por favor tente novamente.")
            continue
    while True:
        estado = input("Estado: ").strip()
        if estado and all(char.isalpha() or char.isspace() for char in estado):
            estado = estado.title()
            break
        else:
            print("Informação incorreta, por favor tente novamente.")
            continue
    while True:
        cep = input("CEP: ").strip()
        if len(cep) == 8 and cep.isdigit():
            cep = cep
            break
        else:
            print("Informação incorreta, por favor tente novamente.")
            continue
    endereço.append([rua, numero_casa, bairro, cidade, estado, cep])
    return endereço
def mostrar_endereço(endereço):
    for linha in endereço:
        print(f"Endereço Completo:\nRua: {linha[0]}, Nº: {linha[1]}\nBairro: {linha[2]}\nCidade: {linha[3]}\nEstado: {linha[4]}\nCEP: {linha[5]}")
def gerar_matricula():
  while True:
    if nascimento != 0:
      num = random.randint(10000, 99999)
      return num
    elif (num == aluno[0]):
      print("Error!")
      num = random.randint(10000, 99999)
      return 0
def consultar_aluno(num):
  for aluno in alunos:
    if aluno[0] == num:
      print("==================================================================")
      print("                     Informações do Aluno:                        ")
      print("==================================================================")
      print("Nome:", aluno[1])
      print("Data de nascimento:", aluno[2])
      print("CPF:", aluno[3])
      print("Telefone:", aluno[4])
      print("E-mail:", aluno[5])
      print("Nome da mãe:", aluno[6])
      print("Endereço:", mostrar_endereço(endereço)) #chamando função
      print("Disciplina:", aluno[8])
      print("==================================================================")
      return
    else:
      print("Matrícula não encontrada.")
cont = 0
num = 0
aluno = 0
alunos = []
# Dicionário para mapear siglas e nomes das disciplinas
disciplinas = {
    "ADM": "Administração",
    "ADS": "Análise e Desenvolvimento de Sistemas",
    "MKT": "Marketing"
}
while True:
  print("\nMenu:")
  print("1. Cadastrar aluno")
  print("2. Consultar aluno")
  print("3. Sair")
  opcao = input("Escolha uma opção: ")

  if opcao == "1":
    #Cada função terá sua condição para impedir erros na programação
    print("==================================================================")
    print("======================Sessão de Matrículas========================")
    print("Preencha as informações abaixo:")
    nome = nome_completo() #chamando função
    while cont != 1:
        nascimento = input("Data de Nascimento (Formato: dd/mm/aaaa): ")
        if data_nascimento(nascimento): #chamando função
            cont = 1
        else:
            print("Data inválida, digite novamente")
            cont = 0
    if cont == 1:
      cont = 0
    nascimento = data_nascimento(nascimento) #chamando função
    cpf = numero_cpf() #chamando função
    telefone = numero_telefone() #chamando função
    email = email_1() #chamando função
    mae = mae_1() #chamando função
    endereço = endereço_completo() #chamando função
    mostrar_endereço(endereço) #chamando função
    num = gerar_matricula() #chamando função
    print(' ')
    print("===========================Disciplinas============================")
    print(' ')
    nome_disciplina = ""
    while True:
      disciplina = str(input("Informe a sigla da disciplina que deseja cursar:\n" "ADM - Administração\n" "ADS - Análise e Desenvolvimento de Sistemas\n" "MKT - Marketing\n")).upper().strip()  # Converte para maiúsculas e remove espaços em branco
      print(" ")
      if disciplina in disciplinas:
          nome_disciplina = disciplinas[disciplina]
          break  # Sai do loop se a disciplina for válida
      else:
          print("Sigla de disciplina inválida. Por favor, digite uma sigla válida.")
          print(" ")
    print("Disciplina:", nome_disciplina)
    print("Número da Matrícula", num)
    print(" ")
    alunos.append([num, nome, nascimento.strftime("%d/%m/%Y"), cpf, telefone, email, mae, endereço, nome_disciplina])
  elif opcao == "2":
        try:
            consultar_matricula = int(input("Informe o número de matrícula: "))
            consultar_aluno(consultar_matricula)
        except ValueError:
            print("Número de matrícula inválido. Por favor, tente novamente.")
  elif opcao == "3":
    break
  else:
    print("Opção inválida.")
