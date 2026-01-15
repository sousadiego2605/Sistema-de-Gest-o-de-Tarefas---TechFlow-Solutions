import sys
import os

# Adiciona a pasta raiz ao caminho do Python para ele achar o 'src'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.main import criar_tarefa, deletar_tarefa

def test_criar_tarefa_com_prioridade():
    tarefa = criar_tarefa(1, "Entrega Urgente", "Alta")
    assert tarefa['prioridade'] == "Alta"
    assert tarefa['titulo'] == "Entrega Urgente"

def test_deletar_tarefa():
    tarefas = [{'id': 1, 'titulo': 'Teste'}]
    resultado = deletar_tarefa(tarefas, 1)
    assert resultado == True
    assert len(tarefas) == 0