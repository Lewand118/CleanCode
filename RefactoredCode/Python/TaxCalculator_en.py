import re

class TaxCalculator(object):
    def __init__(self, social_security_rate=0.0976, social_security_health_rate=0.015, social_security_sickness_rate=0.0245,
                    deductible_expenses_rate=111.25, advance_rate_rate=0.18, reduced_tax_rate=46.33, health_lower_rate=0.0775, health_higher_rate=0.09) -> None:
        self.income = None
        self.type = None
        self.social_security_rate = social_security_rate
        self.social_security_health_rate = social_security_health_rate
        self.social_security_sickness_rate = social_security_sickness_rate
    
        self.deductible_expenses_rate = deductible_expenses_rate
        self.health = {'lower': health_lower_rate, 'higher': health_higher_rate}
        self.advance_rate = advance_rate_rate
        self.reduced_tax = reduced_tax_rate
        self.advance_tax = 0

    def print_rates(self):
        pass

    def get_input(self):
        try:
            self.income = float(input('Enter income: '))
            print('Enter contract type\nE - Employment\nC - Civil')
            self.type = input('Type: ').upper()
            if self.type != 'E' or self.type != 'C':
                raise ValueError('Incorrect contract type')
        except Exception as err:
            print(f'Error with data input: {str(err)}')  

    @staticmethod
    def round_tax(tax):
        try:
            tax_str = str(float(tax))
            dec_list = tax_str.split('.')[1]
            if len(dec_list) > 2 and not re.search('^\d{2}0*$', dec_list):
                dot_pos = tax_str.find('.')
                to_increment = int(tax_str[dot_pos+2]) + 1
                tax_str = tax_str[:dot_pos+2] + str(to_increment)
                tax = float(tax_str)
        except Exception as err:
            print(f'Error with rounding tax: {str(err)}')  
        
        return float(tax)

    def social_security_taxes(self, income):
        # income = self.income
        social_security = self.round_tax(income*self.social_security_rate)
        social_security_health = self.round_tax(income*self.social_security_health_rate)
        social_security_sickness = self.round_tax(income*self.social_security_sickness_rate)
        all_social_taxes = social_security+social_security_health+social_security_sickness

        return {'social_security': social_security, 'social_security_health': social_security_health, 'social_security_sickness': social_security_sickness, 'sum': all_social_taxes}


    def health_security_tax(self, income):
        income_base = income - self.social_security_taxes(income)['sum']
        health_tax_lower = self.round_tax(income_base*self.health['lower'])
        health_tax_higher = self.round_tax(income_base*self.health['higher'])

        return {'health_tax_lower': health_tax_lower, 'health_tax_higher': health_tax_higher}


    def calculate_advance_tax(self, income):
        income = self.income
        pass
    









def main():
    taxObj = TaxCalculator()
    taxObj.get_input()
    
    x = taxObj.social_security_taxes(111)

    print(x)
    r = taxObj.round_tax(3.1101)
    print(r)

    y = taxObj.health_security_tax(100)
    print(y)


if __name__ == '__main__':
    main()