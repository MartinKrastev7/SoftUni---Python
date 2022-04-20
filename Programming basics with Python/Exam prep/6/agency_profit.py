fly_company = input()
adult_tickets_number = int(input())
kids_tickets_number = int(input())
net_price_ticket_adult = float(input())
tax_service_price = float(input())

net_price_ticket_kids = net_price_ticket_adult * 0.3
ticket_adult_tax_service = net_price_ticket_adult + tax_service_price
ticket_kids_tax_service = net_price_ticket_kids + tax_service_price
total_price_tickets = (adult_tickets_number * ticket_adult_tax_service) + (kids_tickets_number * ticket_kids_tax_service)
profit = total_price_tickets * 0.2

print(f"The profit of your agency from {fly_company} tickets is {profit:.2f} lv.")