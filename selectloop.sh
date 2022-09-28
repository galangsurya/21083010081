#!/bin/bash

select makanan in pentol sempol cimol poki seblak semua gaada
do
 case $makanan in
   pentol|sempol|cimol|semua)
     echo "habis, bang"
     ;;
   poki|seblak)
     echo "ready, ngab"
    ;;
   gaada)
         break
       ;;
     *) echo "gaada di menu bang"
 esac
done
