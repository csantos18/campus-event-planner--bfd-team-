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

# EstudandeB
listarEventos = []
proximo_id = 1

def displayMenu ():
    print("\n=== Menu ===")
    print("1 - Adicionar evento (Estdante A)")
    print("2 - Visualizar todos os eventos")
    print("3 - Filtra eventos por categoria")
    print("4 - Marca eventos como participado")
    print("5 - Gerar relatório")
    print("0 - Sair")
    