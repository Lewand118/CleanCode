public class TaxCalculator {
    public TaxCalculator(){
        
    }

	public static double calculateAdvanceTax(double income) {
		return (income * 18) / 100;
	}

	public static double calculateSocialSecurityTax(double income) {
		return (income * 9.76) / 100;
	}
    public static double calculateHealthSocialSecurityTax(double income) {
		return (income * 1.5) / 100;
	}
    public static double calculateSicknessSocialSecurityTax(double income){
        return (income * 1.5) / 100;

    }

	public static double[] calculateOtherHealthTaxes(double income) {
		double[] healthTaxes=new double[2];
        healthTaxes[0] = (income * 9) / 100;
		healthTaxes[1] = (income * 7.75) / 100;
        return healthTaxes;
	}

    public static double calculateTaxDeductibleExpenses(Double income) {
        return (income*20)/100;
    }

    public static double calculateTaxedIncome(Double income,double taxDeductibleExpenses ) {
        return income-taxDeductibleExpenses;
    }

    public static double calculateNetIncome(double income,double socialSecurityTax, double healthSocialSecurityTax,
            double sicknessSocialSecurityTax, double lowerSocialHealthTax, double advanceTax) {
        return income - ((socialSecurityTax + healthSocialSecurityTax + sicknessSocialSecurityTax) + lowerSocialHealthTax + advanceTax);
    }

}
