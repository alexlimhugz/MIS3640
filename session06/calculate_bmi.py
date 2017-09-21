weight = input('how much do you weigh in kg?')
weight = float(weight)
height = input('what is your height in squared meter?')
height = float(weight)   

BMI = weight / (height * weight)

if BMI <= 18.5:
    print('your BMI is{:.1f}. You are underweighted.'.format(BMI))

elif BMI > 18.5 and BMI <= 24.9:
    print('your BMI is{:.1f}. You are normal weighted.'.format(BMI))

elif BMI > 25 and BMI <= 29.9:
    print('your BMI is{:.1f}. You are over-weighted.'.format(BMI))
        
else:
    print('your BMI is{:.1f}. You are obese.'.format(BMI))
    

BMI = weight/height
BMI = float(BMI)