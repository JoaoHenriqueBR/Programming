#include"iostream"
#include"cstdlib"
using namespace std;

int main () 
{
  cout << "Um tipo int     tem "    << sizeof(int) << " bytes " << endl;
  cout << "Um tipo float   tem "    << sizeof(float) << " bytes " << endl;
  cout << "Um tipo double  tem " << sizeof(double) << " bytes " << endl;
  cout << "Um tipo char    tem "   << sizeof(char) << " bytes " << endl;
  cout << "Um tipo bool    tem "   << sizeof(bool) << " bytes " << endl;
  return 0; 
}
