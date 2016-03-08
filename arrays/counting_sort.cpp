#include <iostream>
#include <vector>

using namespace std;

void countingRadixSort( vector<string> & arr, int stringLen )
{
  const int BUCKETS = 256;
  
  int N = arr.size( );
  vector<string> buffer( N );
  
  for( int pos = stringLen - 1; pos >= 0; --pos )
  {
    vector<int> count( BUCKETS + 1 );
    
    for( int i = 0; i < N; ++i )
      ++count[ arr[ i ][ pos ] + 1 ];
    
    for( int b = 1; b <= BUCKETS; ++b )
      count[ b ] += count[ b - 1 ];
    
    for( int i = 0; i < N; ++i )
      buffer[count[ arr[ i ][ pos ] ]++ ] = std::move( arr[ i ] );
    
    // swap in and out roles
    std::swap(arr, buffer);
  }
}

int main(int argc, const char * argv[])
{
  vector<string> strings;
  for (int i = 0; i < 18; ++i)
  {
    string x;
    for (int j = 0; j < 5; ++j)
    {
      x += char(rand()%26+'a');
    }
    strings.push_back(x);
  }
  for (string word: strings) cout << word << ' ';
  cout << endl;
  cout << "After sort:\n";
  countingRadixSort(strings, 5);
  for (string word: strings) cout << word << ' ';
  cout << endl;
  return 0;
}
