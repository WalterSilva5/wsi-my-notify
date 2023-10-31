# wsi-my-notify
<span style="color:red;">
   <strong>Atenção!</strong> este é um README inicial, feito com báse no que está sendo utilizado atualmente, quando o projeto for refatorado para um formato generico esse documento deve ser alterado para refletir a forma correata de utilização, sem caminhos realcionados a maquina do desenvolvedor.
</span >

esse projeto tem como objetivo criar notificações em certos periodos de tempo para o usuário.
as notificações podem ser agendadas para serem enviadas em um determinado horário ou em um determinado intervalo de tempo.

o arquivo main.py é o agendador de notificações, ele é responsável por ler o arquivo de configuração e agendar as notificações.

o arquivo manager.py é o responsável por gerenciar as notificações, ele é responsável por modificar o arquio schedule_events.json, que é o arquivo que contém as notificações agendadas.

o arquivo schedule_events.json deve estar dentro do diretorio /home/seu_usuario/.my-notify/schedule_events.json

é possivel fazer build da aplicação executando o comando pyinstaller main.spec, o executável será gerado na pasta dist.

Executando automaticamente o arquivo compilado:

Para executar um programa automaticamente ao iniciar o sistema Manjaro com linux, você pode seguir estas etapas:

1. **Criar um arquivo `.desktop`**:

   Primeiro, crie um arquivo `.desktop` para o seu aplicativo. Vamos chamá-lo de `wsi-notify.desktop`:

   ```bash
   nano ~/.config/autostart/wsi-notify.desktop
   ```

   Cole o seguinte conteúdo, ajustando para o seu caso:

   ```
   [Desktop Entry]
   Type=Application
   Exec=/home/seu_usuario/.my-notify/main
   Hidden=false
   NoDisplay=false
   X-GNOME-Autostart-enabled=true
   Name=Wsi my Notify
   Comment=Wsi My Notify
   ```

   Salve o arquivo e saia do editor (Ctrl + O, Enter, Ctrl + X no nano).

2. **Torne o arquivo executável**:

   ```bash
   chmod +x ~/.config/autostart/wsi-notify.desktop
   ```

3. **Reinicie o sistema**:

   Depois de reiniciar, seu programa será executado automaticamente ao iniciar o linux.

Observação: Certifique-se de que o caminho `/home/wsi/repositorios/GitHub/main` tem permissões de execução. Se não tiver, você pode adicionar permissões de execução com o comando:

```bash
chmod +x /home/wsi/repositorios/GitHub/main
```

Agora, sempre que você iniciar o linux, o seu programa será executado automaticamente. Se em algum momento você quiser desativar essa inicialização automática, basta deletar o arquivo `wsi-notify.desktop` da pasta `~/.config/autostart/`.