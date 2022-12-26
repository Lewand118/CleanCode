import re

class TaxCalculator(object):
    """
    Given the not precisely defined context of this class (the base class from Code Smells) in the design and its broader intent, the code is architecturally suboptimal. 
    Depending on the context, the current methods could be written differently.
    However, the goal was only to eliminate CodeSmells in a single class and to provide generic approach to allow extensions in different directions.
    Calculation logic in the output program is wrong, but it was not the task to correct the logic itself.
    """
    def __init__(self, social_security_rate=0.0976, social_security_health_rate=0.015, social_security_sickness_rate=0.0245, deductible_expenses_rate=111.25,
                deductible_expenses_rate_civil=0.2, advance_rate_rate=0.18, reduced_tax_rate=46.33, health_lower_rate=0.0775, health_higher_rate=0.09) -> None:
        self.income = None
        self.type = None
        self.social_security_rate = social_security_rate
        self.social_security_health_rate = social_security_health_rate
        self.social_security_sickness_rate = social_security_sickness_rate
    
        self.deductible_expenses_rate = deductible_expenses_rate
        self.deductible_expenses_rate_civil = deductible_expenses_rate_civil
        self.health = {'lower': health_lower_rate, 'higher': health_higher_rate}
        self.advance_rate = advance_rate_rate
        self.reduced_tax_rate = reduced_tax_rate

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
        try:
            social_security = self.round_tax(income*self.social_security_rate)
            social_security_health = self.round_tax(income*self.social_security_health_rate)
            social_security_sickness = self.round_tax(income*self.social_security_sickness_rate)
            all_social_taxes = sum([social_security,social_security_health,social_security_sickness])
        except Exception as err:
            print(f'Error with social security taxes: {str(err)}') 

        return {'social_security': social_security, 'social_security_health': social_security_health, 'social_security_sickness': social_security_sickness, 'sum': all_social_taxes}

    def health_security_tax(self, income, is_base=False):
        try:
            income_base = income-self.social_security_taxes(income)['sum'] if not is_base else income
            health_tax_lower = self.round_tax(income_base*self.health['lower'])
            health_tax_higher = self.round_tax(income_base*self.health['higher'])
        except Exception as err:
            print(f'Error with health security taxes: {str(err)}') 
        

        return {'health_tax_lower': health_tax_lower, 'health_tax_higher': health_tax_higher}

    def advance_tax(self, income_base):
        try: 
            income_base = self.round_tax(income_base)
            advanced = self.round_tax(income_base*self.advance_rate)
        except Exception as err:
            print(f'Error with advance tax: {str(err)}') 
        return advanced

    def reduce_tax(self, income_base):
        try:
            reduced = self.advance_tax(income_base)-self.reduced_tax_rate if self.type == 'E' else self.advance_tax(income_base)
        except Exception as err:
            print(f'Error with reduce tax: {str(err)}') 
        return reduced

    def calculate_net_income(self, deductible_expenses):
        try:
            social_taxes = self.social_security_taxes(self.income)['sum']
            health_tax = self.health_security_tax(self.income)['health_tax_higher']
            advance = self.advance_tax(self.income-social_taxes-deductible_expenses)
            advance -= (health_tax + self.reduced_tax_rate) if self.type == 'E' else health_tax
            net_income = self.income - social_taxes - health_tax - advance
        except Exception as err:
            print(f'Error with net income calculation: {str(err)}') 

        return self.round_tax(net_income)

    def print_all_taxes(self):
        try:
            print_type = 'EMPLOYMENT' if self.type == 'E' else 'CIVIL'
            
            social_taxes = self.social_security_taxes(self.income)
            income_base = self.round_tax(self.income-social_taxes['sum'])
            health_tax = self.health_security_tax(income_base, is_base=True)
            deductible_expenses = self.deductible_expenses_rate if self.type == 'E' else income_base*self.deductible_expenses_rate_civil
            deductible_expenses = self.round_tax(deductible_expenses)
            advanced = self.advance_tax(income_base-deductible_expenses)
            reduced = self.reduce_tax(advanced) if type == 'E' else advanced
            adnance_paid = advanced-health_tax['health_tax_lower']-self.reduced_tax_rate if self.type == 'E' else advanced-health_tax['health_tax_lower']
            adnance_paid = self.round_tax(adnance_paid)
            taxed_income = self.round_tax(self.income-social_taxes['sum']-deductible_expenses)
            net_income = self.calculate_net_income(deductible_expenses)

            type_dependent_text = f'\nTax free income = {self.reduced_tax_rate}' if self.type == 'E' else ''
        except Exception as err:
            print(f'Error with printing: {str(err)}') 

        print(f'''
{print_type}
Income: {self.income}
Social security tax: {self.social_security_rate*100}%
Health social security tax: {self.social_security_health_rate*100}%
Sickness social security tax: {self.social_security_sickness_rate*100}%
Income basis for health social security: {income_base}
Health social security tax: {self.health['higher']*100}% = {health_tax['health_tax_higher']} {self.health['lower']*100}% = {health_tax['health_tax_lower']}
Tax deductible expenses: {deductible_expenses}
Income to be taxed: {taxed_income}  rounded: {round(taxed_income)}
Advance tax: {self.advance_rate*100}% = {advanced}{type_dependent_text}
Reduced tax (already paid) = {reduced}
Advance paid tax = {adnance_paid} rounded: {round(adnance_paid)}\n
Net income = {net_income}''')