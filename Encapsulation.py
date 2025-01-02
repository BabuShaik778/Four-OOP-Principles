# encapsulation

class IPLTicket:
    def __init__(self,team1, team2, venue, match_date, price):
        self.team1=team1
        self.team2=team2
        self.venue=venue
        self.match_date=match_date
        self.price=price
    def get_team1(self):
        return self.team1

    def set_team1(self,team1):
        self.team1 = team1
    def get_team2(self):
        return self.team2

    def set_team2(self,team2):
         self.team2=team2
    def get_venue(self):
        return self.venue
    def set_venue(self, venue):
        self.venue=venue
    def get_match_date(self):
        return self.match_date

    def set_match_date(self, match_date):
        self.match_date=match_date
    def get_price(self):
        return self.price
    def set_price(self, price):
        self.price=price


ipl_ticket = IPLTicket("Mumbai Indians", "Chennai super kings", "Chidambaram stadium", "2024-03-07", 1700)

print("Team1:", ipl_ticket.get_team1())
print("Team2:", ipl_ticket.get_team2())
print("venue:", ipl_ticket.get_venue())
print("Match_date:", ipl_ticket.get_match_date())
print("Ticket price:", ipl_ticket.get_price())

ipl_ticket.set_price(2000)
ipl_ticket.set_venue("Eden gardens")

print("Modified Venue:", ipl_ticket.get_venue())
print("Modified Ticket Price:",ipl_ticket.get_price())
