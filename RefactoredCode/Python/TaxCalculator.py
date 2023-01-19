import re

from RefactoredCode.Python.ContractType import ContractType


class TaxCalculator:
    def __init__(self, income: float, contract_type: ContractType,
                 social_security_rate=0.0976,
                 social_security_health_rate=0.015,
                 social_security_sickness_rate=0.0245, deductible_expenses_rate=111.25,
                 deductible_expenses_rate_civil=0.2, advance_rate_rate=0.18, reduced_tax_rate=46.33,
                 health_lower_rate=0.0775, health_higher_rate=0.09) -> None:
        self.income = income
        self.contract_type = contract_type

        self.social_security_rate = social_security_rate
        self.social_security_health_rate = social_security_health_rate
        self.social_security_sickness_rate = social_security_sickness_rate

        self.deductible_expenses_rate = deductible_expenses_rate
        self.deductible_expenses_rate_civil = deductible_expenses_rate_civil
        self.health_rate = {'lower': health_lower_rate, 'higher': health_higher_rate}
        self.advance_rate = advance_rate_rate
        self.reduced_tax_rate = reduced_tax_rate

    @staticmethod
    def round_tax(tax):
        tax_str = str(float(tax))
        dec_list = tax_str.split('.')[1]
        if len(dec_list) > 2 and not re.search('^\d{2}0*$', dec_list):
            dot_pos = tax_str.find('.')
            to_increment = int(tax_str[dot_pos + 2]) + 1
            tax_str = tax_str[:dot_pos + 2] + str(to_increment)
            tax = float(tax_str)
        return float(tax)

    def calculate_social_taxes(self):
        social_security = self.round_tax(self.income * self.social_security_rate)
        social_security_health = self.round_tax(self.income * self.social_security_health_rate)
        social_security_sickness = self.round_tax(self.income * self.social_security_sickness_rate)
        all_social_taxes = sum([social_security, social_security_health, social_security_sickness])

        return {social_security: social_security,
                social_security_health: social_security_health,
                social_security_sickness: social_security_sickness,
                sum: all_social_taxes}

    def calculate_income_base(self, social_tax_sum):
        income_base = self.round_tax(self.income - social_tax_sum)

        return income_base

    def calculate_health_tax(self, income: float, is_base=False):
        income_base = income - self.calculate_social_taxes['sum'] if not is_base else income
        lower = self.round_tax(income_base * self.health_rate['lower'])
        higher = self.round_tax(income_base * self.health_rate['higher'])

        return {lower, higher}

    def calculate_deductible_expenses(self, income_base: float):
        if self.contract_type == ContractType.EMPLOYMENT:
            deductible_expenses = self.deductible_expenses_rate
        else:
            deductible_expenses = income_base * self.deductible_expenses_rate_civil

        rounded_deductible_expenses = self.round_tax(deductible_expenses)

        return rounded_deductible_expenses

    def calculate_advance_tax(self, income: float):
        income_base = self.round_tax(income)
        advanced = self.round_tax(income_base * self.advance_rate)

        return advanced

    def calculate_reduce_tax(self, income_base: float, advance_tax: float):
        if self.contract_type != ContractType.EMPLOYMENT:
            return advance_tax

        return self.calculate_advance_tax(income_base) - self.reduced_tax_rate

    def calculate_advance_tax_paid(self, advance_tax: float, health_tax_lower: float):
        if self.contract_type == ContractType.EMPLOYMENT:
            advance_paid = health_tax_lower - self.reduced_tax_rate
        else:
            advance_paid = advance_tax - health_tax_lower

        return self.round_tax(advance_paid)

    def calculate_taxed_income(self, social_taxes_sum: float, deductible_expenses: float):
        return self.round_tax(self.income - social_taxes_sum - deductible_expenses)

    def calculate_net_income(self, social_taxes_sum: float, deductible_expenses: float):
        health_tax_higher = self.calculate_health_tax(self.income)['higher']

        advance_tax = self.calculate_advance_tax(self.income - social_taxes_sum - deductible_expenses)

        if self.contract_type == ContractType.EMPLOYMENT:
            advance_tax -= (health_tax_higher + self.reduced_tax_rate)
        else:
            advance_tax -= health_tax_higher

        net_income = self.income - social_taxes_sum - health_tax_higher - advance_tax

        return self.round_tax(net_income)

    def calculate_all_taxes(self):
        social_taxes = self.calculate_social_taxes()
        income_base = self.calculate_income_base(social_taxes['sum'])
        health_tax = self.calculate_health_tax(income_base, is_base=True)
        deductible_expenses = self.calculate_deductible_expenses(income_base)
        advance_tax = self.calculate_advance_tax(income_base - deductible_expenses)
        reduce_tax = self.calculate_reduce_tax(income_base, advance_tax)
        advance_paid = self.calculate_advance_tax_paid(advance_tax, health_tax['lower'])
        taxed_income = self.calculate_taxed_income(social_taxes['sum'], deductible_expenses)
        net_income = self.calculate_net_income(social_taxes['sum'], deductible_expenses)

        return {
            social_taxes,
            income_base,
            health_tax,
            deductible_expenses,
            advance_tax,
            reduce_tax,
            advance_paid,
            taxed_income,
            net_income
        }

    def get_all_rates(self):
        return {
            'social_security_rate': self.social_security_rate,
            'social_security_health_rate': self.social_security_health_rate,
            'social_security_sickness_rate': self.social_security_sickness_rate,
            'deductible_expenses_rate': self.deductible_expenses_rate,
            'deductible_expenses_rate_civil': self.deductible_expenses_rate_civil,
            'health_rate': self.health_rate,
            'advance_rate': self.advance_rate,
            'reduced_tax_rate': self.reduced_tax_rate
        }
