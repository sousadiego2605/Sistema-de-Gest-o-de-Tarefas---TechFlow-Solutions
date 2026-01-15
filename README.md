TechFlow Task Manager – Gerenciamento Ágil para Logística
1. Descrição do Projeto
Este sistema foi desenvolvido para a TechFlow Solutions com o objetivo de atender uma startup de logística que necessita monitorar seu fluxo de trabalho em tempo real. A ferramenta foca na priorização de tarefas críticas e monitoramento de desempenho através de uma interface funcional e intuitiva.


2. Escopo do Projeto
O sistema consiste em um CRUD básico para gerenciamento de demandas logísticas:



Create: Registro de novas tarefas.


Read: Listagem de atividades pendentes e concluídas.


Update: Alteração de detalhes ou status da tarefa.


Delete: Remoção de registros conforme necessidade.

3. Metodologia Ágil
Utilizamos a metodologia ágil com foco em entregas iterativas:



Kanban: Gestão visual realizada através da aba Projects do GitHub, com as colunas A Fazer, Em Progresso e Concluído.



Versionamento: Histórico de no mínimo 10 commits semânticos para rastreabilidade das alterações.


4. Controle de Qualidade (CI/CD)
Para garantir a confiabilidade do software, configuramos um pipeline de integração contínua (CI):



Ferramenta: GitHub Actions.



Testes: Execução automatizada de testes unitários para validação de entradas de dados em cada commit.


5. Como Executar o Projeto
Clone este repositório: git clone [URL-DO-REPOSITORIO].

Certifique-se de ter o ambiente da linguagem escolhida instalado (Python/Node.js).

Instale as dependências necessárias.

Execute o sistema principal na pasta /src.

Para rodar os testes, utilize o comando específico do framework (ex: pytest ou npm test).

6. Gestão de Mudanças (Simulação de Escopo)

Alteração: Adição de campo de "Nível de Prioridade" (Baixa, Média, Alta) e "Data Limite" para cada tarefa. Justificativa: Durante o ciclo de desenvolvimento, a startup de logística identificou que tarefas de entrega expressa precisavam de destaque visual no sistema para evitar atrasos críticos. Esta mudança foi registrada no Kanban e implementada no código.

## Gestão de Mudanças
"Durante o desenvolvimento, foi identificada a necessidade de classificar tarefas por urgência. Foi implementado o campo 'Prioridade' (Alta/Média/Baixa) na entidade Tarefa para atender a esse requisito logístico."
