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

def medie(l):
    sum(l)/len(l)
    x=int(input("Dati numarul:"))
    if medie<x:
        return True

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x//2 + 1):
        if x % i == 0:
            return False
    return True

def test_is_prime():
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(5) == True

def not_prime(x):
    if is_prime(x) == True:
        return False
    elif is_prime(x) == False:
        return True

def test_not_prime():
    assert not_prime(7) == False
    assert not_prime(8) == True
    assert not_prime(9) == True

def toate_elementele_neprime(l):
    rezultat = []
    for x in l:
        if not_prime(x) == True:
            rezultat.append(x)
    return rezultat

def test_toate_elementele_neprime():
    assert toate_elementele_neprime([]) == []
    assert toate_elementele_neprime([3,4]) == [4]
    assert toate_elementele_neprime([6,9]) == [6,9]

def get_longest_all_not_prime(l):
    subsecventa_max = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if toate_elementele_neprime(l[i:j+1]) and len(subsecventa_max) < len(l[i:j+1]):
                subsecventa_max = l[i:j+1]
    return subsecventa_max

def test_get_longest_all_not_prime():
    assert get_longest_all_not_prime([]) == []
    assert get_longest_all_not_prime([2,3]) == []
    assert get_longest_all_not_prime([10,20])== [10,20]

def get_longest_average_below(l):
    subsecventa_max = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if medie(l[i:j + 1]) and len(subsecventa_max) < len(l[i:j + 1]):
                subsecventa_max = l[i:j + 1]
    return subsecventa_max

def main():
    test_is_prime()
    test_not_prime()
    test_toate_elementele_neprime()
    test_get_longest_all_not_prime()
    l = []
    while True:
        print_menu()
        optiune = input("Dati optiunea:")
        if optiune == "1":
            l = citire_lista()
        elif optiune == "2":
            print(get_longest_all_not_prime(l))
        elif optiune == "3":
            print(get_longest_average_below(l))
        elif optiune == "4":
            break

main()
