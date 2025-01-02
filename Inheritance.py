#inheritance

class IPLTicket:
    def __init__(self, team1, team2, date, venue, price):
         self.team1=team1
         self.team2=team2
         self.date = date
         self.venue= venue
         self.price= price
    def display_ticket_info(self):
         print("Match:", self.team1, "vs",self.team2)
         print("Date:", self.date)
         print("venue:", self.venue)
         print("price:", self.price)
class VIPIPLTicket(IPLTicket):
    def __init__(self, team1, team2, date, venue, price, perks):
        self.team1=team1
        self.team2=team2
        self.date=date
        self.venue=venue
        self.price=price
        self.perks=perks
    def display_ticket_info(self):
        IPLTicket.display_ticket_info(self)
        print("VIP Perks:", self.perks)


ipl_ticket=IPLTicket("Mumbai Indians", "Chennai Super kings:", "2025-04-20", "Wankhede Stadium",2000)
vip_ipl_ticket=VIPIPLTicket("Mumabai Indians", "chennai super kings", "2025-04-20", "Wankhede Stadium:",7000, "Acess to VIP Lounge, Complimentry Snacks")

print("Regular Ticket:")
ipl_ticket.display_ticket_info()

print("\n VIP Ticket:")
vip_ipl_ticket.display_ticket_info()




#Data Abstarction

from abc import ABC, abstractmethod

class IPLTicket(ABC):
    def __init__(self, team1, team2, date, venue, price):
        self.team1 = team1
        self.team2 = team2
        self.date = date
        self.venue = venue
        self.price = price

    @abstractmethod
    def display_ticket_info(self):
        pass

class RegularIPLTicket(IPLTicket):
    def __init__(self, team1, team2, date, venue, price):
        self.team1 = team1
        self.team2 = team2
        self.date = date
        self.venue = venue
        self.price = price

    def display_ticket_info(self):
        print("Regular IPL Ticket Information:")
        print("Match:", self.team1, "vs", self.team2)
        print("Date:", self.date)
        print("Venue:", self.venue)
        print("Price:", self.price)

class VIPIPLTicket(IPLTicket):
    def __init__(self, team1, team2, date, venue, price, perks):
        self.team1 = team1
        self.team2 = team2
        self.date = date
        self.venue = venue
        self.price = price
        self.perks = perks

    def display_ticket_info(self):
        print("VIP IPL Ticket Information:") 
        print("Match:", self.team1, "vs", self.team2)
        print("Date:", self.date)
        print("Venue:", self.venue)
        print("Price:", self.price)
        print("VIP Perks:", self.perks)

# Create instances of different ticket types
regular_ticket = RegularIPLTicket("Mumbai Indians", "Chennai Super Kings", "2025-04-20", "Wankhede Stadium", 1500)
vip_ticket = VIPIPLTicket("Mumbai Indians", "Chennai Super Kings", "2025-04-20", "Wankhede Stadium", 5000, "Access to VIP Lounge, Complimentary Snacks and Dinner ")

# Display ticket information using abstraction
regular_ticket.display_ticket_info()
print()
vip_ticket.display_ticket_info()
