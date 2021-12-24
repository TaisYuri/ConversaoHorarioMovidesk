# ConversaoHorarioMovidesk
Projeto desenvolvido em Python 3 para automatização de tarefas.

No cenário, um programa chamado Movidesk emitia um relatório onde era possivel obter o nome do usuário, data e hora em que logou ou deslogou.
Era necessário montar diariamente o registro de ponto em cima deste relatório, então precisaria extrair o nome do usuário e todas as suas entradas e saídas para computar em apenas uma linha o registro do dia.

Este programa lê o arquivo em CSV emitido pelo programa, identifica o nome do usuário configurado no arquivo SUPORTE.TXT e através dele separa os registros de ponto de acordo com o dia.
Ao final do processo, é emitindo um arquivo XLSX.

Observações:
- A pasta onde o arquivo é lido e depois salvo fica em C:/Relatorios-horarios/
- O arquivo para leitura precisa estar no formado CSV
- O arquivo para saída será em XLSX.
- O arquivo SUPORTE.TXT deverá estar salvo na mesma pasta e com os devidos usúarios configurados.
