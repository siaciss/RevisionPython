from greetings import hello # Une autre 
import mathematics.arithmetic as arithmetic
from mathematics import geometrie
#from mathematics.geometrie import surface_square, surface_rectangle, surface_triangle, surface_circle

if __name__ == "__main__": # Pour executer le code uniquement si le fichier est execute directement
    name = "Assi"
    som = arithmetic.sum_two_numbers(5, 3)
    sub = arithmetic.subtract_two_numbers(10, 4)
    mult = arithmetic.multiply_two_numbers(6, 7)
    div = arithmetic.divide_two_numbers(20, 4)

    square_surface = geometrie.surface_square(5)
    rectangle_surface = geometrie.surface_rectangle(10, 5)
    triangle_surface = geometrie.surface_triangle(6, 4)
    circle_surface = geometrie.surface_circle(3)    

    hello(name) # On appelle la fonction hello du module greetings.py
    print("Somme:", som)
    print("Difference:", sub)
    print("Produit:", mult)
    print("Quotient:", div)
    print("Surface du carre:", square_surface)
    print("Surface du rectangle:", rectangle_surface)
    print("Surface du triangle:", triangle_surface)
    print("Surface du cercle:", circle_surface)     
