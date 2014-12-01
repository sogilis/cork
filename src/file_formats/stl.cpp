#include "files.h"

#include <iostream>
#include <fstream>
using std::ifstream;
using std::ofstream;
using std::endl;


namespace Files {

int writeSTL(std::string filename, FileMesh* data){
    if(!data) return 1;
    
    ofstream out;
    out.open(filename.c_str());
    if(!out) return 1;
    
    // "OFF"
    out << "solid" << endl;
    out << "endsolid" << endl;
	return 0;
}

}