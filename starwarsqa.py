import os
import argparse
from dotenv import load_dotenv
from langchain_neo4j import Neo4jGraph
from langchain.chains import GraphCypherQAChain
from langchain_openai import ChatOpenAI

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

def conectar_neo4j():
    return Neo4jGraph(
        url=os.getenv("NEO4J_URL"),
        username=os.getenv("NEO4J_USER"),
        password=os.getenv("NEO4J_PASS"),
        database=os.getenv("NEO4J_DATABASE")
    )

def testar_conexao():
    try:
        graph = conectar_neo4j()
        result = graph.query("RETURN 1 AS test")
        print("✅ Conexão estabelecida com sucesso.")
        print(f"Resultado: {result}")
    except Exception as e:
        print(f"❌ Erro na conexão: {e}")

def mostrar_schema():
    graph = conectar_neo4j()
    schema = graph.get_schema
    print("📋 Schema do banco:")
    print(schema)

def perguntar_llm(pergunta):
    graph = conectar_neo4j()
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

    qa_chain = GraphCypherQAChain.from_llm(
        llm=llm,
        graph=graph,
        verbose=True,
        allow_dangerous_requests=True
    )

    print(f"🧠 Pergunta: {pergunta}")
    resposta = qa_chain.invoke(pergunta)
    print(f"💬 Resposta: {resposta['result']}")

def executar_cypher_unico(query):
    graph = conectar_neo4j()
    try:
        result = graph.query(query)
        if not result:
            print("✅ Executado com sucesso (sem retorno).")
        else:
            print("📊 Resultado:")
            for row in result:
                print(row)
    except Exception as e:
        print(f"❌ Erro ao executar Cypher: {e}")

def executar_cypher_interativo():
    graph = conectar_neo4j()
    print("📝 Modo interativo Cypher iniciado. Digite 'exit' para sair.")
    while True:
        try:
            query = input("cypher> ")
            if query.strip().lower() in ("exit", "quit"):
                print("👋 Encerrando modo Cypher.")
                break
            if not query.strip():
                continue
            result = graph.query(query)
            if not result:
                print("✅ Executado com sucesso (sem retorno).")
            else:
                for row in result:
                    print(row)
        except Exception as e:
            print(f"❌ Erro: {e}")

# CLI
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI do Grafo Star Wars (Neo4j + Langchain)")
    subparsers = parser.add_subparsers(dest="comando")

    subparsers.add_parser("testar", help="Testar conexão com Neo4j")
    subparsers.add_parser("schema", help="Mostrar o schema do banco")

    parser_perguntar = subparsers.add_parser("perguntar", help="Fazer uma pergunta à LLM com base no grafo")
    parser_perguntar.add_argument("texto", type=str, help="Texto da pergunta")

    parser_cypher = subparsers.add_parser("cypher", help="Executar um comando Cypher único")
    parser_cypher.add_argument("query", type=str, help="Cypher a ser executado (entre aspas)")

    subparsers.add_parser("cypher-shell", help="Abrir modo interativo Cypher")

    args = parser.parse_args()

    if args.comando == "testar":
        testar_conexao()
    elif args.comando == "schema":
        mostrar_schema()
    elif args.comando == "perguntar":
        perguntar_llm(args.texto)
    elif args.comando == "cypher":
        executar_cypher_unico(args.query)
    elif args.comando == "cypher-shell":
        executar_cypher_interativo()
    else:
        parser.print_help()