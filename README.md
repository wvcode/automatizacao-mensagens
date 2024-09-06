# Script para Envio de Mensagens em Massa

## Descrição

Este script Python automatiza o envio de mensagens personalizadas em massa. Ele utiliza as bibliotecas `pywhatkit` e `pandas` para enviar mensagens de um arquivo Excel para uma lista de contatos.

## Requisitos

Certifique-se de ter os seguintes requisitos instalados em seu sistema:

- Python 3.6 ou superior
- Bibliotecas Python:
    - pywhatkit
    - pandas
    - typer
    - openpyxl

Você pode instalar as bibliotecas necessárias usando o `pip`:

```bash
pip install pywhatkit pandas typer openpyxl
```

## Configuração

1. **Arquivo de Configuração (config.py):**
   - Crie um arquivo chamado `config.py` no mesmo diretório do script.
   - Defina as seguintes variáveis no arquivo `config.py`:
     - `DATA_FOLDER`: Caminho para a pasta onde o arquivo Excel com os dados está localizado.
     - `DATA_FILE`: Nome do arquivo Excel (ex: `dados.xlsx`).
     - `MSG_INTERVAL`: Intervalo de tempo em minutos entre o envio de cada mensagem.


   ```python
   DATA_FOLDER = "data"
   DATA_FILE = "contatos.xlsx"
   MSG_INTERVAL = 1
   ```

2. **Arquivo de Dados (contatos.xlsx):**
   - Crie um arquivo Excel chamado `contatos.xlsx` (ou o nome que você definiu em `DATA_FILE`) na pasta especificada em `DATA_FOLDER`.
   - Crie duas abas no arquivo Excel:
      - **pessoas:**
          - Colunas:
              - `nome`: Nome do contato (obrigatório)
              - `numero`: Número de telefone do contato no formato internacional (obrigatório)
              - `tag`: Tag para filtrar contatos (opcional)
      - **mensagens:**
          - Colunas:
              - `mensagem`: Mensagem a ser enviada (obrigatório)
              - `tag`: Tag para filtrar mensagens (opcional)

## Execução

1. Abra um terminal ou prompt de comando no diretório do script.
2. Execute o script usando o comando:

```bash
python script.py <tag_pessoas> <tag_mensagem>
```

Substitua `<tag_pessoas>` e `<tag_mensagem>` pelas tags correspondentes no seu arquivo Excel para filtrar as pessoas e mensagens que você deseja enviar. Se você não estiver usando tags, basta passar uma string vazia `""` para ambos os argumentos.

**Exemplo:**

```bash
python script.py "amigos" "aniversario"
```

Isso enviará as mensagens com a tag "aniversario" para os contatos com a tag "amigos".

## Observações

- Certifique-se de ter o WhatsApp Web aberto no seu navegador padrão e logado na sua conta.
- O script enviará as mensagens na ordem em que aparecem no arquivo Excel.
- O intervalo de tempo entre as mensagens é definido pela variável `MSG_INTERVAL` no arquivo `config.py`.
- Este script foi desenvolvido para fins educacionais e de demonstração. Use-o com responsabilidade e respeite os termos de serviço do WhatsApp.
```