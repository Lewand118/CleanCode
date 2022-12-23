import re

class TaxCalculator(object):
    def __init__(self, income=0, social_security_rate=0.0976, social_security_health_rate=0.015, social_security_sickness_rate=0.0245) -> None:
        self.income = income
        self.social_security_rate = social_security_rate
        self.social_security_health_rate = social_security_health_rate
        self.social_security_sickness_rate = social_security_sickness_rate
    
        self.deductible_expenses = 111.25
        self.health = {'lower': 0.775, 'higher': 0.09}
        self.advance_rate = 0.18
        self.reduced_tax = 46.33 # tax free income 46,33 PLN
        self.advance_tax = 0

    @staticmethod
    def round_tax(tax):
        tax_str = str(float(tax))
        dec_list = tax_str.split('.')[1]
        if len(dec_list) > 2 and not re.search('^\d{2}0*$', dec_list):
            dot_pos = tax_str.find('.')
            to_increment = int(tax_str[dot_pos+2]) + 1
            tax_str = tax_str[:dot_pos+2] + str(to_increment)
            tax = float(tax_str)
        
        return float(tax)

    # returns three taxes: social security, social security health, social security sickness
    def social_security_taxes(self):
        income = self.income
        social_security = income*self.social_security_rate
        social_security_health = income*self.social_security_health_rate
        social_security_sickness = income*self.social_security_sickness_rate

        return {'social_security': self.round_tax(social_security), 'social_security_health': self.round_tax(social_security_health), 'social_security_sickness': self.round_tax(social_security_sickness)}


    def calculate_advance_tax(self, income):
        income = self.income
        pass
    









def main():
    taxObj = TaxCalculator(income=1111)
    x = taxObj.social_security_taxes()
    print(x)
    r = taxObj.round_tax(3.110)
    print(r)


if __name__ == '__main__':
    main()