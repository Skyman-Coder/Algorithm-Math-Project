inputs = []
i = 0
#Developer: AmirHossien-Rahimi

while True:
    try:
        value = float(input(f'Enter Number {i+1}: '))
        inputs.append(value)
        i += 1
    except ValueError:
        print('Vorodi Shoma Addad Nist!')   
    if len(inputs) >= 4:
         break
         del i #Baray Pak Kardan Motegayer

while True:
    try:
        n = int(input('Shomare Jomle Khod Ra Vared Konid: '))
    except ValueError:
        print('Lotfan Shomare Ra Dorost Vared Konid!')
    else:
            break
            
if round(inputs[1] - inputs[0], 1) == round(inputs[3] - inputs[2], 1):
    d = inputs[1] - inputs[0]
    print(f'Olgo Shoma Hesabi Ast. Gadre Nesbat: {d}')
    target = inputs[0] + (n - 1) * d
    print('Javab:', target)
elif inputs[1] / inputs[0] == inputs[3] / inputs[2]:
    r = inputs[1] / inputs[0]
    print(f'Olgo Shoma Hendese Ast. Gadre Nesbat: {r}')
    target = inputs[0] * pow(r, n - 1)
    print('Javab:', target)
else:
    print('Donbale Shoma Na Hesabi Ast Va Na Hendese!')

#for Mr.Taragi
