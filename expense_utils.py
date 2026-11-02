def validate_amount(amount):
    if amount>0:
        return True
    else:
        return False


def validate_description(description):
    if description.strip() == "":
        return False
    else:
        return True  


def validate_categoryy(category):
    if category.strip() == "":
        return False
    else:
        return True

import random

def generate_id():
    i = random.randint(10000, 99999)
    return "EXP-"+str(i)


def calculate_total(amounts):
    return sum(amounts)


def calculate_category_total(expenses, category):
    total = 0

    for i in expenses:
        if i["category"] == category:
            total = total + i["amount"]
    
    return total        

def calculate_avg(amounts):
    if len(amounts) == 0:
        return 0
    
    total = sum(amounts)
    a = len(amounts)
    avg = total/a
    return avg


