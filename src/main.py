def criar_tarefa(id, titulo, prioridade="Baixa"):
    return {"id": id, "titulo": titulo, "prioridade": prioridade, "status": "Pendente"}

# Simulação de uso
def deletar_tarefa(tarefas, id_tarefa):
    for tarefa in tarefas:
        if tarefa.get('id') == id_tarefa:
            tarefas.remove(tarefa)
            return True
    return False

print("Sistema TechFlow Iniciado")
tarefa1 = criar_tarefa(1, "Entrega Logística")
lista = [tarefa1]
print(lista)