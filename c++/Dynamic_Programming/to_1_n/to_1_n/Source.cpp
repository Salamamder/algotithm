#include <iostream>

using namespace std;

int d[1000000];

int go(int n)
{
	if (n == 1) return 0;
	if (d[n] > 0) return d[n];
	d[n] = go(n-1) + 1;
	if (n % 2 == 0)
	{
		int tmp = go(n / 2) + 1;
		if (d[n] > tmp) d[n] = tmp;
	}
	if (n % 3 == 0)
	{
		int tmp = go(n / 3) + 1;
		if (d[n] > tmp) d[n] = tmp;
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
	cout << go(n);

	return (0);
}

// 배열 크기가 너무 커서 Stack overfliow가 발생할 수 있음 -> https://lollolzkk.tistory.com/5 사이트 참조해서 스택 예약 크기 키울 것.