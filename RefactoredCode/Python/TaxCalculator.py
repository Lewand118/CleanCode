import re
from math import ceil

class TaxCalculator(object):
    """
    Given the not precisely defined context of this class (the base class from Code Smells) in the design and its broader intent, the code is architecturally suboptimal. 
    Depending on the context, the current methods could be written differently.
    However, the goal was only to eliminate CodeSmells in a single class and to provide generic approach to allow extensions in different directions
    """
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
        self.reduced_tax_rate = reduced_tax_rate
        self.advance_tax = 0

    def print_rates(self):
        pass

    def get_input(self):
        try:
            self.income = float(input('Enter income: '))
            print('Enter contract type\nE - Employment\nC - Civil')
            self.type = input('Type: ').upper()
            if self.type != 'E' and self.type != 'C':
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
        social_security = self.round_tax(income*self.social_security_rate)
        social_security_health = self.round_tax(income*self.social_security_health_rate)
        social_security_sickness = self.round_tax(income*self.social_security_sickness_rate)
        all_social_taxes = sum([social_security,social_security_health,social_security_sickness])
        print(f'social: {all_social_taxes}')
        return {'social_security': social_security, 'social_security_health': social_security_health, 'social_security_sickness': social_security_sickness, 'sum': all_social_taxes}

    def health_security_tax(self, income, is_base=False):
        income_base = income-self.social_security_taxes(income)['sum'] if not is_base else income
        health_tax_lower = self.round_tax(income_base*self.health['lower'])
        health_tax_higher = self.round_tax(income_base*self.health['higher'])

        return {'health_tax_lower': health_tax_lower, 'health_tax_higher': health_tax_higher}

    def advance_tax(self, income):
        print(f'advance: {income}')
        return self.round_tax(income*(self.advance_rate))

    def reduce_tax(self, income):
        reduced = self.advance_tax(income) - self.reduced_tax_rate
        return reduced

    def calculate_net_income(self):
        social_taxes = self.social_security_taxes(self.income)['sum']
        health_tax = self.health_security_tax(self.income)['health_tax_lower']
        advance = 0#advance(self.income)
        net_income = self.income - social_taxes - health_tax - advance

        return net_income

    def print_all_taxes(self):
        social_taxes = self.social_security_taxes(self.income)
        income_base = self.round_tax(self.income-social_taxes['sum'])
        health_tax = self.health_security_tax(income_base, is_base=True)
        advanced = 0#self.advance_tax(self.income)
        reduced = 0#self.reduce_tax(self.income)
        adnance_paid = advanced - health_tax['health_tax_lower'] - reduced
        taxed_income = self.round_tax(self.income-social_taxes['sum']-self.deductible_expenses_rate)
        net_income = self.calculate_net_income()

        print(f'''Income: {self.income}\n
                Social security tax: {self.social_security_rate*100}%\n
                Health social security tax: {self.social_security_health_rate*100}%\n
                Sickness social security tax: {self.social_security_sickness_rate*100}%\n
                Income basis for health social security: {income_base}\n
                Health social security tax: {self.health['higher']*100}% = {health_tax['health_tax_higher']} {self.health['lower']*100}% = {health_tax['health_tax_lower']}\n
                Tax deductible expenses: {self.deductible_expenses_rate}\n
                Income: {taxed_income}  rounded {ceil(taxed_income)}\n
                Advance tax: {self.advance_rate*100}% = {advanced}\n
                Tax free income = {self.reduced_tax_rate}\n
                Reduced tax = {reduced}\n
                Advance paid tax = {adnance_paid} rounded {ceil(adnance_paid)}\n
                
                Net income = {net_income}'''
            )