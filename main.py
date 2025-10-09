from datetime import datetime

# função para validar data
def validarData(data_str):
    try:
        datetime.strptime(data_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False
    
count = 0

# função para adicionar evento
def adicionarEvento(listaEvento, nome, data, local, categoria):
    global count

    if not nome or not data or not local or not categoria:
        print("Erro: Todos os campos são obrigatórios.")
        return
    
    if not validarData(data):
        print("Erro: Data inválida. Use o formato AAAA-MM-DD.")
        return
    
    count += 1
    # novo_id = len(listaEvento) + 1
    novoEvento = {
        "id": count,
        "nome": nome,
        "data": data,
        "local": local,
        "categoria": categoria,
        "participado": False    
    }
    listaEvento.append(novoEvento)
    print("Evento adicionado com sucesso!")

# listaEventos = [
#     {"id": 1, "nome": "Hackathon", "data": "2025-05-20", "local": "Hall", "categoria": "Social", "participado": False},
#     {"id": 2, "nome": "Palestra Python", "data": "2025-05-21", "local": "Sala 101", "categoria": "Acadêmico", "participado": True}
# ]

# função para listar os eventos
def listarEventos(listaEvento):
    if not listaEvento:
        print("Nenhum evento cadastrado.")
        return
    for evento in listaEvento:
        if evento["participado"] == True:
            status = "Sim"
        else:
            status = "Não"

        print(f"ID: {evento['id']}, Nome: {evento['nome']}, Data: {evento['data']}, "
              f"Local: {evento['local']}, Categoria: {evento['categoria']}, "
              f"Participado: {status}")
        
# listarEventos(listaEventos)

# função para procurar evento por nome ou categoria
def procurarEventoPorNome(listaEvento, filtro):
    resultados = []
    for evento in listaEvento:
        if filtro.lower() in evento["nome"].lower() or filtro.lower() in evento["categoria"].lower():
            resultados.append(evento)
    
    if not resultados:
        print("Nenhum evento encontrado.")
        return [] # Retorna lista vazia se nada for encontrado
        
    return resultados 

# print(procurarEventoPorNome(listaEventos, "Hackathon"))  
# print(procurarEventoPorNome(listaEventos, "Acadêmico"))  
# print(procurarEventoPorNome(listaEventos, "Eventox")) 

# função para deletar evento
def deletarEvento(listaEvento, id):
    for i, evento in enumerate(listaEvento):
        if evento["id"] == id:
            listaEvento.pop(i)
            print("Evento deletado com sucesso!")
            return
    print("Evento não encontrado.")
    
# deletarEvento(listaEventos, 1)
# listarEventos(listaEventos)


# # Teste
# eventos = []
# adicionarEvento(eventos, "Evento 1", "2024-12-01", "Local A", "Categoria X")
# adicionarEvento(eventos, "Evento 2", "2024-12-02", "Local B", "Categoria Y")

# # Deletar um evento
# deletarEvento(eventos, 1)

# # Adicionar novo - ID deve ser 3, não 2
# adicionarEvento(eventos, "Evento 3", "2024-12-03", "Local C", "Categoria Z")

# listarEventos(eventos)
# # Deve mostrar: ID 2 e ID 3 (não ID 1 e 2)


# ============================================================
# Gerenciador de Eventos - Projeto Acadêmico
# Autor: estudanteB-feature
# Descrição:
# Este sistema permite o gerenciamento de eventos para estudantes.
# Funcionalidades incluem:
# - Adição de eventos (Estudante A)
# - Visualização de todos os eventos
# - Filtragem por categoria
# - Marcação de eventos como participados
# - Geração de relatório estatístico
# ============================================================

# Lista que armazenará todos os eventos cadastrados
listaEventos = []

# Variável global para controle incremental de IDs dos eventos
proximo_id = 1

# Função que exibe o menu principal com as opções disponíveis
def displayMenu():
    print("\n=== Menu ===")
    print("1 - Adicionar evento (Estudante A)")
    print("2 - Visualizar todos os eventos")
    print("3 - Filtrar eventos por categoria")
    print("4 - Marcar evento como participado")
    print("5 - Gerar relatório")
    print("0 - Sair")

# Função que captura a escolha do usuário e trata erros de entrada
def getEscolhaDoUsuario():
    try:
        return int(input("Escolha uma opção: "))
    except ValueError:
        return -1  # Retorna -1 em caso de entrada inválida

# Função que filtra eventos por categoria informada
def filtrarEventosPorCategoria(lista, categoria):
    return [e for e in lista if e.get('categoria', '').lower() == categoria.lower()]

# Função que marca um evento como participado com base no ID
def marcarEventoAtendido(lista, id):
    for e in lista:
        if e.get('id') == id:
            e['atendido'] = True
            return True  # Evento encontrado e marcado
    return False  # Evento não encontrado

# Função que gera um relatório com estatísticas dos eventos
def gerarRelatorio(lista):
    total = len(lista)
    atendidos = sum(1 for e in lista if e.get('atendido'))

    por_categoria = {}
    for e in lista:
        cat = e.get('categoria', 'Outro')
        por_categoria[cat] = por_categoria.get(cat, 0) + 1

    pctParticipados = (atendidos / total * 100) if total > 0 else 0.0

    print("---- Relatório ----")
    print(f"Total de eventos: {total}")
    print(f"Participados: {atendidos}")
    print(f"Participação: {pctParticipados:.2f}%")
    print("Eventos por categoria:")
    for cat, count in por_categoria.items():
        print(f" - {cat}: {count}")
    print("-------------------")

# Função que adiciona um novo evento para o perfil Estudante A
def adicionarEventoEstudanteA(lista):
    global proximo_id
    titulo = input("Título do evento: ").strip()
    categoria = input("Categoria (Acadêmico, Social, Esportes): ").strip()
    data = input("Data (YYYY-MM-DD): ").strip()
    novo = {
        "id": proximo_id,
        "titulo": titulo,
        "categoria": categoria,
        "data": data,
        "atendido": False
    }
    lista.append(novo)
    print(f"Evento adicionado com sucesso. ID: {proximo_id}")
    proximo_id += 1

# Função principal que controla o fluxo do programa
def main():
    print("Bem-vindo ao Gerenciador de Eventos (Python)")
    while True:
        displayMenu()
        escolha = getEscolhaDoUsuario()

        if escolha == 1:
            adicionarEventoEstudanteA(listaEventos)

        elif escolha == 2:
            if not listaEventos:
                print("Nenhum evento cadastrado.")
            else:
                print("--- Lista de Eventos ---")
                for e in listaEventos:
                    print(f"ID:{e['id']} | {e['titulo']} | {e['categoria']} | {e['data']} | Participado: {'Sim' if e['atendido'] else 'Não'}")

        elif escolha == 3:
            cat = input("Informe a categoria para filtragem: ").strip()
            filtrados = filtrarEventosPorCategoria(listaEventos, cat)
            if not filtrados:
                print("Nenhum evento encontrado nessa categoria.")
            else:
                print("Eventos filtrados:")
                for e in filtrados:
                    print(f"ID:{e['id']} | {e['titulo']} | {e['categoria']} | {e['data']} | Participado: {'Sim' if e['atendido'] else 'Não'}")

        elif escolha == 4:
            id_str = input("Informe o ID do evento para marcar como participado: ").strip()
            try:
                id_num = int(id_str)
                if marcarEventoAtendido(listaEventos, id_num):
                    print("Evento marcado como participado com sucesso.")
                else:
                    print("Evento não encontrado.")
            except ValueError:
                print("ID inválido. Por favor, insira um número.")

        elif escolha == 5:
            gerarRelatorio(listaEventos)

        elif escolha == 0:
            print("Encerrando o programa. Até a próxima!")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Execução do programa
if __name__ == "__main__":
    main()

# ============================================================
# Fim do código - Gerenciador de Eventos
# ============================================================