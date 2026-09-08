print('sup guest')
print('today we are going to the epic theme park of doom')
print('ima figure out the rides you can go on')
name = input('what is your name?')
age = int(input('what is your age?'))
height = int(input('how tall are you in inches?'))
def ticket_check(ticket):
    if ticket == "regular":
        return False
    elif ticket == "premium":
        return True
    else:
        return 100
def member_check(member):
    if member == "yes":
        return True
    elif member == "no":
        return False
    else:
        return 100
def adult_check(adult):
    if adult == "yes":
        return True
    elif adult == "no":
        return False
    else:
        return 100
def vist_time_check(time):
    if time == "morning":
        return "morning"
    elif time == "evening":
        return "evening"
    else:
        return 100
ticket_question = input('did you buy a regular or premium ticket?')
ticket_premium = ticket_check(ticket_question.lower())
member_question = input('are you a park member? yes/no')
park_member_status = member_check(member_question.lower())
adult_question = input('are you visiting with an adult? yes/no')
adult_having_status = adult_check(adult_question.lower())
visit_time = input('are u visiting in the morning or the evening?')
def calculate_admission(age_p):
    if age_p <= 4 and age_p > 0:
        return 0
    elif age_p >= 5 and age_p <= 12:
        return 15
    elif age_p >=13 and age_p <= 64:
        return 30
    else:
        return 20
def calculate_discount(price, member, vist_time):
    discount = 0
    if member == True:
        discount = discount + 5
    if vist_time == "evening":
        discount = discount + 3
    if discount == 8:
        discount = 10
    price = price - discount
    if price <= 0:
        price = 0
    return price
def ride_level(age_f, height_f):
    highest_ride_level = True

    kid_ride_height_req = 36

    family_ride_height_req = 42
    family_ride_age_req = 8

    thrill_ride_height_req = 48
    thrill_ride_age_req = 12

    extreme_ride_height_req = 54
    extreme_ride_age_req = 16


admission_price = calculate_admission(age)
discounted_price = calculate_discount(admission_price, park_member_status, visit_time)