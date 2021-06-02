class CompanyPicks:
    def __init__(self):
        self.selection = None

    def setSelection(self, value):
        self.selection = value

    def getSelection(self):
        return self.selection


def calculate_revenue(company, revenue, picks, launch):
    if int(revenue) == 30:
        if company.revenue < int(revenue):
            if (launch == 2017 and company.launch_year >= launch) or \
                    (launch == 2015 and launch <= company.launch_year < 2017)\
                    or (launch == 2011 and launch <= company.launch_year < 2015):
                picks.append(company)
    elif int(revenue) == 70:
        if 30 < company.revenue < int(revenue):
            if (launch == 2017 and company.launch_year >= launch) or \
                    (launch == 2015 and launch <= company.launch_year < 2017) \
                    or (launch == 2011 and launch <= company.launch_year < 2015):
                picks.append(company)
    elif int(revenue) == 300:
        if 70 < company.revenue < int(revenue):
            if (launch == 2017 and company.launch_year >= launch) or \
                    (launch == 2015 and launch <= company.launch_year < 2017) \
                    or (launch == 2011 and launch <= company.launch_year < 2015):
                picks.append(company)
