class Star_Cinema:
    __hall_list = []

    def entry_hall(self, Hall):
        Star_Cinema.__hall_list.append(Hall)


class Hall(Star_Cinema):

    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.__show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        self.__show_list.append((id, movie_name, time))
        seat = [[0 for i in range(self.cols)] for j in range(self.rows)]
        self.seats[id] = seat

    def book_seats(self, id, row, col):
        self.seats[id][row][col] = 1

    def view_show_list(self):
        for show in self.__show_list:
            print(f'ID:{show[0]} Movie Name:{show[1]} Time:{show[2]}')

    def view_available_seats(self, id):
        for i in self.seats[id]:
            print(i)

    def correct_id(self, id):
        if id in self.seats:
            return True
        else:
            return False

    def booked_seat(self, id, row, col):
        if self.seats[id][row][col] == 1:
            return True
        else:
            return False


# input
cine = Hall(5, 5, 1)
cine.entry_show('1', 'Jawan', '12:30 pm')
cine.entry_show('2', 'Pathan', '2:30 pm')


# Counter :
while 1:
    inpt = input(
        """ 
1.Ongoing Shows 
2.Available Seats
3.Book Seats
4.Exit 
Enter Option : """)
    print(end="\n")

    if inpt == '1':
        print("========================")
        cine.view_show_list()
        print("========================")
    if inpt == '2':
        id = input("Enter ID:")
        if cine.correct_id(id) == True:
            print("Available Seats :")
            cine.view_available_seats(id)
        else:
            print("Invalid ID")

    if inpt == '3':
        id = input("Enter ID: ")

        if cine.correct_id(id) == True:
            ro = input('Input Row:')

            if cine.rows >= ro and cine.cols >= col:
                if cine.booked_seat(id, ro, col) == False:
                    print(
                        f'Your seat ({ro},{col}) is successfully booked for Movie id :{id}')
                    cine.book_seats(id, ro, col)
                else:
                    print(f'Seat ({ro},{col}) is already booked')
            else:
                print(f'({ro},{col}) is invalid seat')
        else:
            print("Invalid ID")

    if inpt == '4':
        break
