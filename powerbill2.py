print "Let's estimate this month's power bill.\n"

a = int (raw_input ("Enter last month's meter reading: \n"))
while a < 1 or a > 9999:
        print 'Bad data'
        print 'Please enter a valid meter reading'
        a = int (raw_input ("Enter last month's meter reading: \n"))

b = int (raw_input ('Enter the current meter reading: \n'))
while b < 1 or b > 9999 or b < a:
        print 'Bad data'
        print 'Please enter a valid meter reading'
        b = int (raw_input ("Enter last month's meter reading: \n"))

c = int (raw_input ("Enter how many days since last month's reading: \n"))
while c < 1 or c > 31:
        print 'Bad data'
        print 'Please enter a valid number of days'
        c = int (raw_input ("Enter how many days since last month's reading: \n"))

def estwatt(a,b,c):
    sofar = b-a
    watts = sofar / float(c) * 31
    return int(watts)

estwatts = estwatt(a,b,c)
print
print 'Estimated usage:',estwatts

v100 = 60.7
v200 = 125.9
v300 = 187.9
v400 = 280.6
v500 = 417.7
vmax = 709.5


def fixed (estwatts):
    if 0 < estwatts <= 100:
        f = 410
    elif 101 < estwatts <= 200:
        f = 910
    elif 201 < estwatts <= 300:
        f = 1600
    elif 301 < estwatts <= 400:
        f = 3850
    elif 401 < estwatts <= 500:
        f = 7300
    elif 501 < estwatts:
        f = 12940 
    return f
    
def vrate(estwatts):
    if 0 < estwatts <= 100:
        v = v100 * estwatts
    elif 101 < estwatts <= 200:
        v = (v100*100) + (estwatts-100) * v200
    elif 201 < estwatts <= 300:
        v = (v100*100) + (v200*100) + (estwatts-200) * v300
    elif 301 < estwatts <= 400:
        v = (v100*100) + (v200*100) + (v300*100) + (estwatts-300) * v400
    elif 401 < estwatts <= 500:
        v = (v100*100) + (v200*100) + (v300*100) + (v400*100) + (estwatts-400) * v500
    elif 501 < estwatts:
        v = (v100*100) + (v200*100) + (v300*100) + (v400*100) + (v500*100) + (estwatts-500) * vmax
    return v

def tax ():
    t = (fixed(estwatts) + vrate(estwatts)) * 0.1
    t1 = t * 1.37
    return t1
 
tvfee = 2500
    
bill = fixed (estwatts) + vrate(estwatts) + tax() + tvfee
print 'Estimated power bill for this month:',   int(bill), 'won' 
print
print 'Are you surprised?'
print
bye = raw_input ('Press ENTER to exit.')
         
        