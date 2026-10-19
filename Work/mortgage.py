# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0 
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    months = months + 1
    if months >= extra_payment_start_month and months <= extra_payment_end_month :
        if payment + extra_payment > principal :
            total_paid = total_paid + principal
            principal = 0.0
        else:
            principal = principal * (1+rate/12) - (payment + extra_payment)
            total_paid = total_paid + payment + extra_payment
        print("---")
    else :
        if payment + extra_payment > principal :
            total_paid = total_paid + principal
            principal = 0.0
        else:
            principal = principal * (1+rate/12) - payment
            total_paid = total_paid + payment
    print(months,total_paid,principal)
    

print('Total paid', total_paid, 'Months', months)
