#include <iostream>

using namespace std;

int main()
{
	int cost[1000][3];
	int n;
	int d[1000][3];

	cin >> n;

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < 3; j++)
		{
			int t_cost;
			cin >> t_cost;
			cost[i][j] = t_cost;
		}
	}

	d[0][0] = cost[0][0];
	d[0][1] = cost[0][1];
	d[0][2] = cost[0][2];

	for (int i = 1; i < n; i++)
	{
		if (d[i - 1][0] > d[i - 1][1])
			d[i][2] = d[i - 1][1] + cost[i][2];
		else
			d[i][2] = d[i - 1][0] + cost[i][2];

		if (d[i - 1][0] > d[i - 1][2])
			d[i][1] = d[i - 1][2] + cost[i][1];
		else
			d[i][1] = d[i - 1][0] + cost[i][1];

		if (d[i - 1][1] > d[i - 1][2])
			d[i][0] = d[i - 1][2] + cost[i][0];
		else
			d[i][0] = d[i - 1][1] + cost[i][0];
	}

	int min_cost;

	if (d[n - 1][0] > d[n - 1][1])
		min_cost = d[n - 1][1];
	else
		min_cost = d[n - 1][0];

	if (min_cost > d[n - 1][2])
		cout << d[n - 1][2];
	else
		cout << min_cost;

	return 0;
}