#!/usr/bin/python3
import sys


def help():
    print("É necessário informar a nota.")
    print("Sintaxe correta: {} <nota>".format(sys.argv[0]))


def conceito(nota):
    if nota > 10:
        print("Nota inválida")
    elif nota >= 9.1:
        print("Conceito: A")
    elif nota >= 8.1:
        print("Conceito: A-")
    elif nota >= 7.1:
        print("conceito: B")
    elif nota >= 6.1:
        print("Conceito: B-")
    elif nota >= 5.1:
        print("Conceito: C")
    elif nota >= 4.1:
        print("Conceito: C-")
    elif nota >= 3.1:
        print("Conceito: D")
    elif nota >= 2.1:
        print("Conceito: D-")
    elif nota >= 1.1:
        print("Conceito: E")
    elif nota >= 0.0:
        print("Conceito: E-")
    else:
        print("Nota inválida")


if __name__ == '__main__':
    nota = float(input("Digite a nota: "))
    conceito(nota)
