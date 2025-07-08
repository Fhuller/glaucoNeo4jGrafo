# Neo4j + LangChain CLI

Uma interface de linha de comando (CLI) para interagir com um banco de dados Neo4j usando LangChain e OpenAI GPT para consultas em linguagem natural.

## Funcionalidades

- **Conexão Neo4j**: Conecta-se ao banco de dados Neo4j usando credenciais do arquivo `.env`
- **Teste de Conexão**: Verifica se a conexão com o banco está funcionando
- **Exploração de Schema**: Visualiza a estrutura do banco de dados
- **Consultas com LLM**: Faz perguntas em linguagem natural que são convertidas em Cypher
- **Execução Cypher**: Executa comandos Cypher diretamente no banco
- **Modo Interativo**: Shell interativo para executar múltiplos comandos Cypher

## Requisitos

### Dependências Python

```bash
pip install langchain-neo4j langchain-openai python-dotenv
```

### Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
# Neo4j
NEO4J_URL=neo4j+s://bd752129.databases.neo4j.io
NEO4J_USER=neo4j
NEO4J_PASS=YLvT9I-usX5xBNGnZmM5ZSryALHXhMQbjFJLezsBGy0
NEO4J_DATABASE=neo4j

# OpenAI
OPENAI_API_KEY=sua_chave_openai_aqui
```

## Uso

### Testar Conexão

```bash
python main.py testar
```

Verifica se a conexão com o Neo4j está funcionando corretamente.

### Visualizar Schema

```bash
python main.py schema
```

Exibe a estrutura do banco de dados (nós, relacionamentos, propriedades).

### Fazer Perguntas com LLM

```bash
python main.py perguntar "Quais são os personagens principais?"
```

Faz uma pergunta em linguagem natural que é convertida automaticamente em Cypher pela LLM.

### Executar Cypher Único

```bash
python main.py cypher "MATCH (n) RETURN count(n)"
```

Executa um comando Cypher específico no banco de dados.

### Modo Interativo Cypher

```bash
python main.py cypher-shell
```

Abre um shell interativo onde você pode executar múltiplos comandos Cypher. Digite `exit` para sair.

## Estrutura do Projeto

```
projeto/
├── main.py          # Código principal da CLI
├── .env             # Variáveis de ambiente (não incluir no git)
├── README.md        # Este arquivo
└── requirements.txt # Dependências (opcional)
```

## Exemplo de Uso

```bash
# Testar conexão
python main.py testar

# Ver estrutura do banco
python main.py schema

# Perguntar sobre dados
python main.py perguntar "Quantos nós existem no banco?"

# Executar Cypher direto
python main.py cypher "MATCH (n:Person) RETURN n.name LIMIT 5"

# Modo interativo
python main.py cypher-shell
cypher> MATCH (n) RETURN count(n)
cypher> MATCH (n:Person) RETURN n.name
cypher> exit
```

## Configuração do Neo4j

1. Instale o Neo4j Desktop ou use Neo4j Aura
2. Crie um banco de dados
3. Configure as credenciais no arquivo `.env`
4. Popule o banco com dados (nós e relacionamentos)

## Segurança

⚠️ **Importante**: O código usa `allow_dangerous_requests=True` para permitir que a LLM execute comandos Cypher. Em produção, considere implementar validações adicionais.

## Troubleshooting

### Erro de Conexão Neo4j
- Verifique se o Neo4j está rodando
- Confirme as credenciais no arquivo `.env`
- Teste a conexão usando o Neo4j Browser

### Erro OpenAI API
- Verifique se a chave da API está correta
- Confirme se há créditos disponíveis na conta OpenAI
- Teste com um modelo diferente se necessário

### Erro de Schema
- Certifique-se que o banco tem dados
- Verifique se o usuário tem permissões adequadas

## Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
