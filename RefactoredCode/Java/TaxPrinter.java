import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.text.DecimalFormat;
import java.math.BigDecimal;
import java.math.RoundingMode;
public class TaxPrinter {
    InputStreamReader inputStreamReader;
    BufferedReader bufferedReader;
    public TaxPrinter(){
        inputStreamReader = new InputStreamReader(System.in);
		bufferedReader = new BufferedReader(inputStreamReader);
    }

    public Double askForIncome() {
        System.out.print("Enter income: ");
		try{
        return Double.parseDouble(bufferedReader.readLine());
    }
    catch (Exception ex) {
        System.out.println("Incorrect income");
        System.err.println(ex);
        System.exit(0);
        return -1.0;
    }
    }

    public char askForContract() {
        System.out.print("Contract Type: (E)mployment, (C)ivil: ");
		try{
        return bufferedReader.readLine().charAt(0);
        }
        catch (Exception ex) {
            System.out.println("Incorrect contract type");
            System.err.println(ex);
            System.exit(0);
            return 'x';
        }

    }

    public void printBasicData(char contractType, Double income) {
        switch(contractType){
            case 'E':
                System.out.println("EMPLOYMENT");
                break;
            case 'C':
                System.out.println("CIVIL");
                break;
            default:
                System.out.println("Unknown type of contract!");
                break;
        }
        System.out.println("Income " + income);
    
    }

    public void printSocialSecurityTaxes(double socialSecurityTax, double healthSocialSecurityTax,
            double sicknessSocialSecurityTax) {
                System.out.println("Social security tax = "
                + Double.toString(round(socialSecurityTax,2)));
        System.out.println("Health social security tax = "
                + Double.toString(round(healthSocialSecurityTax,2)));
        System.out.println("Sickness social security tax = "
                + Double.toString(round(sicknessSocialSecurityTax,2)));       
    }

    public void printHealthSecurityTax(double[] healthTaxes) {
        System.out.println("Health social security tax: 9% = "
					+ Double.toString(round(healthTaxes[0],2)) + " 7,75% = " + Double.toString(round(healthTaxes[1],2)));
    }

    public void printTaxDeductibleAndTaxedIncome(double taxDeductibleExpenses, Double taxedIncome) {
        System.out.println("Tax deductible expenses "
					+ Double.toString(round(taxDeductibleExpenses,2)));
                    System.out.println("taxed income " + round(taxedIncome,2));
    }

    public void printAdvanceTax(double advanceTax) {
        System.out.println("Advance tax 18 % = " + round(advanceTax,2));
    }

    public void printNetIncome(double netIncome) {
        System.out.println("Net income = "+ Double.toString(round(netIncome,2)));
    }
    public static double round(double value, int places) {
        if (places < 0) throw new IllegalArgumentException();
    
        BigDecimal bd = BigDecimal.valueOf(value);
        bd = bd.setScale(places, RoundingMode.HALF_UP);
        return bd.doubleValue();
    }
}


