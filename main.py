#Proprietatile 7 si 17

def print_menu():
    print("1. Citire lista")
    print("2. Determinare cea mai lungă subsecvență cu proprietatea 1")
    print("3. Determinare cea mai lungă subsecvență cu proprietatea 2")
    print("4. Determinare cea mai lunga subsecventa cu proprietatea 3")
    print("5. Iesire")

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
    average = sum(l)/len(l)
    if average < valoare:
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
    secventa_1 = []
    lungime_1 = 0
    for i in range(len(l)):
        for j in range(i, len(l)):
            secventa_2 = l[i:j+1]
            if len(secventa_2) > lungime_1 and medie_inferioara_unei_valori(secventa_2,valoare):
                lungime_1 = len(secventa_2)
                secventa_1 = secventa_2
    return secventa_1

def test_get_longest_average_below():
    assert get_longest_average_below([6,8,22],8) == [6,8]
    assert get_longest_average_below([],3) == []
    assert get_longest_average_below([3,9],5) == [3]

def toate_prime(l):
    '''
    determina daca toate elementele unei liste sunt prime
    :param l: lista de nr. intregi
    :return: True, daca este adevarat, False in caz contrar
    '''
    for x in l:
        if is_prime(x) == True:
            return True
    return False

def test_toate_prime():
    assert toate_prime([7,8]) is False
    assert toate_prime([7,13]) is True
    assert toate_prime([3,4,5]) is False


def get_longest_all_primes(l):
    '''
    determina cea mai lunga subsecventa care are elemente doar nr. prime
    :param l: lista de nr. intregi
    :return: cea mai lunga subsecventa de nr. prime
    '''
    secventa_prima = []
    lungime_0 = 0
    for i in range(len(l)):
        for j in range(i, len(l)):
            secventa_secunda = l[i:j + 1]
            if len(secventa_secunda) > lungime_0 and toate_prime(secventa_secunda):
                lungime_0 = len(secventa_secunda)
                secventa_prima = secventa_secunda
    return secventa_prima

def test_get_longest_all_primes():
    assert get_longest_all_primes([8,9]) == []
    assert get_longest_all_primes([3,5]) == [3,5]
    assert get_longest_all_primes([4,8]) == []

def main():
    test_get_longest_all_not_prime()
    test_get_longest_average_below()
    test_get_longest_all_primes()
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
            print(get_longest_all_primes(l))
        elif optiune == "5":
            break
main()
