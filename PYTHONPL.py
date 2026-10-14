def tlumacz_i_uruchom(kod_pl):
    linie = kod_pl.strip().split('\n')
    przetlumaczone_linie = []

    for linia in linie:
        """ Podmieniamy polskie słowa na angielskie odpowiedniki Pythona
            NAJPIERW podmieniamy dłuższe słowa, żeby krótsze ich nie popsuły ich nie popsuło
            
        """
        linia = linia.replace("jeslijednak", "elif")
        linia = linia.replace("jeslinie", "else")
        # TERAZ bezpiecznie podmieniamy resztę
        linia = linia.replace("wypisz", "print")
        linia = linia.replace("wpisz", "input")
        linia = linia.replace("calkowita", "int")
        linia = linia.replace("jesli", "if")
        linia = linia.replace("ewaluuj", "eval")
        linia = linia.replace("dopoki", "while")
        linia = linia.replace("prawda", "True") 
        linia = linia.replace("przerwij", "break")
        przetlumaczone_linie.append(linia)

    kod_py = "\n".join(przetlumaczone_linie)
    try:
        exec(kod_py)
    except Exception as e:
        print(f"Blad: {e}")

# kod po polsku w pythonPL
moj_kod = """
wypisz("Kalkulator w pythonPL")
wypisz("dodawanie = + np 1+1")
wypisz("odejmowanie = - np 1-1")
wypisz("mnożenie = * np 1*1")
wypisz("dzielenie = / np 1/1")
wypisz("potęga = ** np 1**1")
wypisz("reszta z dzielenia = % np 1%1")
wypisz("pierwiastek = **0.5 np 1**0.5")
wypisz("napisz wyjdź żeby zamknąć program")
wypisz("====================================")
dopoki prawda:
    dzialanie = wpisz("Wpisz całe działanie lub wyjdź: ")
    
    jesli dzialanie == "wyjdź":
        wypisz("Do widzenia")
        przerwij


    w = ewaluuj(dzialanie)
    wypisz("Wynik to")
    wypisz(w)
    wypisz("====================================")
"""

tlumacz_i_uruchom(moj_kod)
