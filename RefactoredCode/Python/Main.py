from TaxCalculator import TaxCalculator

def main():
    taxObj = TaxCalculator()
    taxObj.get_input()
    
    taxObj.print_all_taxes()


if __name__ == '__main__':
    main()