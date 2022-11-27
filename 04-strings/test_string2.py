#!/usr/bin/python -tt
# coding: utf-8
import unittest

# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
#
# Dado uma string, se o seu comprimento for pelo menos 3,
# adicione 'ing' ao final.
# Caso já termine em 'ing' adicionar "ly".
# Se o comprimento da string for inferior a 3, deixe-o inalterado.
def verbing(s):
    if "ing" in s:
        return s + "ly"
    elif len(s) >= 3:
        return s + "ing"
    else:
        return s


# (google solution)
def verbingV2(s):
    if len(s) >= 3:
        if s[-3:] != "ing":
            s = s + "ing"
        else:
            s = s + "ly"
    return s


# Given a string, find the first appearance of the substring 'not' and 'bad'.
# If the 'bad' follows # the 'not',
# replace the whole 'not'...'bad' substring with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
#
# Dado um astring, procurar a primeira ocorrência da substring 'not' e 'bad'
# Se 'bad' vier após o 'not'
# substituir todo o trecho "not ... bad" por 'good'
# Retorne a string resultante.
def not_bad(s):
    n = s.find("not")
    b = s.find("bad")
    if n != -1 and b != -1 and b > n:
        s = s[:n] + "good" + s[b + 3 :]
    return s


# Consider dividing a string into two halves.
# If the length is even,
#   the front and back halves are the same length.
# If the length is odd,
#    we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
#
# Considere dividir uma string em duas metades.
# Se o comprimento for par,
#   a parte da frete (front) e a parte de trás (back) são do mesmo tamanho.
# Se o comprimento for ímpar,
#   o caracter extra irá para a aprte da frente.
#
# Dado 2 strings, 'a' e 'b', retornar um string na forma
# a front + b front + a back + b back
def front_back(a, b):
    a_middle = int(len(a) / 2)
    b_middle = int(len(b) / 2)

    # adiciona 1 se o tamanho for ímpar
    if len(a) % 2 == 1:
        a_middle = a_middle + 1

    if len(b) % 2 == 1:
        b_middle = b_middle + 1

    return a[:a_middle] + b[:b_middle] + a[a_middle:] + b[b_middle:]


class MyTest(unittest.TestCase):
    def test_verbing(self):
        self.assertEqual(verbing("hail"), "hailing")
        self.assertEqual(verbing("swiming"), "swimingly")
        self.assertEqual(verbing("do"), "do")

    def test_not_bad(self):
        self.assertEqual(not_bad("This movie is not so bad"), "This movie is good")
        self.assertEqual(
            not_bad("This dinner is not that bad!"), "This dinner is good!"
        )
        self.assertEqual(not_bad("This tea is not hot"), "This tea is not hot")
        self.assertEqual(not_bad("It's bad yet not"), "It's bad yet not")

    def test_front_back(self):
        self.assertEqual(front_back("abcd", "xy"), "abxcdy")
        self.assertEqual(front_back("abcde", "xyz"), "abcxydez")
        self.assertEqual(front_back("Kitten", "Donut"), "KitDontenut")


if __name__ == "__main__":
    unittest.main()
