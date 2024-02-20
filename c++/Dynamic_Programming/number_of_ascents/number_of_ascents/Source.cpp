#include <iostream>

using namespace std;

int main()
{
	int d[1000][10];
	int n;

	cin >> n;

	for (int i = 0; i < 10; i++)
	{
		d[0][i] = 1;
	}

	for (int i = 1; i < n; i++)
	{
		for (int j = 0; j <= 9; j++)
		{
			int t_sum = 0;
			for (int k = 0; k <= j; k++)
			{
				t_sum += d[i - 1][k];
			}
			d[i][j] = t_sum%10007;
		}
	}

	int sum = 0;

	for (int i = 0; i <= 9; i++)
	{
		sum += d[n - 1][i];
	}

	cout << sum % 10007;
	return 0;
}