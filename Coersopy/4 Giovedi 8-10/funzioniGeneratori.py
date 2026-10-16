def decoratore(funzione):
    def wrapper():
        print('prima')
        funzione()
        print('dopo')
    return wrapper

@decoratore
def ciao():
    print('ciao')
    
ciao()