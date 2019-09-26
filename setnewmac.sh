#!/bin/bash
IFACE="wlo1" ## input network interface here
echo "Set custom MAC Address"
echo -e "\e[96mOld MAC address"
ifconfig $IFACE | grep ether
ifconfig $IFACE | grep inet
echo -e "\e[39m" #newline and color change
read -p "Set new MAC address? (Y/n): " -n 1 -r
if [[ $REPLY =~ ^[Yy]$ ]]
then
    echo #newline
    echo -e "\e[49mLet's get this bread"
    echo -e "\e[91mStopping $IFACE interface and NetworkManager" ## kill the NetworkManager.service
    sudo systemctl stop NetworkManager.service
    sudo ifconfig $IFACE down 
    echo "Stopped service and interface!"
    read -p "Input new MAC Address (xx:xx:xx:xx:xx:xx): " -r
    echo -e "\e[93mSetting new MAC address"
    sudo ifconfig $IFACE hw ether $REPLY ## change cloned MAC
    echo "Done, bringing $IFACE back online"
    sudo ifconfig $IFACE up ## start NetworkManager.service
    sudo systemctl start NetworkManager.service
    echo -e "\e[92mDone$IFACE back up, MAC address changed"
    echo #newline
    echo -e "\e[96mNew MAC address"
    ifconfig $IFACE | grep ether
    ## ifconfig $IFACE | grep inet ## not needed bc you won't be connected that quickly
fi
    echo #newline
