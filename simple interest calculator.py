#### SIMPLE INTEREST CALCULATOR #####

p = float(input( " Enter The Principal : "))
r = float(input( " Enter The Rate : "))
t = float(input( " Enter The Time : "))

SI = ( p * r * t ) / 100
Amt = ( p + SI )

print(f" The Principal {p} , Rate {r} and Time {t} and The Simple Interest is {SI:.2f} and Total Amount is {Amt:.2f}")
