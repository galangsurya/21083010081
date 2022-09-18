#!/bin/bash

#inisialisasi var
a=55;
b=7;
distrolinux="Ubuntu 19.04 LTS"
let c=a%b;

#output printF
printf "OS : $distrolinux \n";
printf "$c \n";
printf "%.2f float \n" $a;
printf "%.1f float \n" $a;
