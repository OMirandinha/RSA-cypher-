import os
import math
import random

print('TRABALHO PRODUZIDO PELOS INTEGRANTES:')
print()
print('Antonio Miguel Lazaro Massari')
print('Claudio Uchoa Júnior')
print('Kleber Shibuya Benini')
print('Gabriel da Silva Lopes')
print('Alexsander Rodrigues')
print('Luigi Nastri')
print('Vitor Hugo Miranda')
print('Vitor Faria de Oliveira')

input()
os.system('cls')

print('RSA')

# p, q
	# Escolha se quer que seja aleatorio ou não o 'p' e 'q'
aleatorio = input('Deseja que as Chaves sejão aleátorias (Y/N)? ')

	# DEF - Vereficar se é primo
def numero_primo(numero):
		for n in range(2, numero - 1):
			if numero % n == 0:
				return False
		return True

	
	# DEF - Gerar aleatorio (primo)
def gerar_aleatorio (minimo, maximo):
		primo = random.randint(minimo, maximo)
		while not numero_primo(primo):
			primo = random.randint(minimo, maximo)
		return primo
	
	# Gerar valor aleatorio para 'p' e 'q'
if aleatorio == 'y' or aleatorio == 'Y':
	p = gerar_aleatorio(3, 10000)
	q = gerar_aleatorio(3, 10000)
	while p == q:
		q = gerar_aleatorio(3, 10000)
	
	print('p: {0}'.format(p))
	print('q: {0}'.format(q))

	# Usuario irá escolher valor para 'p' e 'q'
elif aleatorio == 'n' or aleatorio == 'N':
	print('É necessario que sejam primos e diferentes:')
	p = int(input('p: '))
	q = int(input('q: '))
	if numero_primo(p) == False or numero_primo(q) == False:
		raise ValueError("ERROR - UM DOS VALORES NÃO É PRIMO")
	
# n (Multiplicação de 'p' e 'q')
n = p * q
print('n: {0}'.format(n))
	
# phi_n (Phi de n)
phi_n = (p - 1) * (q - 1)
print('Phi de n: {0}'.format(phi_n))

# e (Chave Publica)
e = random.randint(3, phi_n - 1)
	
	# Vereficar se os dois numeros tem o mesmo grande divisor em comum (1)
while math.gcd(e, phi_n) != 1:
	
		# Gerar outro e repitir processo
	e = random.randint(3, phi_n - 1)
print('Chave Publica: {0}'.format(e))
	
# d (Chave Privada)
	# DEF - Achar numero entre 'e' e 'phi_n' que quando (e * d) e depois dividos pelo phi_n (modulo), de como resto 1 
def mod_inverse(e, phi_n):
	for d in range(3, phi_n):
		if (d * e) % phi_n == 1:
			return d
	raise ValueError('ERROR - O RESTANTE DO MODÚLO NÃO É IGUAL AO VALOR 1')
		
d = mod_inverse(e, phi_n)
print('Chave Privada: {0}'.format(d))

# Mensagem
mensagem = input('Mensagem: ')
print()

	# Transforma os caracteres em numeros (ASCII)
mensagem_cod = [ord(ch) for ch in mensagem]
print('Mensagem Codificada (ASCII): {0}'.format(mensagem_cod))

	# Irá pegar os numeros (ASCII) e fazer a seguinte conta para cada caracter ((ch ** e) % n) -> texto criptografado
texto_cript = [pow(ch, e, n) for ch in mensagem_cod]
print('Texto Criptografado: {0}'.format(texto_cript))
print()
	
	# Irá pegar o texto criptografado e fazer a seguinte conta para cada caracter ((ch ** d) % n) -> mensagem codificada 
d = int(input('Insira Chave Privada: '))
mensagem_cod = [pow(ch, d, n) for ch in texto_cript]

	# Transforma os numeros (ASCII) em caracteres
mensagem = ''.join(chr(ch) for ch in mensagem_cod)
	
print('Mensagem: {0}'.format(mensagem))
input()
