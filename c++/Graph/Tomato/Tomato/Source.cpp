#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

int n, m;
int ans[1000][1000];
int a[1000][1000];
int dx[4] = { -1,1,0,0 };
int dy[4] = { 0,0,1,-1 };

int main()
{
	cin >> m >> n;

	queue<pair<int, int>> q;

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			cin >> a[i][j];
			ans[i][j] = -1;
			if (a[i][j] == 1)
			{
				q.push(make_pair(i, j));
				ans[i][j] = 0;
			}
		}
	}

	while (!q.empty())
	{
		int x = q.front().first, y = q.front().second; q.pop();
		for (int k = 0; k < 4; k++)
		{
			int nx = x + dx[k], ny = y + dy[k];
			if (0 <= nx && nx < n && 0 <= ny && ny < m)
			{
				if (a[nx][ny] == 0 && ans[nx][ny] == -1)
				{
					ans[nx][ny] = ans[x][y] + 1;
					q.push(make_pair(nx, ny));
				}
			}
		}
	}

	int max = 0;
	for (int i = 0; i < n; i++)
	{
		for (int j=0; j < m; j++)
		{
			if (max < ans[i][j])
				max = ans[i][j];
		}
	}

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			if (a[i][j] == 0 && ans[i][j] == -1)
			{
				max = -1;
			}
		}
	}

	cout << max << '\n';

	return 0;
}