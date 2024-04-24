#include <iostream>
#include <queue>

using namespace std;

int main()
{
	int n;
	cin >> n;

	int dx[8] = { -2, -1, 1, 2, 2, 1, -1, -2 };
	int dy[8] = { 1, 2, 2, 1, -1, -2, -2, -1 };
	for (int i = 0; i < n; i++)
	{
		int a[300][300] = { 0 };
		int ans[300][300] = { 0 };

		queue<pair<int, int>> q;

		int l;
		int x, y;
		int f_x, f_y;
		cin >> l;
		cin >> x >> y;
		cin >> f_x >> f_y;

		q.push(make_pair(x, y)); ans[x][y] = 0; a[x][y] = 1;
		while (!q.empty())
		{
			x = q.front().first; y = q.front().second; q.pop();
			for (int k = 0; k < 8; k++)
			{
				int nx = x + dx[k], ny = y + dy[k];
				if (0 <= nx && nx < l && 0 <= ny && ny < l)
				{
					if (a[nx][ny] == 0)
					{
						ans[nx][ny] = ans[x][y] + 1;
						a[nx][ny] = 1;
						q.push(make_pair(nx, ny));
					}
				}
			}
		}
		cout << ans[f_x][f_y] << '\n';
	}

	return 0;
}