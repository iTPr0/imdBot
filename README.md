# <p align="center">Seja bem-vindo(a) 🎬🤖</p>

### <p align="center">É um bot do Telegram desenvolvido em Python que fornece informações sobre filmes e séries, utilizando a API do The Movie Database (TMDb).</p>

### Pré-requisitos
Antes de começar, certifique-se de ter os seguintes requisitos instalados:

- Python 3.6 ou superior
- Pip (gerenciador de pacotes do Python)
- Um token de API do Telegram (obtenha um [aqui](https://core.telegram.org/bots#botfather))
- Uma chave de API do The Movie Database (TMDB) (obtenha uma [aqui](https://www.themoviedb.org/documentation/api))

## Passos de Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/imdBot.git
```

Ou faça o download do arquivo [imdBot.zip](https://github.com/iTPr0/imdBot/files/13704438/imdBot.zip)

## Acesse o diretório do projeto:
```
cd imdBot
```

## Ative o ambiente virtual no Windows:
```bash
venv\Scripts\activate
```

## No macOS/Linux:
```bash
source venv/bin/activate
```

## Instale as dependências:
```bash
pip install requests
pip install urllib3
pip install python-dotenv
pip install --upgrade python-telegram-bot
pip install python-telegram-bot --upgrade
pip install -r requirements.txt
```

## Crie um arquivo .env na raiz do projeto e adicione as chaves de API necessárias:
```
TMDB_API_KEY=your_tmdb_api_key
```

Certifique-se de substituir `your_tmdb_api_key` pelas suas chaves de API do The Movie Database (TMDb) e do Telegram Bot, respectivamente.

## Execute o bot:
```
python imdBot.py
```
Agora o bot está pronto para uso!

### Comandos disponíveis:
1. `/start`: Inicie o bot no Telegram clicando em /start.
2. `/tools`: Exibe uma lista de ferramentas disponíveis.
3. `/info`: Mostra informações sobre o desenvolvedor.
4. `/restart`: Reinicia o bot.

### Como usar
Para obter informações sobre um filme ou série, digite @ seguido pelo nome desejado.

### Contribuições :handshake:
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues, pull requests ou reportar bugs.

### ❤️ Apoio, suporte.

Se por acaso você adora este projeto, deixe uma estrela no repo.

<div align="center">
 <img src="https://github-production-user-asset-6210df.s3.amazonaws.com/66981750/262346028-b6bf186e-5554-4736-a192-956402c5b0db.jpg" width="15%" height="15%">
<br/>

[![WebSite](https://img.shields.io/badge/website-000000?style=for-the-badge&logo=About.me&logoColor=white)](https://links.tifodao.com)

</div>

<div align="center">
Desenvolvido com ❤️ no Brasil 🌟 <br/>

[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://www.javascript.com/)

</div>

### Contato
Para mais informações, entre em contato com o desenvolvedor [@tifodao](https://t.me/tifodao).

### Licença :page_facing_up:

Este projeto é licenciado sob a Licença MIT.

```
MIT License

Copyright (c) [2023] [Diego Melo]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
