# Teste unitário simples usando PyTest
def test_criar_tarefa():
    tarefa = {"titulo": "Entrega Expressa", "status": "Pendente"}
    # Simula a verificação se o título não está vazio
    assert len(tarefa["titulo"]) > 0 
    assert tarefa["status"] == "Pendente"
    