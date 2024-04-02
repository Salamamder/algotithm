#include <iostream>
#include <algorithm>
#include<vector>

using namespace std;

int main()
{
	int n;

	while (1)
	{
		cin >> n;
		if (n == 0)
			break;
		else
		{
			vector<int> a(n), d(n);
			for (int i = 0; i < n; i++)
			{
				cin >> a[i];
				if (i < 6)
					d[i] = 0;
				else
					d[i] = 1;
			}

			sort(d.begin(), d.end());

			do {
				for (int i = 0; i < n; i++)
				{
					if (d[i] == 0)
						cout << a[i] << ' ';
				}
				cout << '\n';
			} while (next_permutation(d.begin(), d.end()));
		}

		cout << '\n';
	}

	return 0;
}