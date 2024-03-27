service_tickets = {
    "Ticket001": {"Customer": "Alice", 
                  "Issue": "Login problem", 
                  "Status": "open"},
    "Ticket002": {"Customer": "Bob",
                  "Issue": "Payment issue", 
                  "Status": "closed"}
}
count = 2

def new_ticket(ticket_number, customer_name, issue):
    service_tickets.update({ticket_number: {"Customer": customer_name, "Issue": issue, "Status": "open"}})

new_ticket("Ticket003", "Charlie", "Website down")

# print(service_tickets)

def update_status (ticket_number, status):
    service_tickets[ticket_number]["Status"] = status
    
update_status("Ticket003", "closed")

# print(service_tickets)

def print_tickets():
    for ticket, info in service_tickets.items():
        print(f"Ticket {ticket} is {info['Status']} and is about {info['Issue']} and is reported by {info['Customer']}")
        
print_tickets()