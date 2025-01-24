
# Aplicativo de Redimensionamento de Imagens 📸

Bem-vindo ao **Aplicativo de Redimensionamento de Imagens**, uma ferramenta simples e eficiente para redimensionar suas imagens de maneira rápida e prática.

## Descrição

Este aplicativo web, desenvolvido com **Streamlit**, permite que você faça upload de múltiplas imagens, defina as dimensões desejadas e baixe as imagens redimensionadas em um único arquivo ZIP. Ideal para fotógrafos, designers e qualquer pessoa que precise ajustar o tamanho de suas imagens com facilidade.

## Funcionalidades

- **Upload Multiplo**: Carregue várias imagens simultaneamente nos formatos JPG, JPEG, PNG, BMP, GIF e TIFF.
- **Redimensionamento Personalizado**: Defina a largura e a altura desejadas para suas imagens.
- **Download em ZIP**: Após o redimensionamento, baixe todas as suas imagens em um único arquivo compactado.
- **Interface Intuitiva**: Interface amigável e fácil de usar, permitindo uma experiência rápida e eficiente.

## Tecnologias Utilizadas

- **Python 3.10**
- **Streamlit**
- **Pillow (PIL)**
- **Zipfile**
- **Outras Bibliotecas**: Consulte o arquivo `requirements.txt` para uma lista completa de dependências.

## Instalação

1. **Clone o repositório**

    ```bash
    git clone 
    cd "nome_projeto"
    ```

2. **Crie um ambiente virtual**

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # No Windows: .venv\Scripts\activate
    ```

3. **Instale as dependências**

    ```bash
    pip install -r requirements.txt
    ```

## Como Usar

1. **Execute o aplicativo**

    ```bash
    streamlit run app.py
    ```

2. **Acesse no Navegador**

    Abra o navegador e vá para `http://localhost:8501` para acessar o aplicativo.

3. **Redimensione suas Imagens**

    - Carregue as imagens desejadas.
    - Defina a largura e altura desejadas.
    - Clique em "Redimensionar Imagens".
    - Baixe o arquivo ZIP com as imagens redimensionadas.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorar este projeto.


