# Web Scraping e Manipulação de Dados com Python

Esse projeto foi desenvolvido para fazer scraping de um site específico (https://imepac.edu.br/) e coletar dados como imagens e cabeçalhos. A ideia é pegar esses dados da página, salvá-los de forma organizada em formatos como JSON, CSV e Excel, e ainda modificar o conteúdo HTML. Usei Python para isso, com algumas bibliotecas poderosas que facilitam bastante o trabalho!

Tecnologias e Ferramentas:

Python: A principal linguagem utilizada para automação e manipulação de dados.

BeautifulSoup: Para fazer o scraping da página HTML e extrair os dados de forma fácil.

Pandas: Para manipulação e organização dos dados, gerando os arquivos JSON, CSV e Excel.

openpyxl: Para criar e salvar o arquivo Excel.

Requests: Para fazer as requisições HTTP e pegar os dados da página.

Como funciona:

O código começa com uma requisição HTTP para o site e utiliza o BeautifulSoup para entender e extrair as informações da página. Depois, ele pega todas as imagens e cabeçalhos encontrados e salva esses dados de maneira bem organizada. O projeto também tem a função de modificar o conteúdo do HTML, como adicionar ou alterar tags.
Eu fiz tudo isso usando o VS Code, que é minha IDE favorita para programar. É bem simples de rodar o código, só precisar de um ambiente Python configurado.
