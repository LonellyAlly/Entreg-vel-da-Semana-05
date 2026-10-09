# Sistema de Análise de Dados em Python (Sprint 5)

Este projeto é um sistema em Python para leitura, validação e análise de arquivos de dados (CSV). Ele foi desenvolvido para consolidar conceitos de manipulação de arquivos, Expressões Regulares (Regex) e Tratamento de Exceções em Python.

## 📌 Funcionalidades
- Leitura segura de arquivos `.csv` utilizando `with open(..., encoding="utf-8")`.
- Validação estrutural de dados através do módulo `re` (Regex).
- Tratamento rigoroso de exceções e fluxo de controle (`try`, `except`, `else`, `finally`).
- Emissão de um relatório gerencial no terminal utilizando `f-strings`.

## 🧠 Justificativa das Validações (Regex)
As seguintes regras de expressões regulares foram aplicadas para garantir a integridade dos dados:

1. **E-mail** (`^[\w\.-]+@[\w\.-]+\.\w+$`): 
   - `\w` garante que contenha caracteres alfanuméricos. 
   - Exige a presença de um `@` separando o usuário do domínio e um `.` no final (ex: `.com`).
2. **CPF** (`^\d{3}\.\d{3}\.\d{3}-\d{2}$`): 
   - `\d` força a entrada apenas de números. 
   - Obriga exatamente o padrão com pontos e traço: `XXX.XXX.XXX-XX`.
3. **Telefone** (`^\(\d{2}\)\s\d{4,5}-\d{4}$`): 
   - Exige parênteses escapados `\(` no DDD, um espaço `\s` obrigatório e suporte tanto a telefones fixos (4 dígitos) quanto celulares (5 dígitos) antes do hífen.
4. **Data** (`^(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/\d{4}$`):
   - Valida dias lógicos (01 a 31), meses lógicos (01 a 12) e um ano de 4 dígitos.

## 🛡️ Exceções Tratadas
Para evitar que o programa quebre de forma abrupta, os seguintes erros são tratados:
- `FileNotFoundError`: Captura o erro caso o arquivo `dados.csv` não exista no diretório, exibindo uma mensagem amigável e encerrando graciosamente.
- `KeyError`: Verifica se a estrutura do CSV possui as colunas esperadas (nome, email, cpf, etc.). Caso falte alguma, o script avisa qual está faltando.
- `ValueError`: Aplicado na coluna "idade", garantindo que falhas ao converter strings (ex: "trinta") para `int` sejam registradas como erro da linha em vez de parar a execução do código.
- `FormatoInvalidoError`: **Exceção Customizada**. Herdada da classe base `Exception`, é acionada exclusivamente quando as validações de Regex falham, separando erros de negócio de erros nativos do Python.

## 🚀 Exemplos de Entrada e Saída

**Exemplo do Arquivo Lido (`dados.csv`):**
```csv
nome,email,cpf,telefone,data,idade
Joao Silva,joao@email.com,123.456.789-00,(11) 91234-5678,10/05/2023,30
Maria Souza,maria.com,999.888.777-66,11999998888,25/12/2023,25
Pedro,pedro@email.com,111.222.333-44,(21) 98888-7777,32/13/2024,trinta
