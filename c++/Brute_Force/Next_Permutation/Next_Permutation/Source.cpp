#include <iostream>
#include <algorithm>

using namespace std;

bool next_permumation(int* a, int n)
{
	int i = n - 1;
	while (i > 0 && a[i - 1] >= a[i]) i -= 1;
	if (i <= 0) return false;
	int j = n - 1;
	while (a[j] <= a[i - 1]) j -= 1;
	swap(a[i - 1], a[j]);
	j = n - 1;
	while (i < j)
	{
		swap(a[i], a[j]);
		i += 1;
		j -= 1;
	}
	return true;
}

int main()
{
	int a[10000];
	int n;

	cin >> n;

	for (int i = 0; i < n; i++)
	{
		cin >> a[i];
	}

	bool is_fianl = next_permumation(a, n);
	if (is_fianl == false)
		cout << -1 << endl;
	else
	{
		for (int i = 0; i<n; i++)
		{
			cout << a[i] << ' ';
		}
		cout << '\n';
	}

	return 0;
}