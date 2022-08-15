class TicketBookingForm:
    def information(self, name, phn, adds):
        self.name = name
        self.phn = phn
        self.adds = adds

    def info_print(self):
        print(f'Hello {self.name} ,your ticket is confirmed with address {self.adds} and confirmation is sent to {self.phn}')



puja = TicketBookingForm()
puja.information('Sradhanjali Nayak',9899,'Motto')

sambit=TicketBookingForm()
sambit.information('Sambit Behera',8888,'chandbali')

raj=TicketBookingForm()
raj.information('Raj Kapoor',0000,'Mumbai')


shidarth=TicketBookingForm()
# shidarth.info_print()

puja.info_print()
sambit.info_print()

