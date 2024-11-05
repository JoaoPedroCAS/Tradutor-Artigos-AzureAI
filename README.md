# Tradutor de Documentos e Artigos com Azure OpenAI

Este repositório contém dois scripts Python para tradução automática de textos usando a API Azure OpenAI e o Microsoft Translator. O primeiro script, `tradutor_documentos_azure`, realiza a tradução de documentos `.docx`, enquanto o segundo, `tradutor_artigos_azure`, extrai e traduz o conteúdo textual de uma URL.

## Pré-requisitos

- Python 3.8 ou superior
- [Microsoft Translator Text API](https://learn.microsoft.com/en-us/azure/cognitive-services/translator/) (necessário para `tradutor_documentos_azure`)
- [Azure OpenAI](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/) (necessário para `tradutor_artigos_azure`)
- Bibliotecas Python:
  - `requests`
  - `beautifulsoup4`
  - `python-docx`
  - `langchain_openai`

Instale as dependências via pip:
```bash
pip install requests beautifulsoup4 python-docx langchain_openai
```

## Configuração

Crie uma conta nas APIs do Azure e obtenha suas chaves de API e Endpoints. Altere os valores das variáveis `subscription_key`, `endpoint`, `location`, `api_key`, `azure_endpoint`, e outras informações de autenticação nos scripts conforme necessário.

### Estrutura dos Arquivos

- `tradutor_documentos_azure.py`: Traduz o conteúdo de um arquivo `.docx` do inglês para o idioma especificado.
- `tradutor_artigos_azure.py`: Extrai o texto de uma URL, limpa o conteúdo, e traduz o texto para o idioma especificado.

## Uso

### `tradutor_documentos_azure`

Este script realiza a tradução de um documento Word (.docx) de um idioma para outro.

1. Abra o arquivo `tradutor_documentos_azure.py`.
2. Defina o valor de `input_file` com o caminho do documento a ser traduzido.
3. Execute o script:

   ```bash
   python tradutor_documentos_azure.py
   ```

4. O arquivo traduzido será salvo no mesmo diretório com o sufixo `_translated_document.docx`.

### `tradutor_artigos_azure`

Este script extrai o texto de uma URL e traduz para o idioma desejado.

1. Abra o arquivo `tradutor_artigos_azure.py`.
2. Defina o valor da variável `url` com a URL do artigo a ser traduzido.
3. Defina o idioma de destino na variável `lang`.
4. Execute o script:

   ```bash
   python tradutor_artigos_azure.py
   ```

5. A tradução será exibida no console e também pode ser manipulada conforme necessário.

## Observações

- **Limitações da API**: Verifique o número máximo de tokens permitido para tradução e possíveis custos associados ao uso das APIs.
- **Tratamento de Erros**: Os scripts incluem tratamento básico de erros de conexão e resposta HTTP. Customize conforme necessário para seu ambiente.

## Contribuição

Sinta-se à vontade para abrir issues e enviar pull requests para melhorias e novas funcionalidades.