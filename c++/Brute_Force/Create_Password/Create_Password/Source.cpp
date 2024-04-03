#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

bool check(string password)
{
	int ja = 0;
	int mo = 0;
	for (char x : password)
	{
		if (x == 'a' || x == 'e' || x == 'i' || x == 'o' || x == 'u')
			mo += 1;
		else
			ja += 1;
	}

	return ja >= 2 && mo >= 1;
}

void go(int x, vector<char>& alpha, string password, unsigned int i)
{
	if (password.length() == x)
	{
		if (check(password))
		{
			cout << password << '\n';
		}
		return;
	}

	if (i >= alpha.size()) return;
	go(x, alpha, password + alpha[i], i + 1);
	go(x, alpha, password, i + 1);
}

int main()
{
	int n, x;
	cin >> x >> n;

	vector<char> c(n);

	for (int i = 0; i < n; i++)
	{
		char ch;
		cin >> c[i];
	}

	string password;

	sort(c.begin(), c.end());

	go(x, c, password, 0);

	return 0;
}