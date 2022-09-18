#!/bin/bash

#deklarasi array
distroLinux=("linux" "windows" "mac" "ubuntu")

#random distro
let pilih=$RANDOM%5

#eksekusi
echo "saya memilih distro $pilih, ${distroLinux[$pilih]}!"
