#include <iostream>

using namespace std;

int main()
{
	int ite;
	int n;

	cin >> ite;
	while (ite--)
	{
		cin >> n;
		int d[100000][3];
		int cost[100000][2];
		for (int i = 0; i < 2; i++)
		{
			for (int j = 0; j < n; j++)
			{
				cin >> cost[j][i];
			}
		}

		d[0][0] = 0;
		d[0][1] = cost[0][0];
		d[0][2] = cost[0][1];

		for (int i = 1; i < n; i++)
		{
			int tmp_max;
			if (d[i - 1][1] > d[i - 1][2])
				tmp_max = d[i - 1][1];
			else
				tmp_max = d[i - 1][2];

			if (d[i - 1][0] > tmp_max)
				d[i][0] = d[i - 1][0];
			else
				d[i][0] = tmp_max;

			if (d[i - 1][0] > d[i - 1][2])
				d[i][1] = d[i - 1][0] + cost[i][0];
			else
				d[i][1] = d[i - 1][2] + cost[i][0];

			if (d[i - 1][0] > d[i - 1][1])
				d[i][2] = d[i - 1][0] + cost[i][1];
			else
				d[i][2] = d[i - 1][1] + cost[i][1];
		}

		int t_max;
		if (d[n - 1][0] > d[n - 1][1])
			t_max = d[n - 1][0];
		else
			t_max = d[n - 1][1];

		if (t_max > d[n - 1][2])
			cout << t_max << '\n';
		else
			cout << d[n - 1][2] << '\n';
	}

	return 0;
}