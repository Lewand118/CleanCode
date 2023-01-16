from operator import attrgetter
from RefactoredCode.Python.TaxCalculator import TaxCalculator
from RefactoredCode.Python.ContractType import ContractType


class UserInterface:
    income: float = None
    contract_type: ContractType = None

    def read_user_data(self):
        try:
            self.income = float(input('Enter income: '))

            print('Enter contract type\n'
                  'E - Employment\n'
                  'C - Civil')

            contract_type_value = input('Type: ').upper()
            self.contract_type = ContractType[contract_type_value]

        except KeyError:
            print('Incorrect contract type')

        except Exception as err:
            print(f'Error with data input {str(err)}')

    def print_user_taxes(self):
        if self.income is None or self.contract_type is None:
            print('No contract type or income provided')
            return

        tax_calculator = TaxCalculator(self.income, self.contract_type)

        contract_type_name = self.contract_type.name

        social_taxes, income_base, health_tax, \
            deductible_expenses, advance_tax, \
            reduce_tax, advance_paid, taxed_income, \
            net_income = tax_calculator.calculate_all_taxes()

        all_rates = tax_calculator.get_all_rates()

        social_security_rate, \
            social_security_health_rate, \
            social_security_sickness_rate, \
            health_rate, \
            advance_rate, \
            reduced_tax_rate = attrgetter(
            'social_security_rate', 'social_security_health_rate', 'social_security_sickness_rate', 'health_rate',
            'advance_rate', 'reduced_tax_rate')(all_rates)

        advance_tax_free_income_text = ''
        if self.contract_type == ContractType.EMPLOYMENT:
            advance_tax_free_income_text = f'\nTax free income = {reduced_tax_rate}'

        print(f'''
            {contract_type_name}
            Income: {self.income}
            Social security tax: {social_security_rate * 100}%
            Health social security tax: {social_security_health_rate * 100}%
            Sickness social security tax: {social_security_sickness_rate * 100}%
            Income basis for health social security: {income_base}
            Health social security tax: {health_rate['higher'] * 100}% = {health_tax['higher']} {health_rate['lower'] * 100}% = {health_tax['lower']}
            Tax deductible expenses: {deductible_expenses}
            Income to be taxed: {taxed_income}  rounded: {round(taxed_income)}
            Advance tax: {advance_rate * 100}% = {advance_tax}{advance_tax_free_income_text}
            Reduced tax (already paid) = {reduce_tax}
            Advance paid tax = {advance_paid} rounded: {round(advance_paid)}\n
            Net income = {net_income}
            ''')
