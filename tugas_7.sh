#!/bin/bash
 
luas(){
panjang=$1
lebar=$2
luas=$(($1*$2))
echo "luas persegi: "
echo $luas
}

echo "masukkan panjang: "
read panjang 
echo "masukkan lebar: "
read lebar
luas $panjang $lebar
