#include <iostream>

using namespace std;

int d[1001];

int tile(int n)
{
	d[1] = 1;
	d[2] = 2;
	for (int i = 3; i <= n; i++)
	{
		d[i] = (d[i - 1] + d[i - 2])%10007;
		//���� ���� �״�� ���� �����÷ο� �߻�, ���� ������ 10007�� ���� ���� ����̹Ƿ� �̸� ����
	}

	return d[n];
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n;

	cin >> n;

	cout << tile(n);
	return(0);
}