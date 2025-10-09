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
    
    #🔢 Solicita ao usuário uma opção numérica do menu
def getEscolhaDoUsuario():
    try:
        return int(input("Escolha uma opção"))
    except ValueError:
        return -1
    
def filtrarEventosPorCategoria(lista, categoria):
    #Retorna uma lista contendo apenas os eventos cuja categoria (ignorando maiúsculas e minúsculas) corresponde à categoria fornecida. Usa compreensão de lista para filtrar de forma eficiente.
    return [ e for e in lista if e.get('categoria', '').lower() == categoria.lower()]

def marcarEventoAtendido(lista, id):
    # Percorre a lista de eventos e marca como atendido o evento que possui o ID correspondente.
    # Retorno True se o evento foi encontrado e marcado; caso contrário, retorne False.
    for e in lista:
        if e.get("id") == id:
            e["atendido"] = True
            return True
    return False

def gerarRelatorio(lista):
    # :bar_chart: Gera e imprime um relatório estatistico com base na lista de eventos.
    # :white_check_mark:  Calcula o total de eventos, quantos foram atendidos, a porcentagem de participação.
    # :card_index_dividers: Agrupa os eventos por categoria e exibe os dados formatados no console.

 def gerarRelatorio(lista):
    total = len(lista)
    atendido = sum(1 for e in lista if e.get('atendido'))

    por_categoria = {}
    for e in lista:
        cat = e.get('categoria', 'Outros')
        por_categoria[cat] = por_categoria.get(cat, 0) + 1

        pctParticipados = (atendido / total * 100) if total > 0 else 0

        print("=== Relatório de Eventos ===")
        print(f"Total de eventos: {total}")
        print(f"Participados: {atendido}")
        print(f"Participação: {pctParticipados:.2f}%")
        print("Eventos por categoria:")
        for cat, count in por_categoria.items():
            print(f" - {cat}: {count}")
            print("---------------------------")

def adicionarEventoEstudanteA(lista):
    # 📝 Solicita ao usuário os dados de um novo evento (titulo, categoria e data).
    # 🆔 Gera um ID único usando a variável global 'proximo_id' e adiciona o evento à lista.
    # ✅ Exibe uma mensagem de confirmação. e incrementa o ID para o próximo evento.
    global proximo_id
    titulo = input("Titulo do evento:").strip()
    categoria = input("Categoria (Acadêmico, Social, Esportes):").strip()
    data = input("Data (AAAA-MM-DD):").strip()
    novo = {"id": proximo_id, "titulo": titulo, "categoria": categoria, "data": data, "atendido": False}
    lista.append(novo)
    print(f"Evento '{titulo}' adicionado com sucesso com ID {proximo_id}.")
    proximo_id += 1
    

# EstudanteB
listarEventos = []
proximo_id = 1

def displayMenu():
    print("\n=== Menu ===")
    print("1 - Adicionar evento (Estudante A)")
    print("2 - Visualizar todos os eventos")
    print("3 - Filtrar eventos por categoria")
    print("4 - Marcar eventos como participado")
    print("5 - Gerar relatório")
    print("0 - Sair")

# 🔢 Solicita ao usuário uma opção numérica do menu
def getEscolhaDoUsuario():
    try:
        return int(input("Escolha uma opção: "))
    except ValueError:
        return -1

def filtrarEventosPorCategoria(lista, categoria):
    # 🔍 Retorna uma lista contendo apenas os eventos cuja categoria (ignorando maiúsculas e minúsculas) corresponde à fornecida.
    return [e for e in lista if e.get('categoria', '').lower() == categoria.lower()]

def marcarEventoAtendido(lista, id):
    # ✅ Marca como atendido o evento que possui o ID correspondente.
    for e in lista:
        if e.get("id") == id:
            e["atendido"] = True
            return True
    return False

def gerarRelatorio(lista):
    # 📊 Gera e imprime um relatório estatístico com base na lista de eventos.
    # ✅ Calcula o total de eventos, quantos foram atendidos e a porcentagem de participação.
    # 🗂️ Agrupa os eventos por categoria e exibe os dados formatados no console.
    total = len(lista)
    atendido = sum(1 for e in lista if e.get('atendido'))

    por_categoria = {}
    for e in lista:
        cat = e.get('categoria', 'Outros')
        por_categoria[cat] = por_categoria.get(cat, 0) + 1

    pctParticipados = (atendido / total * 100) if total > 0 else 0

    print("=== Relatório de Eventos ===")
    print(f"Total de eventos: {total}")
    print(f"Participados: {atendido}")
    print(f"Participação: {pctParticipados:.2f}%")
    print("Eventos por categoria:")
    for cat, count in por_categoria.items():
        print(f" - {cat}: {count}")
    print("---------------------------")

def adicionarEventoEstudanteA(lista):
    # 📝 Solicita ao usuário os dados de um novo evento (título, categoria e data).
    # 🆔 Gera um ID único usando a variável global 'proximo_id' e adiciona o evento à lista.
    # ✅ Exibe uma mensagem de confirmação e incrementa o ID para o próximo evento.
    global proximo_id
    titulo = input("Título do evento: ").strip()
    categoria = input("Categoria (Acadêmico, Social, Esportes): ").strip()
    data = input("Data (AAAA-MM-DD): ").strip()
    novo = {
        "id": proximo_id,
        "titulo": titulo,
        "categoria": categoria,
        "data": data,
        "atendido": False
    }
    lista.append(novo)
    print(f"Evento '{titulo}' adicionado com sucesso com ID {proximo_id}.")
    proximo_id += 1
# EstudanteB
listarEventos = []
proximo_id = 1

def displayMenu():
    print("\n=== Menu ===")
    print("1 - Adicionar evento (Estudante A)")
    print("2 - Visualizar todos os eventos")
    print("3 - Filtrar eventos por categoria")
    print("4 - Marcar eventos como participado")
    print("5 - Gerar relatório")
    print("0 - Sair")

# 🔢 Solicita ao usuário uma opção numérica do menu
def getEscolhaDoUsuario():
    try:
        return int(input("Escolha uma opção: "))
    except ValueError:
        return -1

def filtrarEventosPorCategoria(lista, categoria):
    # 🔍 Retorna eventos cuja categoria corresponde à fornecida (ignorando maiúsculas/minúsculas)
    return [e for e in lista if e.get('categoria', '').lower() == categoria.lower()]

def marcarEventoAtendido(lista, id):
    # ✅ Marca como atendido o evento com o ID correspondente
    for e in lista:
        if e.get("id") == id:
            e["atendido"] = True
            return True
    return False

def gerarRelatorio(lista):
    # 📊 Gera e imprime relatório com estatísticas dos eventos
    # 🗂️ Agrupa por categoria e calcula participação
    total = len(lista)
    atendido = sum(1 for e in lista if e.get('atendido'))

    por_categoria = {}
    for e in lista:
        cat = e.get('categoria', 'Outros')
        por_categoria[cat] = por_categoria.get(cat, 0) + 1

    pctParticipados = (atendido / total * 100) if total > 0 else 0

    print("=== Relatório de Eventos ===")
    print(f"Total de eventos: {total}")
    print(f"Participados: {atendido}")
    print(f"Participação: {pctParticipados:.2f}%")
    print("Eventos por categoria:")
    for cat, count in por_categoria.items():
        print(f" - {cat}: {count}")
    print("---------------------------")

def adicionarEventoEstudanteA(lista):
    # 📝 Solicita dados de um novo evento
    # 🆔 Gera ID único e adiciona à lista
    # ✅ Exibe confirmação e incrementa o ID
    global proximo_id
    titulo = input("Título do evento: ").strip()
    categoria = input("Categoria (Acadêmico, Social, Esportes): ").strip()
    data = input("Data (AAAA-MM-DD): ").strip()
    novo = {
        "id": proximo_id,
        "titulo": titulo,
        "categoria": categoria,
        "data": data,
        "atendido": False
    }
    lista.append(novo)
    print(f"Evento '{titulo}' adicionado com sucesso com ID {proximo_id}.")
    proximo_id += 1

# EstudanteB
listaEventos = []
proximo_id = 1

# 📋 Exibe o menu de opções para o usuário
def displayMenu():
    print("\n=== Menu ===")
    print("1 - Adicionar evento (Estudante A)")
    print("2 - Visualizar todos os eventos")
    print("3 - Filtrar eventos por categoria")
    print("4 - Marcar eventos como participado")
    print("5 - Gerar relatório")
    print("0 - Sair")

# 🔢 Solicita ao usuário uma opção numérica do menu
def getEscolhaDoUsuario():
    try:
        return int(input("Escolha uma opção: "))
    except ValueError:
        return -1

# 🔍 Filtra eventos por categoria (ignora maiúsculas/minúsculas)
def filtrarEventosPorCategoria(lista, categoria):
    return [e for e in lista if e.get('categoria', '').lower() == categoria.lower()]

# ✅ Marca como atendido o evento com o ID correspondente
def marcarEventoAtendido(lista, id):
    for e in lista:
        if e.get("id") == id:
            e["atendido"] = True
            return True
    return False

# 📊 Gera e imprime relatório com estatísticas dos eventos
def gerarRelatorio(lista):
    total = len(lista)
    atendido = sum(1 for e in lista if e.get('atendido'))

    por_categoria = {}
    for e in lista:
        cat = e.get('categoria', 'Outros')
        por_categoria[cat] = por_categoria.get(cat, 0) + 1

    pctParticipados = (atendido / total * 100) if total > 0 else 0

    print("=== Relatório de Eventos ===")
    print(f"Total de eventos: {total}")
    print(f"Participados: {atendido}")
    print(f"Participação: {pctParticipados:.2f}%")
    print("Eventos por categoria:")
    for cat, count in por_categoria.items():
        print(f" - {cat}: {count}")
    print("---------------------------")

# 📝 Adiciona novo evento com dados fornecidos pelo usuário
def adicionarEventoEstudanteA(lista):
    global proximo_id
    titulo = input("Título do evento: ").strip()
    categoria = input("Categoria (Acadêmico, Social, Esportes): ").strip()
    data = input("Data (AAAA-MM-DD): ").strip()
    novo = {
        "id": proximo_id,
        "titulo": titulo,
        "categoria": categoria,
        "data": data,
        "atendido": False
    }
    lista.append(novo)
    print(f"Evento '{titulo}' adicionado com sucesso com ID {proximo_id}.")
    proximo_id += 1
