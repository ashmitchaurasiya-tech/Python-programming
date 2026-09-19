''' program to accept basic salary of emlployee and its HRA is 20%,DA is 80% and deduct
 tax 200 with PF of 12% of basic salary, then print the net salary'''
basic=float(input("Enter basic salary :"))
hra=basic*0.20
da=basic*0.80
tax=200
pf=basic*0.12
gross=basic+hra+da
net=gross-tax-pf
print("basic salary: ",basic)
print("HRA(20%): ",hra)
print("DA(80%): ",da)
print("Tax(200): ",tax)
print("PF(12%): ",pf)
print("Gross salary: ",gross)
print("Net salary: ",net)