mkdir -p ~/.config/autostart
cat <<EOL > ~/.config/autostart/wsi-notify.desktop
[Desktop Entry]
Type=Application
Exec=/home/wsi/.my-notify/main
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=Wsi my Notify
Comment=Wsi My Notify
EOL