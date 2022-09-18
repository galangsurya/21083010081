#!/bin/bash
echo -n "berapa tinggi badanmu?"
read tinggi

if (( tinggi <= 140 )); then
  echo "maaf tinggi mu tidak sesuai kriteria"
elif (( tinggi <= 170 )); then
  echo "yeay tinggi mu sesuai kriteria"
else
  echo "maaf tinggi kamu melebihi kriteria:((("
fi
