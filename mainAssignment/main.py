import csv
import pandas as pd

user_list = []
movie_list = []


def user_wants():

    x = 10
    Booked_seat = 0
    prize_of_ticket = 0
    Total_Income = 0
    Row = 4
    Seats = 4
    Total_seat = Row * Seats
    Booked_ticket_Person = [[None for j in range(Seats)] for i in range(Row)]

    class chart:

        @staticmethod
        def chart_maker():
            seats_chart = {}
            for i in range(Row):
                seats_in_row = {}
                for j in range(Seats):
                    seats_in_row[str(j + 1)] = 'S'
                seats_chart[str(i)] = seats_in_row
            return seats_chart

        @staticmethod
        def find_percentage():
            percentage = (Booked_seat / Total_seat) * 100
            return percentage

    class_call = chart
    table_of_chart = class_call.chart_maker()

    while x != 0:
        print('1 for Show the seats \n2 for Buy a Ticket \n3 for Statistics ',
              '\n4 for Show booked Tickets User Info \n0 for Exit')
        x = int(input('Select Option - '))
        if x == 1:
            if Seats < 10:
                for seat in range(Seats):
                    print(seat, end='  ')
                print(Seats)
            else:
                for seat in range(10):
                    print(seat, end='  ')
                for seat in range(10, Seats):
                    print(seat, end=' ')
                print(Seats)
            if Seats < 10:
                for num in table_of_chart.keys():
                    print(int(num) + 1, end='  ')
                    for no in table_of_chart[num].values():
                        print(no, end='  ')
                    print()
            else:
                count_num = 0
                for num in table_of_chart.keys():
                    if int(list(table_of_chart.keys())[count_num]) < 9:
                        print(int(num) + 1, end='  ')
                    else:
                        print(int(num) + 1, end=' ')
                    count_key = 0
                    for no in table_of_chart[num].values():
                        if int(list(table_of_chart[num].keys())[count_key]) <= 10:
                            print(no, end='  ')
                        else:
                            print(no, end='  ')
                        count_key += 1
                    count_num += 1
                    print()
            print('Vacant Seats = ', Total_seat - Booked_seat)
            print()

        elif x == 2:
            Row_number = int(input('Enter Row Number - \n'))
            Column_number = int(input('Enter Column Number - \n'))
            if Row_number in range(1, Row + 1) and Column_number in range(1, Seats + 1):
                if table_of_chart[str(Row_number - 1)][str(Column_number)] == 'S':
                    if Row * Seats <= 60:
                        prize_of_ticket = 10
                    elif Row_number <= int(Row / 2):
                        prize_of_ticket = 10
                    else:
                        prize_of_ticket = 8
                    print('prize_of_ticket - ', '$', prize_of_ticket)
                    conform = input('"yes" for booking and no for Stop booking - ')
                    person_detail = {}
                    if conform == 'yes':
                        person_detail['Name'] = input('Enter Name - ')
                        person_detail['Gender'] = input('Enter Gender - ')
                        person_detail['Age'] = input('Enter Age - ')
                        person_detail['Phone_No'] = input('Enter Phone number - ')
                        person_detail['Ticket_prize'] = prize_of_ticket
                        table_of_chart[str(Row_number - 1)][str(Column_number)] = 'B'
                        Booked_seat += 1
                        Total_Income += prize_of_ticket
                    else:
                        continue
                    Booked_ticket_Person[Row_number - 1][Column_number - 1] = person_detail
                    print('\n'+'****** Booked Successfully ****')
                else:
                    print('This seat already booked by some one')
            else:
                print()
                print('***  Invalid Input  ***')
            print()

        elif x == 3:
            print('Number of purchased Ticket - ', Booked_seat)
            print('Percentage - ', class_call.find_percentage())
            print('Current  Income - ', '$', prize_of_ticket)
            print('Total Income - ', '$', Total_Income)
            print()

        elif x == 4:
            Enter_row = int(input('Enter Row number - \n'))
            Enter_column = int(input('Enter Column number - \n'))
            if Enter_row in range(1, Row + 1) and Enter_column in range(1, Seats + 1):
                if table_of_chart[str(Enter_row - 1)][str(Enter_column)] == 'B':
                    person = Booked_ticket_Person[Enter_row - 1][Enter_column - 1]
                    print('Name - ', person['Name'])
                    print('Gender - ', person['Gender'])
                    print('Age - ', person['Age'])
                    print('Phone number - ', person['Phone_No'])
                    print('Ticket Prize - ', '$', person['Ticket_prize'])
                else:
                    print()
                    print('---**---  Vacant seat  ---**---')
            else:
                print()
                print('***  Invalid Input  ***')
            print()

        else:
            print()
            print('***  Invalid Input  ***')
            print()

# -------------Methods-------------
# Registration page method

def register_user():
    print("************ Welcome to Login Page *************"+'\n')
    f = open("users.csv", "w", newline='')
    wo = csv.writer(f)
    wo.writerow(["name", "email", "phoneNo", "age", "password"])
    while True:

        name = str(input('name : '))
        email = str(input('Email: '))
        phoneNo = str(input('phone : '))
        age = str(input('age : '))
        password = str(input('Password: '))
        data = [name, email, phoneNo, age, password]
        wo.writerow(data)
        print('\n'+"new user added successfully !"+ '\n')
        ch = input("add another user (y/n) : "+'\n')
        if ch in 'Nn':
            break
    f.close()


# Login page
def login_user():
    print("Welcome to Login Page")
    file = open('users.csv', 'r')
    found = 0
    email = str(input('Email: '))
    password = str(input('Password: '))
    ro = csv.reader(file)
    # next(ro)

    for i in ro:
        # item = i.split(',')
        # if email == item[1] and password == item[4]:
        #     print('Logged in successfully!')
        if i[1] == email and i[4] == password:
            print('\n'+'Logged in successfully!')
            found = 1
            print("*********  welcome  "+ i[0]+"  *********"+'\n')
            user_wants()

    if found == 0:
        print('\n'+"sorry no record found"+'\n')

    file.close()





# Admin Login
def login_admin():
    print('\n'+"****Welcome to Admin Login Page****"+'\n')
    emailid = "admin@gmail.com"
    password = "admin"
    email = input("Enter admin email")
    passw = input("Enter password ")

    if emailid == email and password == passw:
        print('\n'+"******* Welcome Admin! ********")

        print("1-Add new Movie Info")
        print("2- Edit movie Info")
        print("3- Delete Movies")
        print("4- exit")
        admin_input = int(input("Enter your Input:"))
        f = open("movies.csv", "w", newline='')
        wo = csv.writer(f)
        wo.writerow(['title', 'genre', 'length', 'cast', 'director', 'rating', 'language', 'show_timings', 'capacity'])
        if admin_input == 1:
         while True:
            title = input("Enter title : ")
            genre = input("Enter genre : ")
            length = input("Enter length : ")
            cast = input("Enter cast : ")
            director = input("Enter director : ")
            rating = input("Enter rating : ")
            language = input("Enter language : ")
            show_timings = input("Enter show Timings : ")
            capacity = input("Enter capacity : ")
            data = [title, genre, length, cast, director, rating, language, show_timings, capacity]
            wo.writerow(data)

            #movie_list.append(movie_1)
            print("Movie Added successfully")
            ch = input("add another movie (y/n) : ")
            if ch in 'Nn':
             exit(0)
         f.close()
            # We are printing details of movie
            # for i in movie_list:
            #     print(i.title)
            #     print(i.cast)
            #     print(i.director)
        elif admin_input == 2:
            print("'Admin!'You are on edit movie page")


            print("1- Title")
            print("2- genre")
            print("3- length")
            print("4- Rating")
            admin_input2 = input("Enter what do you want to edit")
            if admin_input2 == 1:
                i=input("Enter the index of the title : ")
                df = pd.read_csv("movies.csv")
                df.loc[i,'title'] = input("Enter the new title : ")


                df.to_csv("movies.csv", index=False)

                print(df)
            elif admin_input2 == 2:
                exit()
            elif admin_input2 == 3:
                exit()

            elif admin_input2 == 4:
                exit()


        elif admin_input == 3:
            df = pd.read_csv("movies.csv")


            df_s = df[:5]

            # 3.
            df_s.set_index('sepal_length', inplace=True)

            # 4.1.
            df_s = df_s.drop(5.1)

            print(df_s)

        elif admin_input ==4 :
            exit(0)

    else:
        print("Wrong credentials!")

def login():
    print('\n' + "1. Login for user " + '\n' + "2. Login for admin")
    select = int(input('\n'+"Enter your Input" + '\n'))
    if select ==1:
        login_user()
    elif select == 2 :
        login_admin()
    else :
        print("Invalid input")
        exit(0)


# Welcome page


while True:
    print('\n'+"****Welcome to Book my Show****"+'\n')
    print("1. Login ")
    print("2. Register New Account!")
    print("3. Exit")
    user_input = int(input("Enter your Input : "+'\n'))
    if user_input == 1:
        login()

    elif user_input == 2:
        register_user()
    elif user_input == 3:
        print("Logging off")
        break
    else:
        'Invalid Input'