def get_base_16_from_2(n: str):
	'''
	Transforma un numar din baza 2 in baza 10.
	Input:
	- n : int
	Output:
	- scrierea numarului citit in baza 2, in baza 16.

	Am folosit functii predefinite care sa ma ajute in calcul.

	INTREBARE: in urma execturarii functiei, in output apare rexultatul corect insa cu '0x' inaintea rezultatului.
				apare o eroare la functia de test.
	'''
	decimal_representation = int(n, 2)
	baza = hex(decimal_representation)
	return baza


'''
???????????
def test_get_base_16_from_2():
	assert get_base_16_from_2( 0001 ) == 0x1
	assert get_base_16_from_2( 00010010 ) == 0x12
	assert get_base_16_from_2( 1010 ) == 0xa
	assert get_base_16_from_2( 0010000000100001 ) == 0x2021
	assert get_base_16_from_2( 101010111100000110011000 ) == 0xabc198
'''


def get_n_choose_k(n: int, k: int):
	'''
	Calcularea combinarilor de N numere luate cate K

	Input:
	-n,k : int

	Output:
	se returneaza prin parametrul "combinari" rezultatul calculului

	Am folosit variabile ca "n_fact, k_fact, n_and_k_fact" care reprezinta rezultatul factorial al lui n, k, si (n-k).
	'''
	n_and_k_fact = 1
	d = n-k
	while d:
		n_and_k_fact = n_and_k_fact * d
		d = d-1
	n_fact = 1
	while n:
		n_fact = n_fact * n
		n = n-1
	k_fact = 1
	while k:
		k_fact = k_fact * k
		k = k-1
	numitor = k_fact * n_and_k_fact
	combinari = n_fact // numitor
	return combinari


def test_get_n_choose_k():
	assert get_n_choose_k(3, 2) == 3
	assert get_n_choose_k(6, 4) == 15
	assert get_n_choose_k(7, 3) == 35
	assert get_n_choose_k(5, 2) == 10
	assert get_n_choose_k(6, 3) == 20


def main():
	while True:
		print('1. Transformarea din baza 2 in baza 16.')
		print('2. Combinari de n luate cate k.')
		print('x. Iesire din program - exit.')
		optiune = input('Alege optiunea: ')
		if optiune == '1':
			nr1 = input('Dati numarul in baza 2: ')
			baza = get_base_16_from_2(nr1)
			print(f'In baza 16, numarul eate {baza}.')
			print("\n")
		elif optiune == '2':
			n = int(input('Dati numarul n: '))
			k = int(input('Dati numarul k: '))
			combinari = get_n_choose_k(n, k)
			print(f'Rezultatul a n combinari luate cate k este {combinari}.')
			print("\n")
		elif optiune == 'x':
			break
		else:
			print('Optiune invalida!')


'''test_get_base_16_from_2()'''
test_get_n_choose_k()
main()
