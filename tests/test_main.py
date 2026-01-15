from src.main import criar_tarefa # Garanta que esta linha está no topo

def test_criar_tarefa_com_prioridade():
    tarefa = criar_tarefa(1, "Entrega Urgente", "Alta")
    assert tarefa['prioridade'] == "Alta"

def test_deletar_tarefa():
    # Cria uma lista simulada
    tarefas = [{'id': 1, 'titulo': 'Teste'}]
    
    # Tenta deletar a tarefa de ID 1
    resultado = deletar_tarefa(tarefas, 1)
    
    # Verifica se funcionou
    assert resultado == True
    assert len(tarefas) == 0