n= int(input("saisir le nombre de copies:"))
if n<=10:
    f= n*0.30
elif n<= 30 :
    f=n*0.25
else:
    f= n*0.20
print("le montant de facture  a payer est :" ,f)
