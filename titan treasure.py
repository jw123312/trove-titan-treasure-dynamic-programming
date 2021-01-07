#test if titan treasure worht it

price = 2800 # price of titan treasures

#starting money
money = 400000

# probility of geting ammount
probact = [43.29268293,
25.6097561,
14.63414634,
10.36585366,
1.829268293,
1.219512195,
3.048780482
    ]

prob = []

for i in probact:
    prob.append(i/100)

def t(m):

    if m < price:
        return 0

    else:
        profit = (-100, 0)
        for i in range(10):
            if m > price*i:
                earning = (prob[0]*1500+ prob[1]*2500 + prob[2]*3500 + prob[3]*5000 + prob[4]*6000 + prob[5]*7500 + prob[6]*9999)*i + m - price*i
            
                if earning > profit[0]:
                    profit = (earning, i)
        return profit



print(t(money))



