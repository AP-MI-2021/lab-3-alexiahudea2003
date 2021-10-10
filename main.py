#Proprietatile 7 si 17

def print_menu():
    print("1. Citire lista")
    print("2. Determinare cea mai lungă subsecvență cu proprietatea 1")
    print("3. Determinare cea mai lungă subsecvență cu proprietatea 2")
    print("4. Iesire")

def citire_lista():
    l = []
    given_string = input("Dati lista, cu elementele separate prin virgula:")
    numbers_as_string = given_string.split(",")
    for x in numbers_as_string:
        l.append(int(x))
    return l

def is_prime(x):
    '''
    determina daca un nr. este prim
    :param x: un numar intreg
    :return: True, daca x este prim sau False in caz contrar
    '''
    if x < 2:
        return False
    for i in range(2, x//2 + 1):
        if x % i == 0:
            return False
    return True

def test_is_prime():
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(5) is True

def not_prime(l):
    '''
    determina daca toate elementele unei liste sunt neprime
    :param l: lista nr. intregi
    :return: True, daca proprietatea e adevarata, False in caz contrar
    '''
    for x in l:
        if is_prime(x):
            return False
    return True

def test_not_prime():
    assert not_prime([19,6,8]) is False
    assert not_prime([7,13]) is False
    assert not_prime([44,40,12]) is True

def get_longest_all_not_prime(l):
    '''
    determina cea mai lunga subsecventa de nr. neprime dintr-o lista
    :param l: lista de nr. intregi
    :return: cea mai lunga subsecventa de nr. neprime
    '''
    secventa_finala = []
    lungime_maxima = 0
    for i in range(len(l)):
        for j in range(i, len(l)):
            secventa_initiala = l[i:j+1]
            if len(secventa_initiala) > lungime_maxima and not_prime(secventa_initiala):
                lungime_maxima = len(secventa_initiala)
                secventa_finala = secventa_initiala
    return secventa_finala

def test_get_longest_all_not_prime():
    assert get_longest_all_not_prime([6,8,7]) == [6,8]
    assert get_longest_all_not_prime([3,6,7]) == [6]
    assert get_longest_all_not_prime([6,8,10,7]) == [6,8,10]

def medie_inferioara_unei_valori(l,valoare):
    '''
    determina daca media aritmetica a elementelor unei liste este mai mica decat o valoare data
    :param l: lista de nr. intregi
    :return: True sau False
    '''
    if(sum(l)/len(l) < valoare == True):
        return True
    else:
        return False

def test_medie_inferioara_unei_valori():
    assert medie_inferioara_unei_valori([7,8],12) is False
    assert medie_inferioara_unei_valori([10,20],20) is True
    assert medie_inferioara_unei_valori([3,2],6) is False

def get_longest_average_below(l,valoare):
    '''
    determina cea mai lunga subsecventa de nr. a caror medie aritmetica se afla sub valoarea data
    :param l: lista de nr. intregi
    :return: cea mai lunga subsecventa de nr. a caror medie aritmetica se afla sub valoarea data
    '''
    secventa_finala = []
    lungime_maxima = 0
    for i in range(len(l)):
        for j in range(i, len(l)):
            secventa_initiala = l[i:j+1]
            if len(secventa_initiala) > lungime_maxima and medie_inferioara_unei_valori(secventa_initiala,valoare):
                lungime_maxima = len(secventa_initiala)
                secventa_finala = secventa_initiala
    return secventa_finala

def test_get_longest_average_below():
    assert get_longest_average_below([6,8,22],8) == [6,8]
    assert get_longest_average_below([],3) == []
    assert get_longest_average_below([3,9],5) == [3]

def main():
    test_get_longest_all_not_prime()
    test_get_longest_average_below
    l = []
    while True:
        print_menu()
        optiune = input("Dati optiunea:")
        if optiune == "1":
            l = citire_lista()
        elif optiune == "2":
            print(get_longest_all_not_prime(l))
        elif optiune == "3":
            valoare = int(input("Introduceti valoarea:"))
            print(get_longest_average_below(l,valoare))
        elif optiune == "4":
            break
main()
