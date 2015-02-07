def invest(amount, rate, time):
    '''
    Amount in BTC
    Rate - daily rate
    Time in days
    RRSO = end_amount/principial_amount * 100%
    '''
    principial=amount = amount
    for i in range(1, time):
        amount = amount * rate
        print "%s, %s" % (i, amount)
        if i%30 == 0:
            print "You have to pay %s BTC" % (0.05*principial)
            amount = amount - (principial*0.05)

    print "Loan RRSO: %s" % (amount/principial)
