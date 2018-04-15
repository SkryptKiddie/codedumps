#!/bin/bash
mkdir minecraft
cd minecraft
wget -O minecraft_server.jar https://s3.amazonaws.com/Minecraft.Download/versions/1.12.2/minecraft_server.1.12.2.jar
java -Xmx1024M -Xms1024M -jar minecraft_server.jar nogui
sudo rm -rf eula.txt
echo "eula=true" > myfile.txt
echo "Installed and ready!"
