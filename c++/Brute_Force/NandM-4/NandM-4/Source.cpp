#include <iostream>

using namespace std;

bool c[10];
int a[10];

void go(int index, int start, int n, int m)
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

	for (int i = start; i <= n; i++)
	{
		a[index] = i;
		go(index + 1, i, n, m);
	}
}

int main()
{
	int n, m;

	cin >> n >> m;
	go(0, 1, n, m);

	return 0;
}