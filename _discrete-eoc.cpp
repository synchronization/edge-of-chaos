#include <iostream>
#include <vector>

using namespace std;

int main ()
{
    double x = 0.38;
    std::vector<double> xs;
    xs.push_back(0.38);

    double a = 3.8;
    std::vector<double> as;

    double r = 0.0;//0.005;

    if (a > 0) {
        as.push_back(a);
    }
    else {
        as.push_back(0.38);
    };

    for (int n = 0; n < 10; n++) {
        cout << "----------\n";
        cout << "1: x == " << x << "\n";

        double f = x;

        cout << "2: f == " << f << "\n";

        for (int k = 1; k <= 32; k++) {
            x = as[n] * x * (1 - x);
            cout << "m: x == " << x << "\n";
        }
        //        x = x + (rand() - 0.5) * r;

        cout << "3: x == " << x << "\n";

        if (x > 1) { x = 0.999; }
        if (x < 0) { x = 0.001; }

        f = f - x;
        //        xs[n] = x;
        //        as[n+1] = as[n] + 0.1 * f;
        xs.push_back(x);
        as.push_back(as[n] + 0.1 * f);

        if (as[n+1] < 0) {
            as[n+1] = 0;
        };
        if (as[n+1] > 4) {
            as[n+1] = 4;
        }

        for (int k = 1; k < 32; k++) {
            x = as[n] * x * (1 - x);
        }
    }

    return 0;
}
