#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include<queue>

using namespace std;

int a[25][25];
int in[25][25];
int dx[4] = { -1,1,0,0 };
int dy[4] = { 0,0,1,-1 };
int n;
vector<int> num(25 * 25);

void bfs(int x, int y, int cnt)
{
	queue<pair<int, int>> q; q.push(make_pair(x, y)); a[x][y] = cnt;
	while (!q.empty())
	{
		x = q.front().first, y = q.front().second; q.pop();
		for (int k = 0; k < 4; k++)
		{
			int nx = x + dx[k], ny = y + dy[k];
			if (0 <= nx && nx < n && 0 <= ny && ny < n)
			{
				if (in[nx][ny] == 1 && a[nx][ny] == 0)
				{
					q.push(make_pair(nx, ny)); a[nx][ny] = cnt;
					num[cnt] = num[cnt] + 1;
				}
			}
		}
	}
}

int main()
{
	cin >> n;

	for (int i = 0; i < n; i++)
	{
		string line;
		cin >> line;

		for (int j = 0; j < n; j++)
		{
			in[i][j] = line[j] - '0';
		}
	}

	int comp = 0;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (in[i][j] == 1 && a[i][j] == 0)
			{
				bfs(i, j, ++comp);
			}
		}
	}

	sort(num.rbegin(), num.rend());

	cout << comp << '\n';

	for (int i = 1; i <= comp; i++)
	{
		cout << num[comp-i]+1 << '\n';
	}

	return 0;
}