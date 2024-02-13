#include <iostream>
using namespace std;

int main()
{
    double sales = 95000;

    const double state_tax_rate = 0.04;
    double state_tax = sales * state_tax_rate;
    const double county_tax_rate = 0.02;
    double county_tax = sales * county_tax_rate;

    cout << "state tax " << state_tax << endl;
    cout << "county tax " << county_tax << endl;

    double total_tax = state_tax + county_tax;

    double total_sale = sales - total_tax;
    cout << "total sales " << total_sale << endl;
}