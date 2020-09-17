#Västtrafik
#Average month 30.42 days
dayTicket = 30
monthTicket = 775


days = int(input("How many days do you wish to travel: "))
print(f"Price: {dayTicket*days}kr")

print("Is it worth using Day Tickets an entire month instead of Month Tickets?")
print(f"Price for Day Tickets lasting a month {dayTicket*30.42}kr. Price for Month Ticket: {monthTicket}kr. Is it worth using Day Tickets over Month Tickets? {dayTicket*30.42 < monthTicket}")


