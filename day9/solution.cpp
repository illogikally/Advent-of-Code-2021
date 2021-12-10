#include <bits/stdc++.h>

using namespace std;
using std::cout;

#define pii pair<int, int>
#define M 4098
#define N 4098


array<pii, 4> get_adjacents(pair<int, int> pos) {
  int i = pos.first;
  int j = pos.second;
  return array<pii, 4>({
    make_pair(i+1, j),
    make_pair(i-1, j),
    make_pair(i, j+1),
    make_pair(i, j-1),
  });
}

long bfs(pair<int, int> pos, char matrix[][N]) {
  long sum = 0;
  stack<pair<int, int>> children;
  children.push(pos);
  int i = pos.first;
  int j = pos.second;
  matrix[i][j] = '9';

  while (children.size() != 0) {
    auto child = children.top();
    children.pop();
    auto adjs = get_adjacents(child);
    i = child.first;
    j = child.second;
    ++sum;
    for (auto adj : adjs) {
      i = adj.first;
      j = adj.second;
      if (matrix[i][j] != '9') {
        children.push(adj);
        matrix[i][j] = '9';
      }
    }
  }
  return sum;
  return 0;
}
// long bfs(pair<int, int> pos, vector<vector<char>>& matrix) {
//   long sum = 0;
//   stack<pair<int, int>> children;
//   children.push(pos);
//   int i = pos.first;
//   int j = pos.second;
//   matrix[i][j] = '9';

//   while (children.size() != 0) {
//     auto child = children.top();
//     children.pop();
//     auto adjs = get_adjacents(child);
//     i = child.first;
//     j = child.second;
//     ++sum;
//     for (auto adj : adjs) {
//       i = adj.first;
//       j = adj.second;
//       if (matrix[i][j] != '9') {
//         children.push(adj);
//         matrix[i][j] = '9';
//       }
//     }
//   }
//   return sum;
// }

int main() {
  ifstream input("input");
  string line;

  static char matrix[M][N];

  for (int m = 0; getline(input, line); ++m) {
    if (m == 0) {
      char n[N];
      fill_n(n, N, '9');
      copy(begin(n), end(n), begin(matrix[0]));
    }
    istringstream iss(line);
    char n[N];
    n[0] = '9';
    copy(begin(line), end(line), begin(n)+1);
    n[N-1] = '9';
    copy(begin(n), end(n), begin(matrix[m+1]));
  }
  copy(begin(matrix[0]), end(matrix[0]), begin(matrix[M-1]));

  vector<long> b{0, 0, 0};
  for (int i = 1; i < M-1; ++i) {
    for (int j = 1; j < N-1; ++j) {
      if (matrix[i][j] != '9') {
        long r = bfs(make_pair(i, j), matrix);
        for (int k = 0; k < 3; ++k) {
          if (b[k] < r) {
            b.insert(b.begin()+k, r);
            break;
          }
        }
      }
    }
  }

  // vector<vector<char>> matrix;
  // while (getline(input, line) && line.length() != 0) {
  //   if (matrix.size() == 0) {
  //     vector<char> n(line.length()+2, '9');
  //     matrix.push_back(n);
  //   }
  //   istringstream iss(line);
  //   vector<char> n;
  //   n.push_back('9');
  //   for (auto c : line) {
  //     n.push_back(c);
  //   }
  //   n.push_back('9');
  //   matrix.push_back(n);
  // }
  // matrix.push_back(matrix[0]);

  // vector<long> b{0, 0, 0};
  // for (int i = 1; i < matrix.size()-1; ++i) {
  //   for (int j = 1; j < matrix[0].size()-1; ++j) {
  //     if (matrix[i][j] != '9') {
  //       long r = bfs(make_pair(i, j), matrix);
  //       for (int k = 0; k < 3; ++k) {
  //         if (b[k] < r) {
  //           b.insert(b.begin()+k, r);
  //           break;
  //         }
  //       }
  //     }
  //   }
  // }

  cout << endl << b[0] * b[1] * b[2] << endl;
}