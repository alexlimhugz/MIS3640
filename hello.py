def divide(a,b):
    try:
        return a/b
    except:ZeroDivisionError
        return("Zero division in meaningless")
print(divide(1,0))
print("go learn some more math")