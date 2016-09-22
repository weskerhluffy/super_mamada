'''
Created on 22/09/2016

@author: ernesto
'''


import logging
import fileinput

nivel_log = logging.ERROR
#nivel_log = logging.DEBUG
logger_cagada = None

def super_chingadera_main():
    lineas = list(fileinput.input())
    
    mierda = lineas[0].strip()
    
    logger_cagada.debug("io q fui %s" % mierda)
    
    disque_pila_letras = []
    for letra in mierda:
        disque_pila_letras.append(letra)
        if(len(disque_pila_letras) > 1):
            if(disque_pila_letras[-1] == disque_pila_letras[-2]):
                disque_pila_letras.pop()
                disque_pila_letras.pop()
    
    logger_cagada.debug("la cadena q kedo %s" % disque_pila_letras)
    if(disque_pila_letras):
        print("%s" % ("".join(disque_pila_letras)))
    else:
        print("Empty String")
                
        

if __name__ == '__main__':
        FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
        logging.basicConfig(level=nivel_log, format=FORMAT)
        logger_cagada = logging.getLogger("asa")
        logger_cagada.setLevel(nivel_log)
    
        super_chingadera_main()
