#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"
#include "files.h"
#include <cstdio>

#define STL_TAG "[TESTS_STL_TAG]"



TEST_CASE( "Write stl is implemented", STL_TAG ) {
    // Given
	std::string stlFileName = "titi.stl";
	Files::FileMesh* mesh = new Files::FileMesh();

    // When
    int result = writeTriMesh(stlFileName, mesh);

    // Then
    CHECK(result != 1);
}

TEST_CASE("write stl write head infos", STL_TAG) {
	// Given
	std::string stlFileName = "titi.stl";
	Files::FileMesh* mesh = new Files::FileMesh();

    // When
    int result = writeTriMesh(stlFileName, mesh);

    // Then
    std::ifstream in; // will close on exit from this read function
    in.open(stlFileName.c_str());
    REQUIRE(in);

    std::string header;
    in >> header;
    CHECK(header == "solid");

    std::string footer;
    in >> footer;
    CHECK(footer == "endsolid");

    // need to clean by removing the file
    std::remove(stlFileName.c_str());
}