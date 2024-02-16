#include <iostream>

int memo[100];
int memo2[100];

int fibonacci_T_D(int n) {
	if (n <= 1)
		return n;
	else
	{
		if (memo[n] > 0)
			return memo[n];
		memo[n] = fibonacci_T_D(n - 1) + fibonacci_T_D(n - 2);
		return memo[n];
	}
}

int fibonacci_B_U(int n)
{
	if (n <= 1)
		return n;
	else
	{
		for (int i = 2; i <= n; i++)
		{
			memo2[i] = memo[i - 1] + memo[i - 2];
		}
		return memo2[n];
	}
}

int main()
{
	int n = 10;
	std::cout << fibonacci_T_D(n) << std::endl;
	std::cout << fibonacci_B_U(n) << std::endl;
	return(0);
}