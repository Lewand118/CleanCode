
public class TaxManager {
    Double income;
    char contractType;
    TaxCalculator taxCalculator;
    TaxPrinter taxPrinter;
    public TaxManager(){
        taxCalculator=new TaxCalculator();
        taxPrinter=new TaxPrinter();	
    }

    public void calculateTaxes(){
        askForData();
        
        double socialSecurityTax,healthSocialSecurityTax,sicknessSocialSecurityTax;

        socialSecurityTax=TaxCalculator.calculateSicknessSocialSecurityTax(income);
        healthSocialSecurityTax=TaxCalculator.calculateHealthSocialSecurityTax(income);
        sicknessSocialSecurityTax=TaxCalculator.calculateSicknessSocialSecurityTax(income);


        double[] healthTaxes=TaxCalculator.calculateOtherHealthTaxes(income);
        double taxDeductibleExpenses = TaxCalculator.calculateTaxDeductibleExpenses(income);
        double taxedIncome= TaxCalculator.calculateTaxedIncome(income, taxDeductibleExpenses);
        double advanceTax=TaxCalculator.calculateAdvanceTax(income);
        double netIncome=TaxCalculator.calculateNetIncome(income,socialSecurityTax,healthSocialSecurityTax,sicknessSocialSecurityTax,healthTaxes[0],advanceTax);

        taxPrinter.printBasicData(contractType,income);
        taxPrinter.printSocialSecurityTaxes(socialSecurityTax,healthSocialSecurityTax,sicknessSocialSecurityTax);
        taxPrinter.printHealthSecurityTax(healthTaxes);
        taxPrinter.printTaxDeductibleAndTaxedIncome(taxDeductibleExpenses,taxedIncome);
        taxPrinter.printAdvanceTax(advanceTax);
        taxPrinter.printNetIncome(netIncome);
    }
    private void askForData(){
        income=taxPrinter.askForIncome();
		contractType=taxPrinter.askForContract();
    }
}
