import csv
import re
import sys

# 1. Criação de Exceção Personalizada
class FormatoInvalidoError(Exception):
    """Exceção levantada quando um dado não bate com o padrão Regex exigido."""
    def __init__(self, mensagem):
        super().__init__(mensagem)

# 2. Funções de Validação com Expressões Regulares (Regex)
def validar_email(email):
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(padrao, email):
        raise FormatoInvalidoError(f"E-mail inválido: {email}")

def validar_cpf(cpf):
    padrao = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
    if not re.match(padrao, cpf):
        raise FormatoInvalidoError(f"CPF inválido (use XXX.XXX.XXX-XX): {cpf}")

def validar_telefone(telefone):
    padrao = r"^\(\d{2}\)\s\d{4,5}-\d{4}$"
    if not re.match(padrao, telefone):
        raise FormatoInvalidoError(f"Telefone inválido (use (XX) XXXXX-XXXX): {telefone}")

def validar_data(data):
    # Formato DD/MM/AAAA
    padrao = r"^(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/\d{4}$"
    if not re.match(padrao, data):
        raise FormatoInvalidoError(f"Data inválida (use DD/MM/AAAA): {data}")

# 3. Função Principal de Processamento
def analisar_dados(caminho_arquivo):
    total_registros = 0
    registros_validos = 0
    registros_invalidos = 0
    erros_detalhados = []

    print("Iniciando análise de dados...\n")

    # Tratamento de Exceções: Arquivo não encontrado
    try:
        with open(caminho_arquivo, mode="r", encoding="utf-8") as arquivo:
            leitor_csv = csv.DictReader(arquivo)
            
            # Validando se as colunas necessárias existem (KeyError prevention/trigger)
            colunas_obrigatorias = ["nome", "email", "cpf", "telefone", "data", "idade"]
            for col in colunas_obrigatorias:
                if col not in leitor_csv.fieldnames:
                    raise KeyError(f"Coluna obrigatória ausente no arquivo: '{col}'")

            for linha in leitor_csv:
                total_registros += 1
                try:
                    # Tentativa de conversão para forçar ValueError se não for número
                    idade = int(linha["idade"]) 
                    
                    # Validações Regex
                    validar_email(linha["email"])
                    validar_cpf(linha["cpf"])
                    validar_telefone(linha["telefone"])
                    validar_data(linha["data"])
                    
                except ValueError as e:
                    registros_invalidos += 1
                    erros_detalhados.append(f"Linha {total_registros} ({linha['nome']}): Erro de valor - A idade deve ser um número inteiro.")
                except FormatoInvalidoError as e:
                    registros_invalidos += 1
                    erros_detalhados.append(f"Linha {total_registros} ({linha['nome']}): {e}")
                else:
                    # Executa se NENHUMA exceção ocorrer no bloco try interno
                    registros_validos += 1
                finally:
                    # Executa sempre, linha a linha
                    pass # Poderia ser usado para logar o progresso da leitura

    except FileNotFoundError:
        print(f"❌ ERRO CRÍTICO: O arquivo '{caminho_arquivo}' não foi encontrado.")
        sys.exit(1)
    except KeyError as e:
        print(f"❌ ERRO CRÍTICO DE ESTRUTURA: {e}")
        sys.exit(1)
    finally:
        # Executa independentemente de o arquivo existir ou falhar no meio
        print("-" * 50)
        print("Processo de leitura finalizado pelo sistema.")
        print("-" * 50)

    # 4. Geração de Relatório Formatado com f-strings
    relatorio = f"""
    📊 RELATÓRIO FINAL DE ANÁLISE DE DADOS 📊
    =========================================
    Total de registros analisados : {total_registros}
    ✅ Registros Válidos          : {registros_validos}
    ❌ Registros Inválidos        : {registros_invalidos}
    =========================================
    """
    print(relatorio)
    
    if registros_invalidos > 0:
        print("🔍 Detalhamento dos Erros:")
        for erro in erros_detalhados:
            print(f"  - {erro}")

if __name__ == "__main__":
    analisar_dados("dados.csv")
