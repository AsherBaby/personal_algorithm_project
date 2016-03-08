#include <iostream>
#include <vector>

using namespace std;

void radixSort(vector<string>& arr, int stringMaxLen)
{
  const int BUCKETS = 256;
  vector<vector<string>> bucketsByWordLen(stringMaxLen+1);
  vector<vector<string>> buckets(BUCKETS);
  
  for (string& word: arr) bucketsByWordLen[word.size()].push_back(move(word));
  int idx = -1;
  for (vector<string>& wordList: bucketsByWordLen)
  {
    for (string& word: wordList)
    {
      arr[++idx] = move(word);
    }
  }
  
  int startingIdx = arr.size();
  for (int pos = stringMaxLen-1; pos >= 0; --pos)
  {
    startingIdx -= bucketsByWordLen[pos+1].size();
    for (int i = startingIdx; i < arr.size(); ++i)
    {
      buckets[arr[i][pos]].push_back(move(arr[i]));
    }
    int idx = startingIdx - 1;
    for (vector<string>& thisBucket: buckets)
    {
      for (string& word: thisBucket)
      {
        arr[++idx] = move(word);
      }
      thisBucket.clear();
    }
  }
}
int main(int argc, const char * argv[])
{
  vector<string> vs;
  vs.push_back("you");
  vs.push_back("love");
  vs.push_back("i");
  radixSort(vs, 4);
  for (auto& it: vs) cout << it << ' ';
  cout << endl;
  return 0;
}
