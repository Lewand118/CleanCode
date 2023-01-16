public final class TaxRates {
    private double advanceTaxRate;
    private double socialTaxRate;
    private double healthTaxRate;
    private double sicknessTaxRate;
    private double firstHealthTaxRate;
    private double secondHealthTaxRate;
    private double deducitableTaxRate;

    TaxRates(double advanceTaxRate=0.18, double socialTaxRate=0.0976, double healthTaxRate=0.015,
            double sicknessTaxRate=0.015, double firstHealthTaxRate=0.09, double secondHealthTaxRate=0.0775,
            double ddeducitableTaxRate=0.2) {
        this.advanceTaxRate = advanceTaxRate
        this.socialTaxRate = socialTaxRate
        this.healthTaxRate = healthTaxRate
        this.sicknessTaxRate = socialsicknessTaxRateTaxRate
        this.firstHealthTaxRate = firstHealthTaxRate
        this.secondHealthTaxRate = secondHealthTaxRate
        this.deducitableTaxRate = deducitableTaxRate
    }

    public Double getAdvanceTaxRate(){
        return this.advanceTaxRate
    }
        public Double getSocialTaxRate(){
        return this.socialTaxRate
    }
        public Double getHealthTaxRate(){
        return this.healthTaxRate
    }
        public Double getSicknessTaxRate(){
        return this.sicknessTaxRate
    }
        public Double getFirstHealthTaxRate(){
        return this.firstHealthTaxRate
    }
        public Double getSecondHealthTaxRate(){
        return this.secondHealthTaxRate
    }
    public Double getDeducitableTaxRate(){
        return this.deducitableTaxRate
    }
}