#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def estimasi_func():
    jarak = input("masukkan jarak(km):")
    jarak = float(jarak) #casting string to float

    kecepatan = input("masukkan kecepatan(km/jam):")
    kecepatan = float(kecepatan) #casting string to float

    waktutempuh = jarak/kecepatan #menghitung waktu tempuh
    print("waktu tempuh: ", waktutempuh, "jam")

    waktu = waktutempuh * 60
    print("estimasi waktu tempuh dalam menit: ", waktu, "menit")


# In[ ]:


def estimasi_func():
    jarak = input("masukkan jarak(km):")
    jarak = float(jarak) #casting string to float

    kecepatan = input("masukkan kecepatan(km/jam):")
    kecepatan = float(kecepatan) #casting string to float

    waktutempuh = jarak/kecepatan #menghitung waktu tempuh
    print("waktu tempuh: ", waktutempuh, "jam")

    waktu = waktutempuh * 60
    print("estimasi waktu tempuh dalam menit: ", waktu, "menit")


# In[2]:


print ("====================================================================")
print ("|                                                                  |")
print ("         SELAMAT DATANG DI SISTEM ESTIMASI PERJALANAN               ")
print ("|                                                                  |")
print ("====================================================================")
nama = input("masukkan nama: ")
print ("========================= Destinasi ================================")
print ("jakarta")
print ("jogja")
print ("malang")
print ("bandung")
print ("custom")
kota = str(input("pilih destinasi(jakarta/jogja/malang/bandung/custom): " ))
if kota == "jakarta":
    if kota == "jakarta":
        print('----------------------kota asal------------------------')
        print("1. surabaya")
        print("2. sidoarjo")
        asal = input(" masukkan kota asal: ")
        if asal == "surabaya":
            print("jarak surabaya ke jakarta adalah 760 km")
            estimasi_func()
            print ("hati hati dijalan ya:)")
if kota == "jakarta":
        if asal == "sidoarjo":
            print("jarak sidoarjo ke jakarta adalah 752 km")
            estimasi_func()
            print ("hati hati dijalan ya:)")
if kota == "jogja":
    if kota == "jogja":
        print('----------------------kota asal------------------------')
        print("1. surabaya")
        print("2. sidoarjo")
        asal = input(" masukkan kota asal: ")
        if asal == "surabaya":
            print("jarak surabaya ke jogja adalah 335 km")
            estimasi_func()
            print ("hati hati dijalan ya:)")
if kota == "jogja":
        if asal == "sidoarjo":
            print("jarak sidoarjo ke jogja adalah 330 km")
            estimasi_func()
            print ("hati hati dijalan ya:)")
if kota == "malang":
    if kota == "malang":
        print('----------------------kota asal------------------------')
        print("1. surabaya")
        print("2. sidoarjo")
        asal = input(" masukkan kota asal: ")
        if asal == "surabaya":
            print("jarak surabaya ke malang adalah 80 km")
            estimasi_func()
            print ("hati hati dijalan ya:)")
if kota == "malang":
        if asal == "sidoarjo":
            print("jarak sidoarjo ke malang adalah 75 km")
            estimasi_func()
            print ("hati hati dijalan ya:)")
if kota == "bandung":
    if kota == "bandung":
        print('----------------------kota asal------------------------')
        print("1. surabaya")
        print("2. sidoarjo")
        asal = input(" masukkan kota asal: ")
        if asal == "surabaya":
            print("jarak surabaya ke bandung adalah 770 km")
            estimasi_func()
            print ("hati hati dijalan ya:)")
if kota == "bandung":
        if asal == "sidoarjo":
            print("jarak sidoarjo ke jogja adalah 765 km")
            estimasi_func()
            print ("estimasi diatas diluar dari kemacetan di jalan, hati hati dijalan ya:)")
if kota == "custom":
    jarak = input("masukkan jarak(km):")
    jarak = float(jarak) #casting string to float

    kecepatan = input("masukkan kecepatan(km/jam):")
    kecepatan = float(kecepatan) #casting string to float

    waktutempuh = jarak/kecepatan #menghitung waktu tempuh
    print("waktu tempuh: ", waktutempuh, "jam")

    waktu = waktutempuh * 60
    print("estimasi waktu tempuh dalam menit: ", waktu, "menit")


# In[ ]:





# In[ ]:




