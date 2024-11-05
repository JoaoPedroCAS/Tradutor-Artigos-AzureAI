import requests
from bs4 import BeautifulSoup
from langchain_openai.chat_models.azure import AzureChatOpenAI

# Função para extrair o texto limpo de uma URL
def extract_text_from_url(url):
    # Faz uma requisição para a URL
    response = requests.get(url)
    
    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Converte o conteúdo da página em um objeto BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove todos os elementos 'script' e 'style' para evitar textos irrelevantes
        for script_style in soup(["script", "style"]):
            script_style.decompose()
        
        # Extrai o texto visível na página
        text = soup.get_text(separator=' ')
        
        # Remove linhas e espaços desnecessários para limpar o texto
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        
        return text
    else:
        # Em caso de falha na requisição, exibe o código de erro
        print(f"Failed to fetch the URL. Status code: {response.status_code}")
        return None

# Exemplo de uso da função com uma URL de entrada
url = "YOUR_URL"
text = extract_text_from_url(url)

# Configuração do cliente AzureChatOpenAI para tradução de texto
client = AzureChatOpenAI(
    azure_endpoint="YOUR_ENDPOINT",
    api_key="YOUR_API_KEY",
    api_version="YOUR_API_VERSION",
    deployment_name="YOUR_DEPLOYMENT_NAME",
    max_retries=3  # Aumentamos para 3 tentativas em caso de falha na API
)

# Função para traduzir um texto extraído para o idioma desejado
def translate_article(text, lang):
    # Define as mensagens para a API do Azure Chat
    messages = [
        ("system", "Você atua como tradutor de textos"),
        ("user", f"Traduza o texto a seguir para o idioma {lang} e responda em markdown:\n\n{text}")
    ]
    
    # Invoca a API de tradução e captura a resposta
    response = client.invoke(messages)
    print(response.content)  # Exibe a tradução no console
    return response.content

# Defina o idioma alvo para tradução e execute a tradução
lang = "YOUR_LANGUAGE"
if text:  # Verifica se o texto foi extraído com sucesso antes de traduzir
    translate_article(text, lang)
