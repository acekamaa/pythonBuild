# learning about python match
# use the week day number to print the weekday name
day = 3
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case _: # default value '_'
        print("Sunday")

# combining values using pipe
eggs = 5
match eggs:
    case 1 | 2 | 3 | 4:
        print("Cook homelet")
    case 5 | 6 | 7 :
        print("Bake cake")