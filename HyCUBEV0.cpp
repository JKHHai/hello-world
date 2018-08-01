//HyCUBE.cpp
//Implements the HyCUBE architecture using the C++ API in CGRA-ME
//Utilizes HyCUBEPE, a processing element specified in the HyCUBE paper

//1. Setup
#include <CGRA/Module.h>
#include <CGRA/ModuleComposites.h>
#include <CGRA/CGRA.h>
#include <CGRA/ILPMapper.h>
#include <CGRA/OpGraph.h>
#include <CGRA/Exception.h>
#include <CGRA/user-inc/UserArchs.h>
#include <CGRA/user-inc/UserModules.h>
#include <stdio.h>
std::unique_ptr<CGRA> UserArchs::createHyCUBEArch(const std::map<std::string, std::string> & args)
{
	//Declare all variables
	int cols;
	int rows;
	int pred;
	int c,r;

	//For use in connections
	std::string north = std::to_string(0);
	std::string east = std::to_string(1);
	std::string west = std::to_string(2);
	std::string south = std::to_string(3);

	//Collect variables from arguments
	try
	{
		cols = std::stoi(args.at("cols"));
		rows = std::stoi(args.at("rows"));
		pred = std::stoi(args.at("pred")); //Indicates whether or not we are using predicates
	}
	catch(const std::out_of_range & e)
	{
		throw cgrame_error("C++ Architecture Argument Error");
	}

	//Determine bit width
	if(pred == 1)
	{	
		unsigned const SIZE = 33;
	} else {
		unsigned const SIZE = 32;
	}
		
	//Create CGRA pointer
	std::unique_ptr<CGRA> result(new CGRA());

	//2. Add all elements within the Architecture
	
	//HyCUBE Processing Elements:
	for (c = 0; c < cols; c++)
	{
		for(r = 0; r < rows; r++)
		{
			if(c == 0)
			{	//Load-store-enabled PE's must sit in the second column
				result->addSubModule(new HyCUBEPE("pe_c0_r" + std::to_string(r), pred, 1));
			} else {
				//All other PE's are not load-store-enabled
				result->addSubModule(new HyCUBEPE("pe_c" + std::to_string(c) + "_r" + std::to_string(r), pred, 0));
			}
		}
	}

	//3. Add Configuration Files (if necessary)

	//4. Add Ports

	//5. Add Connections
	for(c = 1; c < cols; c++)
	{
		for(r = 1; r < rows; r++)
		{	
			std::string cColumn = std::to_string(c);
			std::string cRow = std::to_string(r);
			std::string pColumn = std::to_string(c-1);
			std::string pRow = std::to_string(r-1);
			
			//North-South connection
			result->addConnection("pe_c" + cColumn + "_r" + pRow + ".out" + south,
					      "pe_c" + cColumn + "_r" + cRow + ".in" + north);

			result->addConnection("pe_c" + cColumn + "_r" + cRow + ".out" + north, 
					      "pe_c" + cColumn + "_r" + pRow + ".in" + south);
			//East-West connection
			result->addConnection("pe_c" + pColumn + "_r" + cRow + ".out" + east,
					      "pe_c" + cColumn + "_r" + cRow + ".in" + west);
			
			result->addConnection("pe_c" + cColumn + "_r" + cRow + ".out" + west, 
					      "pe_c" + pColumn + "_r" + cRow + ".in" + east);

		}
	}

	//6. Return pointer
	return result;
}			 			
