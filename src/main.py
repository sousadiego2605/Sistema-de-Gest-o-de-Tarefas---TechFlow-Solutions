def criar_tarefa(id, titulo, status="Pendente"):
    if not titulo:
        return "Erro: Título vazio"
    return {"id": id, "titulo": titulo, "status": status}

def deletar_tarefa(tarefas, id_tarefa):
    for tarefa in tarefas:
        if tarefa.get('id') == id_tarefa:
            tarefas.remove(tarefa)
            return True
    return False

# Simulação de uso

print("Sistema TechFlow Iniciado")
tarefa1 = criar_tarefa(1, "Entrega Logística")
lista = [tarefa1]
print(lista)