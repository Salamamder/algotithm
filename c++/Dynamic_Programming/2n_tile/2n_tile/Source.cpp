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
		//원래 값을 그대로 쓰면 오버플로우 발생, 문제 조건이 10007로 나눈 값을 출력이므로 미리 나눔
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