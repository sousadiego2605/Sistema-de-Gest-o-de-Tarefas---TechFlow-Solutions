from src.main import deletar_tarefa, criar_tarefa

def test_criar_tarefa():
    # Usa a função real do sistema para criar a tarefa
    tarefa = criar_tarefa(1, "Entrega Expressa")
    assert tarefa['titulo'] == "Entrega Expressa"
    assert tarefa['status'] == "Pendente"

def test_deletar_tarefa():
    # Cria uma lista simulada
    tarefas = [{'id': 1, 'titulo': 'Teste'}]
    
    # Tenta deletar a tarefa de ID 1
    resultado = deletar_tarefa(tarefas, 1)
    
    # Verifica se funcionou
    assert resultado == True
    assert len(tarefas) == 0