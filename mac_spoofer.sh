#!/bin/bash
# Joshek's MAC (and IP on DCHP) changer/spoofer/generator
IFACE="wlo1" ## input network interface here
echo -e "\e[96mOld MAC address"
ifconfig $IFACE | grep ether
ifconfig $IFACE | grep inet
echo
echo -e "\e[91mStopping service" ## kill the NetworkManager.service
sudo systemctl stop NetworkManager.service
sudo ifconfig $IFACE down 
echo Stopped service
hexchars="0123456789ABCDEF" ## generate new mac address
end=$( for i in {1..10} ; do echo -n ${hexchars:$(( $RANDOM % 16 )):1} ; done | sed -e 's/\(..\)/:\1/g' )
MAC=00$end
echo -e "\e[93mSetting new MAC address"
sudo ifconfig $IFACE hw ether $MAC ## change cloned MAC
echo -e "\e[92mDone, bringing $IFACE back online"
sudo ifconfig $IFACE up ## start NetworkManager.service
sudo systemctl start NetworkManager.service
echo Service started, MAC address changed
echo
echo -e "\e[96mNew MAC address"
ifconfig $IFACE | grep ether
## ifconfig $IFACE | grep inet ## not needed bc you won't be connected that quickly
