## change wlo1 to your appropriate interface
#!/bin/bash
echo Old MAC
cat /sys/class/net/wlo1/address
echo Stopping NetworkManager.service
sudo systemctl stop NetworkManager.service
echo Stopped service
sudo ifconfig wlo1 down
hexchars="0123456789ABCDEF"
end=$( for i in {1..10} ; do echo -n ${hexchars:$(( $RANDOM % 16 )):1} ; done | sed -e 's/\(..\)/:\1/g' )
MAC=00$end
echo Setting new cloned MAC address
sudo ifconfig wlo1 hw ether $MAC
echo Done, bringing interface back online
sudo ifconfig wlo1 up
sudo systemctl start NetworkManager.service
echo Service started, MAC changed
echo New MAC
cat /sys/class/net/wlo1/address
