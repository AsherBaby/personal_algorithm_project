#include <iostream>
#include <vector>
#include <list>
#include <stack>
#include <string>
#include <set>
#include <algorithm>

using namespace std;

bool isBalanced(const string& code)
{
  stack<char> symbolStorage;
  for (auto& it: code)
  {
    if (it == '(' || it == '[' || it == '{')
    {
      symbolStorage.push(it);
    }
    else if (it == ')')
    {
      if (symbolStorage.top() == '(') symbolStorage.pop();
      else return false;
    }
    else if (it == ']')
    {
      if (symbolStorage.top() == '[') symbolStorage.pop();
      else return false;
    }
    else if (it == '}')
    {
      if (symbolStorage.top() == '{') symbolStorage.pop();
      else return false;
    }
  }
  return symbolStorage.empty() ? true : false;
}

int evaluatePostfix(const string& expression)
{
  stack<float> numStorage;
  set<char> operators {'+', '-', '*'};
  for (auto& symbol: expression)
  {
    // Work only for digit here
    if (isdigit(symbol))
    {
      numStorage.push((float)symbol - '0');
    }
    else if (operators.find(symbol) != operators.end())
    {
      float firstNum = numStorage.top();
      numStorage.pop();
      float secondNum = numStorage.top();
      numStorage.pop();
      float target;
      switch (symbol)
      {
        case '+':
          target = firstNum + secondNum;
          break;
        case '-':
          target = firstNum - secondNum;
          break;
        case '*':
          target = firstNum * secondNum;
          break;
        default:
          ;
      }
      numStorage.push(target);
    }
  }
  return numStorage.top();
}

string infixToPostfix(const string& expression)
{
  string output;
  stack<char> operatorStorage;
  for (auto& symbol: expression)
  {
    if (isalpha(symbol))
    {
      output.push_back(symbol);
    }
    else
    {
      if (operatorStorage.empty())
      {
        operatorStorage.push(symbol);
      }
      else
      {
        if (symbol == '(')
        {
          operatorStorage.push(symbol);
        }
        else if (symbol == ')')
        {
          while (operatorStorage.top() != '(')
          {
            output.push_back(operatorStorage.top());
            operatorStorage.pop();
            if (operatorStorage.empty()) break;
          }
          operatorStorage.pop();
        }
        else if (symbol == '+')
        {
          while (operatorStorage.top() == '+' || operatorStorage.top() == '*')
          {
            output.push_back(operatorStorage.top());
            operatorStorage.pop();
            if (operatorStorage.empty()) break;
          }
          operatorStorage.push(symbol);
        }
        else if (symbol == '*')
        {
          while (operatorStorage.top() == '*')
          {
            output.push_back(operatorStorage.top());
            operatorStorage.pop();
            if (operatorStorage.empty()) break;
          }
          operatorStorage.push(symbol);
        }
      }
    }
  }
  while (!operatorStorage.empty())
  {
    output.push_back(operatorStorage.top());
    operatorStorage.pop();
  }
  return output;
}

int main(int argc, const char * argv[])
{
  string code {"{[()]}"};
  if (isBalanced(code)) cout << "True" << endl;
  else cout << "False" << endl;
  string postfixExpression {"6523+8*+3+*"};
  cout << evaluatePostfix(postfixExpression) << endl;
  string infix {"a+b*c+(d*e+f)*g"};
  cout << infixToPostfix(infix) << endl;
  return 0;
}
