from TaxCalculator import TaxCalculator


def main():
    tax_calc = TaxCalculator()

    tax_calc.get_input()
    tax_calc.print_all_taxes()


if __name__ == '__main__':
    main()
