# Livraria Folha Solta

Site de uma livraria básica, conectado a uma API Flask. Projeto da Atividade 3 de Desenvolvimento de Websites (DWS), 4º bimestre.

**Autor:** SEU NOME  
**Turma:** SUA TURMA

## O que o projeto faz

- Lista os livros do banco de dados na página (requisição `GET`).
- Cadastra novos livros por um formulário (requisição `POST`).
- Atualiza o catálogo na tela depois do cadastro, sem recarregar a página.
- Permite buscar por título ou autor e filtrar por gênero.
- Tem uma sacola de compras com total e controle de quantidade (simulação, nada é salvo no banco).
- Mostra mensagens de erro na tela quando a API não responde ou recusa o cadastro.

## Tecnologias

- HTML, CSS e JavaScript (`fetch`, `async/await`, `try/catch`)
- Python com Flask e Flask-CORS
- SQLite

## Como rodar

1. Instale as dependências:

   ```
   pip install flask flask-cors
   ```

2. Inicie a API:

   ```
   python app.py
   ```

   A API fica disponível em `http://localhost:5000`. O banco `livraria.db` é criado automaticamente na primeira execução.

3. Abra o arquivo `index.html` no navegador. Deixe o terminal da API aberto enquanto usa o site.

## Rotas da API

| Método | Rota      | O que faz                  | Corpo (JSON)                              |
|--------|-----------|----------------------------|-------------------------------------------|
| GET    | `/livros` | Lista todos os livros      | -                                         |
| POST   | `/livros` | Cadastra um novo livro     | `titulo`, `autor`, `genero`, `preco`      |

Exemplo de corpo do `POST`:

```json
{
  "titulo": "Dom Casmurro",
  "autor": "Machado de Assis",
  "genero": "Romance",
  "preco": 29.9
}
```

O `POST` responde com status `201` quando o livro é cadastrado e `400` quando falta algum campo ou o preço é inválido.

## Estrutura de arquivos

```
.
├── index.html   # front-end (página, estilos e JavaScript)
├── app.py       # API Flask com CORS e banco SQLite
├── .gitignore
└── README.md
```

## Requisitos da atividade

- [x] CORS ativado na API Flask (`CORS(app)`)
- [x] Requisição GET exibindo os dados do banco
- [x] Formulário conectado a uma requisição POST (`Content-Type: application/json` e `JSON.stringify`)
- [x] Lista atualizada automaticamente após o cadastro
- [x] Código publicado no GitHub
