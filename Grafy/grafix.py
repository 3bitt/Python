import sys
import os
import string
import collections

### Program pobiera ilosc wierzcholkow i krawedzi grafu
### i zwraca informacje takie jak:
#       1. Info o wierzcholkach
#       2. Spojnosc grafu
#       3. Sciezka Eulera
#       4. Dwudzielnosc grafu (kolory)

class W:     #-----------------------   Deklaracja klasy wierzcholkow
    nr = 0
    deg = int
    friends = list
    visited = 0
    def __init__(self, name, deg, friends, visited):
        self.name = name
        self.deg = deg
        self.friends = friends
        self.visited = visited
        self.color = 0
        self.__class__.nr += 1
        self.nr = self.__class__.nr



class Stack:
    def __init__(self):
        self.Stack = []
    def push(self, s):
        self.Stack.append(s)
    def pop(self):
        self.Stack.pop(len(self.Stack)-1)
    def size(self):
        return len(self.Stack)
    def top(self):
        return self.Stack[-1]


def mark(v):                # ------------ Funkcja oznaczajaca wierzcholek jako odwiedzony
    for i in range(0, rg):
        if Vertex[i].name == v and Vertex[i].visited is False:
            Vertex[i].visited = True
            Vertex[i].__class__.visited += 1
        else:
            pass

def kolej(element):      # ---------------- Funkcja sprawdzajaca spojnosc
    for i in range(0, len(Vertex)):
        if Vertex[i].name == element and Vertex[i].visited is False:
            Vertex[i].visited = True
            for k in Vertex[i].friends:
                kolejka.append(k)
            kolejka.pop(0)
            continue
        if Vertex[i].name == element and Vertex[i].visited == True:
            kolejka.pop(0)

def spr():                      # --------- Algorytm szukania sciezki Eulera
    for k in range(0, rg):
        if Vertex[k].name == stos.top() and Vertex[k].friends[0] in stos.Stack[::1]:
            Vertex[k].friends.remove(Vertex[k].friends[0])
            break
        elif Vertex[k].name == stos.top() and Vertex[k].friends[0] not in stos.Stack[::1]:
            stos.push(Vertex[k].friends[0])
            waste = Vertex[k].friends[0]
            mark(waste)
            Vertex[k].friends.remove(waste)
            break

def check_color2(v):            # Funkcja sprawdzajaca czy graf jest dwudzielny
    for gg in range(0, rg):
        if Vertex[gg].name == v:
            kolor = Vertex[gg].color
            for fr in Vertex[gg].friends:
                for ggg in range(0, rg):
                    if Vertex[ggg].name == fr:
                        kolor_friend = Vertex[ggg].color
                if kolor != kolor_friend:
                    pass
                elif kolor == kolor_friend:
                    global zapadka
                    zapadka += 1

def colors():         # ------------- Funkcja kolorujaca
    for k in kolejka2[0]:
        for w in range(0, rg):
            if Vertex[w].name == k and Vertex[w].color == 0:
                if stoss.top() == 1:
                    Vertex[w].color = 2
                elif stoss.top() == 2:
                    Vertex[w].color = 1
            elif Vertex[w].name == k and Vertex[w].color != 0:
                pass
        kolejka2.pop(0)

def show_colors():
    kolor1 = []
    kolor2 = []
    print 10 * '---'
    for pr in range(0, rg):
        if Vertex[pr].color == 1:
            kolor1.append(Vertex[pr].name)
        elif Vertex[pr].color == 2:
            kolor2.append(Vertex[pr].name)
    print 'Podzbior koloru 1:  %s' % kolor1
    print 'Podzbior koloru 2:  %s' % kolor2

def next_color():            #------------ Funkcja kolorujaca c.d
    if kolejka2 == [] and W.visited == rg:
        W.visited += 1
        for check in range(0, rg):
            check_color2(lista[check])
            if zapadka > 0:
                print 'Graf nie jest dwudzielny'
                break
            elif (check+1) == rg and zapadka == 0:
                print '\nGraf jest dwudzielny\n\n'
                show_colors()

    elif kolejka2 == [] and W.visited != rg:
        W.visited += 1
        for dod in range (0, rg):
            if Vertex[dod].visited is False and Vertex[dod].color != 0:
                for frie in Vertex[dod].friends:
                    kolejka2.append(frie)
                stoss.push(Vertex[dod].color)
                Vertex[dod].visited = True
                break

def dodaj(a, b):
    zbior[a-1].append(lista[b-1])       ### Funkcja tworzaca slownik
    zbior[b-1].append(lista[a-1])       ### (szkielet grafu)
    graf[a] = zbior[a-1]
    graf[b] = zbior[b-1]

zapadka = 0
Euler = bool
spojny = bool

### WPROWADZANIE WIERZCHOLKOW --- Filtrowanie wejscia ###

print('Witaj w programie \nProgram tworzy graf prosty i wypisuje info o stopniach \n')
V = input('Podaj liczbe wierzcholkow: ')
if V <= 0 or V == 1:
    while V <= 0:
        print('tylko liczby dodatnie, wieksze od zera')
        V = input('sprobuj jeszcze raz: ')
    while V == 1:
        V = input('minimum 2 wierzcholki \n'
                  'sprobuj jeszcze raz: ')

graf = {}
lista = []
zbior = []
for x in range(0, V):
    lista.append(string.uppercase[x:x+1])
    zbior.append([])
print(10*'-----')

### WPROWADZANIE KRAWEDZI --- Filtrowanie wejscia ###

edge = (V*(V-1)/2)
print 'Mam %d wierzcholkow' % V, 'co oznacza, ze moge przyjac maks %d krawedzi' % edge
E = input('Podaj liczbe krawedzi: ')
while E > edge:
    print 'za duzo krawedzi, nie zmieszcze tyle \n'
    E = input('sprobuj jeszcze raz: ')
while V == 2 and E > 1:
    print 'maks. 1 krawedz \n'
    E = input('sprobuj jeszcze raz: ')


for x in range(0, E):
    n = input('Numer wierzcholka poczatkowego: ')
    while n <= 0 or n > V:
        if n <= 0:
            print('ujemna nie zadziala')
        elif n > V:
            print('nie ma takiego wierzcholka (maks. %d )' % V)
        n = input('sprobuj jeszcze raz: ')


    m = input('Numer wierzcholka koncowego: ')
    while m <= 0 or m > V:
        if m <= 0:
            print('ujemna nie zadziala')
        elif m > V:
            print('nie ma takiego wierzcholka (maks. %d )' % V)
        m = input('sprobuj jeszcze raz: ')
    while n == m:
        m = input('nie robie petli, wybierz inny wierzcholek koncowy: ')
    while lista[m-1] in zbior[n-1][:]:
        print 'Te krawedzie sa juz polaczone \n'
        m = input('Wybierz inny koniec: ')
        while m == n:
            m = input('nie moge zapetlic, wybierz inny koniec: ')

    dodaj(n, m)
    print(20*'---')
    print graf
print(10*'-----')


p = zbior[:].__len__()
o = zbior[0].__len__()

for x in range(0, p):
    if o < (zbior[x].__len__()):
        o = zbior[x].__len__()
    else:
        continue
                    ### PODSUMOWANIE ###


print "\n\n\nLista sasiedztwa: \n\n"

if E > 10:
    str_format = '{:^15} {:^15} {:^70}'
else:
    str_format = '{:^15} {:^15} {:^35}'

print str_format.format("WIERZCHOLEK", "KRAWEDZIE", "DEG (V)")

for x in range(0, V):
    print str_format.format(lista[x], zbior[x], zbior[x].__len__())
    print 4*'--------------'
print "\n\nStopien grafu:   [ %d ]" % o
# ----------------------------------------------------------------------
Vertex = []
graf.keys().sort()

rg = len(graf.keys())    #---------------- Liczba wierzcholkow
for x in range(0, rg):   #---------------- Inicjalizacja objektow (Vertexow)
    name = lista[graf.keys()[x]-1]
    dg = len(graf.values()[x])
    fr = graf.values()[x]
    visited = False
    Vertex.append(W(name, dg, fr, visited))

#-------------------------- sprawdzenie czy graf jest Eulerowski -----
#par_count = 0
#for l in range(0, rg):
#    st_par = Vertex[l].deg % 2
#    if st_par == 0:
#        par_count += 1
#    if st_par != 0:
#        pass
#
#if par_count == rg:
#    print 'Graf jest grafem Eulerowskim'
#    Euler = True
#elif rg - par_count <= 2:
#    print 'Graf jest poleulerowski'
#    Euler = False
#else:
#    print 'Graf nie jest Eulerowski'
#    Euler = False

#--------------------Sprawdzenie czy graf jest spojny ----------------
kolejka = []
Vertex[0].visited = True
for k in Vertex[0].friends:
    kolejka.append(k)

while kolejka != []:
    elem = kolejka[0]
    kolej(elem)

count = 0
for k in range(0, rg):
    if Vertex[k].visited is True:
        count += 1
    else:
        pass
if count == rg:
    spojny = True
    print '\nGraf jest spojny\n'
else:
    spojny = False
    print '\nGraf nie jest spojny\n'


for revisit in range(0, rg):            # reset .visited
    Vertex[revisit].visited = False

# ------------------------------- Kolorowanie -------------------
#if spojny is True:
#    kolejka2 = []
#    stoss = Stack()
#    Vertex[0].color = 1
#    Vertex[0].visited = True
#    Vertex[0].__class__.visited += 1
#    for kk in Vertex[0].friends:
#        kolejka2.append(kk)
#    stoss.push(Vertex[0].color)
#
#    while rg != (W.visited-1):
#        colors()
#        next_color()
#
#    #  Sprawdzenie czy graf jest dwudzielny ---------
#    # --- przeniesienie funkcji do next_color()
#
#print 10 *'---', '\n'
#
#W.visited = 0

# ---------------------- Wypisanie sciezki Eulera --------------------
#if Euler is True and spojny is True:
    #k = 0
    #for i in range(0, rg):
     #   Vertex[i].visited = False
    #stos = Stack()
    #stos.push(Vertex[0].name)
    #Vertex[0].visited = True
    #W.visited += 1
    #while W.visited != rg:
    #    spr()
    #print 'Cykl Eulera: %s\n\n\n' % stos.Stack

# --------------------------- KOLOROWANIE SL ----------------------

for revisit in range(0, rg):            # reset .visited
    Vertex[revisit].visited = False
    Vertex[revisit].color = 0

kolor_order_list = []
kolor_order = []
deg_order = {}

for v in range(0, rg):
    deg_order[Vertex[v].name] = Vertex[v].deg
order_temp = deg_order

for v in range(0, rg):
    for key, val in deg_order.items():   # --- ustalam kolejnosc SL (smallest last)
        x = min(order_temp.values())
        if x == deg_order[key]:
            kolor_order.append(key)
            order_temp.pop(key, val)

kolor_order.reverse()
print 10*'---', '\nKolorowanie SL\n\nKolejnosc ---> ', kolor_order, '\n\n'


for oznacz in Vertex:        #---- pokoloruj pierwszego z kolor_order
    if oznacz.name == kolor_order[0]:
        oznacz.color = 1
        kolor_order_list.append(oznacz.color)


for akt in kolor_order:
    for ver in Vertex:

        if ver.name == akt and ver.color != 0:
            pass
        elif ver.name == akt:           #--- wez niepokolorowany z kolor_order
            fr_list = ver.friends
            spr_kolor = []
            for friend in fr_list:      #--- przegladam jego sasiadow
                for vert in Vertex:
                    if vert.name == friend:      # --- zbieram kolory sasiadow
                        spr_kolor.append(vert.color)
            spr_kolor.sort()


            temp_list = []
            for temp in range(1, len(spr_kolor)+1):
                temp_list.append(temp)
                for k in spr_kolor:
                    if k in temp_list:
                        temp_list.remove(k)
            if temp_list == []:
                ver.color = max(spr_kolor)+1
            else:
                ver.color = min(temp_list)
            kolor_order_list.append(ver.color)

kolorki = []            #---- wydruk
for kk in range(0, rg):
    kolorki.append([])
    for vv in Vertex:
        if vv.color == kk:
            kolorki[kk].append(vv.name)
for pr in range(0, len(kolorki)):
    if kolorki[pr]:
        print 'Kolor [ %d ] ---' % pr, '%s' % kolorki[pr]



