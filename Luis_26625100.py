#!/usr/bin/env python3
"""
Proyecto Polinomio de Lagrange.

Cada participante debe completar su módulo y luego solicitar el Pull-Request.
"""

def polinomio_lagrange(X, Y):

    if len(X) != len(Y): raise ValueError("Dimensiones diferentes en X e Y.")

    # Ordena el par (x, y) en forma ascendente por x.
    pares = list(zip(X, Y))
    pares.sort(key = lambda x: x[0])
    X, Y  = zip(*pares)

    def getCurrentPolynom(currentPosition):

        def currentPolynom(x):
            currentPolynomFuction = 1

            for i in range(len(pares)):
                if i != currentPosition:
                    currentPolynomFuction = currentPolynomFuction * ((x - X[i]) / (X[currentPosition] - X[i]))
            return currentPolynomFuction

        return currentPolynom

    def polynom(x):
        polynomFunction = 0

        for i in range(len(pares)):
            polynomFunction = polynomFunction + (Y[i] * getCurrentPolynom(i)(x))

        return polynomFunction


    return polynom


if __name__ == '__main__':
    # Pruebe aquí su Polinomio de Lagrange ...
    X = [2, 1, -1]
    Y = [5, -2, 1]
    polynom = polinomio_lagrange(X,Y)
    aproximation = polynom(2)

    print("La aproximacion encontrada atraves del polinomio de lagrange es de", aproximation)
