#!/bin/bash
clear

token="23456";
read -sp "token : " word;
if [ $token == $word ]
then
    echo "Token Benar"
else
    echo "Token Salah"
fi
