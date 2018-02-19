#include <sstream>
using namespace std;

template <typename mytype>
double converter(mytype x){
	std::string str = boost::lexical_cast<std::string>(x);
	double x1 = boost::lexical_cast<double>(str);
	return x1;
}

//template <typename mytype2>
//mytype2 reconverter(double y){
//	std::ostringstream strs;
//	strs << y;
//	std::string str = strs.str();
//
//	istringstream os(str);
//	mytype2 d;
//	os >> d;
//	return d;
//}