def testnume(numele,vastata):
	print ("Salut te numesti " + numele + " si ai " + vastata + " ani")
	return
	
welcome = print("Pentru început, te rog spune-ne câte ceva despre tine!")
nume = input("Cum te numesti?: ")
varsta = input("Cati ani ai?: ")

testnume(nume,varsta)


wins = 0
losses = 0

#Întrebarea număru 1 

inceputmesaj = print("Prima întrebare o să fie destul de simplă!")
creat=['2007']
aproape=['2008','2006']
like=input('Metinul a fost creat în anul ?: ')
f=like in creat
g=like in aproape
if f:
	print ("Răspuns Corect!")
	wins +=1
elif g:
	print ("Ai fost pe aproape!")
else:
	print ('Răspuns gresit!')
	losses +=1
	
puncte = print(" Pana acum ai acumulat\n [" + str(wins) + " puncte]")
#Întrebarea număru 2

inceputmesaj = print("Daca ai raspuns corect la prima intrebare\naceasta o sa fie o nimica toata")
creat=['Nu','nu']
aproape=['Da','da']
like=input('Fierarul tine un fierastrau în mână?"\nda/nu: ')
f=like in creat
g=like in aproape
if f:
	print ("Răspuns Corect!")	
	wins +=1
else:
	print ('Răspuns gresit!')
	losses +=1
	
puncte = print(" Pana acum ai acumulat\n [" + str(wins) + " puncte]")
#Întrebarea număru 3 

inceputmesaj = print("De acum o să fie umpic mai greu!")
creat=['Da','da']
aproape=['Nu','nu']
like=input('Izbitura la Perfect Master are nevoie de 210 MP ?: ')
f=like in creat
g=like in aproape
if f:
	print ("Răspuns Corect!")	
	wins +=1
elif g:
	print ("Ai fost pe aproape!")
else:
	print ('Răspuns gresit!')
	losses +=1
	
puncte = print(" Pana acum ai acumulat\n [" + str(wins) + " puncte]")
#Întrebarea număru 4 

inceputmesaj = print("Aceasta este ultima întrebare!")
creat=['Da','da']
aproape=['Nu','nu']
like=input('Putem strica un server aruncand mult yang pe jos?: ')
f=like in creat
g=like in aproape
if f:
	print ("Răspuns Corect!")	
	wins +=1
elif g:
	print ("Ai fost pe aproape!")
else:
	print ('Răspuns gresit!')
	losses +=1
	
puncte = print(" Bravo ai terminat jocul cu : \n [" + str(wins) + " puncte]")
	
sfarsit = print("Acest mini quiz metin2 a fost creat de câtre Grimmjow\nMultumesc pentru participare!")