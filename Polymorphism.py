#polymorphism

class IPLTicket:
    def __init__(self, team1, team2, venue, match_date, price):
        self.team1=team1
        self.team2=team2
        self.venue=venue
        self.match_date=match_date
        self.price=price

    def display_ticket_info(self):
        print("IPL Ticket Information:")
        print("Team1:",self.team1)
        print("Team2:",self.team2)
        print("venue:",self.venue)
        print("Match_date:",self.match_date)
        print("Ticket price:",self.price)
class ConcertTicket(IPLTicket):
    def __init__(self, artist, venue, concert_date, price):
        IPLTicket.__init__(self, None, None, venue, concert_date, price)
        self.artist=artist

    def display_ticket_info(self):
        print("Concert Ticket Information:")
        print("Artist:",self.artist)
        print("Venue:", self.venue)
        print("Concert Date:", self.match_date)  # Using match_date from parent class
        print("Ticket Price:", self.price)

def display_ticket_information(ticket):
    ticket.display_ticket_info()


ipl_ticket = IPLTicket("Mumbai Indians", "Chennai Super Kings", "Wankhede Stadium", "2024-04-20", 5000)
concert_ticket = ConcertTicket("Arjit singh", "Navi Mumbai Arena", "2024-06-15", 7700 )



display_ticket_information(ipl_ticket)

print()
display_ticket_information(concert_ticket)


