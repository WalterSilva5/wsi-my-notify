# wsi-my-notify

esse projeto tem como objetivo criar notificações em certos periodos de tempo para o usuário.
as notificações podem ser agendadas para serem enviadas em um determinado horário ou em um determinado intervalo de tempo.

o arquivo main.py é o agendador de notificações, ele é responsável por ler o arquivo de configuração e agendar as notificações.

o arquivo manager.py é o responsável por gerenciar as notificações, ele é responsável por modificar o arquio schedule_events.json, que é o arquivo que contém as notificações agendadas.

o arquivo schedule_events.json deve estar dentro do diretorio /home/seu_usuario/.my-notify/schedule_events.json

é possivel fazer build da aplicação executando o comando pyinstaller main.spec, o executável será gerado na pasta dist.