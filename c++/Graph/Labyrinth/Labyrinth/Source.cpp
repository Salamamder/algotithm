#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

int dx[4] = { -1,1,0,0 };
int dy[4] = { 0,0,1,-1 };
int ans[101][101];
int a[101][101];

int n, m;

void bfs(int x, int y) {
	queue<pair<int, int>> q; q.push(make_pair(x, y)); ans[x][y] = 1;
	while (!q.empty())
	{
		x = q.front().first; y = q.front().second; q.pop();
		for (int k = 0; k < 4; k++)
		{
			int nx = x + dx[k], ny = y + dy[k];
			if (0 <= nx && nx < n && 0 <= y && ny < m)
			{
				if (a[nx][ny] == 1 && ans[nx][ny] == 0)
				{
					ans[nx][ny] = ans[x][y] + 1;
					q.push(make_pair(nx, ny));
				}
			}
		}
	}
}

int main()
{
	cin >> n >> m;

	for (int i = 0; i < n; i++)
	{
		string line;
		cin >> line;

		for (int j = 0; j < m; j++)
		{
			a[i][j] = line[j] - '0';
		}
	}

	bfs(0, 0);
	cout << ans[n-1][m-1] << '\n';
	return 0;
}