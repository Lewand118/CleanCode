public class TaxCalculator {
    private taxRates;
    public TaxCalculator(){
        taxRates = new TaxRates()
    }

	public static double calculateAdvanceTax(double income) {
		return income * taxRates.getAdvanceTaxRate();
	}

	public static double calculateSocialSecurityTax(double income) {
		return income * taxRates.getSocialTaxRate();
	}
    public static double calculateHealthSocialSecurityTax(double income) {
		return income * taxRates.getHealthTaxRate();
	}
    public static double calculateSicknessSocialSecurityTax(double income){
        return income * taxRates.getSicknessTaxRate();
    }

	public static double[] calculateOtherHealthTaxes(double income) {
		double[] healthTaxes=new double[2];
        healthTaxes[0] = income * taxRates.getFirstHealthTaxRate();
		healthTaxes[1] = income * taxRates.getSecondHealthTaxRate();
        return healthTaxes;
	}

    public static double calculateTaxDeductibleExpenses(Double income) {
        return income * taxRates.getDeducitableTaxRate();
    }

    public static double calculateTaxedIncome(Double income,double taxDeductibleExpenses ) {
        return income-taxDeductibleExpenses;
    }

    public static double calculateNetIncome(double income,double socialSecurityTax, double healthSocialSecurityTax,
            double sicknessSocialSecurityTax, double lowerSocialHealthTax, double advanceTax) {
        return income - ((socialSecurityTax + healthSocialSecurityTax + sicknessSocialSecurityTax) + lowerSocialHealthTax + advanceTax);
    }

}
