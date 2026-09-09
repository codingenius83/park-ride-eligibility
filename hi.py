#welcomings to the script

print('\nsup guest')
print('today we are going to the epic theme park of doom')
print('ima figure out the rides you can go on\n')

#functions in case if user puts in a negative number for age or height

def age_checker(a):

    if a <= 0:
        return 0
    
    else:
        return a
    
def height_checker(h):

    if h <= 0:
        return 0
    
    else:
        return h
    
#gets name, age, and height

name = input('\nwhat is your name?')

age = int(input('\nwhat is your age?'))
age = age_checker(age)

height = int(input('\nhow tall are you in inches?'))
height = height_checker(height)

#function for the case that user puts something other than what they are supposed to put.

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

def visit_time_check(time):

    if time == "evening":
        return "evening"
    
    elif time == "morning":
        return "morning"
    
    else:
        return 100

#gets if u have ticket premium, your member status, if you have an adult with you, and what time you are visiting

ticket_question = input('\ndid you buy a regular or premium ticket?')
ticket_premium = ticket_check(ticket_question.lower())

member_question = input('\nare you a park member? yes/no')
park_member_status = member_check(member_question.lower())

adult_question = input('\nare you visiting with an adult? yes/no')
adult_having_status = adult_check(adult_question.lower())

visit_time_question = input('\nare u visiting in the morning or the evening?')
visit_time = visit_time_check(visit_time_question.lower())

#this function calculates your admission based on your age

def calculate_admission(age_p):

    if age_p <= 4 and age_p > 0:
        return 0
    
    elif age_p >= 5 and age_p <= 12:
        return 15
    
    elif age_p >=13 and age_p <= 64:
        return 30
    
    else:
        return 20
    
#this function will calculate your discount based on the calculated admission, your member status, and what time you are visiting

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

#this function determines the highest level ride you can ride based on your age, and height

def ride_level(age_f, height_f):

    kid_ride_height_req = 36

    family_ride_height_req = 42
    family_ride_age_req = 8

    thrill_ride_height_req = 48
    thrill_ride_age_req = 12

    extreme_ride_height_req = 54
    extreme_ride_age_req = 16

    if age_f >= extreme_ride_age_req and height_f >= extreme_ride_height_req:
        return "extreme rides"
    
    elif age_f >= thrill_ride_age_req and height_f >= thrill_ride_height_req:
        return "thrill rides"
    
    elif age_f >= family_ride_age_req and height_f >= family_ride_height_req:
        return "family rides"
    
    elif height_f >= kid_ride_height_req:
        return "kid rides"
    
    else:
        return "no rides"
    
#this function checks if you have an adult with you if you are below the age of 13

def check_supervision(age_f, visiting_with_adult):

    age_enter_req = 13

    if age_f >= age_enter_req:
        return "approved"
    
    else:

        if visiting_with_adult == True:
            return "approved"
        
        else:
            return "adult required or u didnt answer the question correctly"
        
#this function checks your ticket to see if its premium and returns a string to be used in guest report

def premium_bonus_check(ticket):

    if ticket == True:
        return "you recieve a free snack and priority ride access"
    
    else:
        return "u aint premium buddy or u didnt answer the question correctly"
    
#this functions checks to see if you are identified as a vip

def check_vip(prem_ticket, park_memb, age_lol):

    if prem_ticket == True and park_memb == True and age_lol >= 65:
        return "you are a vip"
    
    else:
        return "boi u aint a vip"
    
#call all the functions

admission_price = calculate_admission(age)
discounted_price = calculate_discount(admission_price, park_member_status, visit_time)
highest_ride_level = ride_level(age, height)
supervision_status = check_supervision(age, adult_having_status)
premium_bonus = premium_bonus_check(ticket_premium)
is_vip = check_vip(ticket_premium, park_member_status, age)

#final guest report

print('\n\n','='*25,'\nepic theme park of doom\nguest report\n','='*25)
print(f'\n\nguest: {name}\n\nage: {age}\nheight: {height}\nticket premium: {ticket_premium}\npark member: {park_member_status}')
print(f'\n\nregular admission: {admission_price}\nfinal admission: {discounted_price}')
print(f'\n\nhighest ride level: \n{highest_ride_level}\n\nsupervision status: \n{supervision_status}')
print(f'premium bonus: \n{premium_bonus}\n\n')
print(f'vip: {is_vip}\n\n')
print('='*25, '\nhave an amazing day at this epic park\n', '='*25)

#bro cant ride no rides

if highest_ride_level == "no rides":
    print('\nbro cant ride any rides lol' * 10)