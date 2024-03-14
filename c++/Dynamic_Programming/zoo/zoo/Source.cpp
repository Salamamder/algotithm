#include <iostream>

using namespace std;

int main()
{
	int d[100000][3];
	int n;
	int x[100000][3];

	cin >> n;

	x[0][0] = 1;
	x[0][1] = 1;
	x[0][2] = 1;

	for (int i = 1; i < n; i++)
	{
		x[i][0] = (x[i - 1][0] + x[i - 1][1] + x[i - 1][2])%9901;
		x[i][1] = (x[i - 1][0] + x[i - 1][2])%9901;
		x[i][2] = (x[i - 1][0] + x[i - 1][1])%9901;
	}

	cout << (x[n - 1][0] + x[n - 1][1] + x[n - 1][2])%9901;
	return 0;
}