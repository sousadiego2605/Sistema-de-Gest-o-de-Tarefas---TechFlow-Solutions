def criar_tarefa(titulo, status="Pendente"):
    if not titulo:
        return "Erro: Título vazio"
    return {"titulo": titulo, "status": status}

# Simulação de uso
tarefa1 = criar_tarefa("Entrega Logística Expressa")
print(tarefa1)
print("Sistema TechFlow Iniciado")
