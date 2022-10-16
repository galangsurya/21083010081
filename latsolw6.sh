#!/bin/bash
echo "masukkan nama : "
a=0
read input
echo "masukkan nilai:"
read -a angka
t=0
for i in ${angka[@]}
do
    let t+=$i
done 

p=${#angka[@]}

echo "ips mahasiswa = $t  / $p"
echo "ipk mahasiswa = $((t / p))"
