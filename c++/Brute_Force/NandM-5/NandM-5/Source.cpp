#include <iostream>
#include <algorithm>


using namespace std;

bool c[10];
int a[10];
int arr[10];

void go(int index, int n, int m)
{
	if (index == m)
	{
		for (int i = 0; i < index; i++)
		{
			cout << a[i] << ' ';
		}
		cout << '\n';
		return;
	}

	for (int i = 1; i <= n; i++)
	{
		if (c[i])
			continue;
		c[i] = true;
		a[index] = arr[i - 1];
		go(index + 1, n, m);
		c[i] = false;
	}
}

int main()
{
	int n, m;

	cin >> n >> m;

	for (int i = 0; i < n; i++)
	{
		cin >> arr[i];
	}

	sort(arr, arr + n);

	go(0, n, m);

	return 0;
}