#include "readFile.h"
#define configFileName "test_data.txt"
int userInput;
using namespace std;

readFile::readFile()
{
}


readFile::~readFile()
{
}

int myTable[15];

void initMyTable() {
	for (unsigned int iCount = 0; iCount < 15; iCount++)
	{
		myTable[iCount] = 0;
	}
}

void printError() 
{
	for (unsigned int iCount = 0; iCount < 15; iCount++)
	{
		//myTable[iCount] = 0;
		if (myTable[iCount] != 0)
		std::cout << iCount << " has : " << myTable[iCount] << std::endl;
	}
}

void updateTable(char x) {
	if (x == 'Z') 
		myTable[0] += 1;
	if (x == 'W')
		myTable[1] += 1;
		
	if (x == 'U')
		myTable[2] += 1;
		
	if (x == 'X')
		myTable[3] += 1;
		
	if (x == 'G')
		myTable[4] += 1;
		
	if (x == 'H')
		myTable[5] += 1;
		
	if (x == 'F')
		myTable[6] += 1;
		
	if (x == 'V')
		myTable[7] += 1;
	
	if (x == 'S')
		myTable[8] += 1;
		
	if (x == 'R')
		myTable[9] += 1;
		
	if (x == 'T')
		myTable[10] += 1;
		
	if (x == 'O')
		myTable[11] += 1;
	if (x == 'N')
		myTable[12] += 1;
	if (x == 'I')
		myTable[13] += 1;
	if (x == 'E')
		myTable[14] += 1;
}


string getResult() {
	string result ="";
	int loop = 0;
	if (myTable[0] >= 1)
	{
		loop = myTable[0];
		for (unsigned int iCount = 0; iCount < loop; iCount++)
		{
			result = result + '0';
			myTable[0]--; //z
			myTable[14]--; //e
			myTable[9]--; //r
			myTable[11]--; //o
		}
		loop = 0;
	}
	if (myTable[1] >= 1)
	{
		loop = myTable[1];
		for (unsigned int iCount = 0; iCount < loop; iCount++)
		{
			result = result + '2';
			myTable[10]--; //t
			myTable[1]--; //w
			myTable[11]--; //o
		}
		loop = 0;
		
	}
	if (myTable[2] >= 1)
	{
		loop = myTable[2];
		for (unsigned int iCount = 0; iCount < loop; iCount++)
		{
			result = result + '4';
			myTable[6]--; //f
			myTable[11]--; //o
			myTable[2]--; //u
			myTable[9]--; //r
		}
		loop = 0;
	}
	if (myTable[3] >= 1)
	{
		loop = myTable[3];
		for (unsigned int iCount = 0; iCount < loop; iCount++)
		{
			result = result + '6';
			myTable[8]--; //s
			myTable[13]--; //i
			myTable[3]--; //x
		}
		loop = 0;
	}
	if (myTable[4] >= 1)
	{
		loop = myTable[4];
		for (unsigned int iCount = 0; iCount < loop; iCount++)
		{
			result = result + '8';
			myTable[14]--; //e
			myTable[13]--; //i
			myTable[4]--; //g
			myTable[5]--; //h
			myTable[10]--; //t
		}
		loop = 0;
	}
	if (myTable[5] >= 1)
	{
		loop = myTable[5];
		for (unsigned int iCount = 0; iCount < loop; iCount++)
		{
			result = result + '3';
			myTable[10]--; //t
			myTable[5]--; //h
			myTable[9]--; //r  
			myTable[14]--; //e
			myTable[14]--; //e
		}
		loop = 0;
	}
	if (myTable[6] >= 1)
	{
		loop = myTable[6];
		for (unsigned int iCount = 0; iCount < loop; iCount++)
		{
			result = result + '5';
			myTable[6]--; //f
			myTable[13]--; //i
			myTable[7]--; //v  
			myTable[14]--; //e
		}
		loop = 0;
	}
	if (myTable[7] >= 1)
	{
		loop = myTable[7];
		for (unsigned int iCount = 0; iCount < loop; iCount++)
		{
			result = result + '7';
			myTable[8]--; //s
			myTable[14]--; //e
			myTable[7]--; //v  
			myTable[14]--; //e
			myTable[12]--; //e
		}
		loop = 0;

	}
	if (myTable[11] >= 1)
	{
		loop = myTable[11];
		for (unsigned int iCount = 0; iCount < loop; iCount++)
		{
			result = result + '1';
			myTable[11]--; //o
			myTable[12]--; //n
			myTable[14]--; //e
		}
		loop = 0;
	}
	if (myTable[13] >= 1)
	{
		loop = myTable[13];
		for (unsigned int iCount = 0; iCount < loop; iCount++)
		{
			result = result + '9';
			myTable[12]--; //n
			myTable[13]--; //i
			myTable[12]--; //n
			myTable[14]--; //e  
		}
		loop = 0;
	}

	return result;
}
int main() {
	std::ifstream readConfigFile(configFileName, std::ifstream::in);
	char line[255];
	while (readConfigFile.good())
	{
		readConfigFile.getline(line, 255);
		if(readConfigFile) std::cout << "Input : "<< line <<std::endl;
		
		initMyTable();
		for (unsigned int iCount = 0; iCount < 255; iCount++)
		{
			if (line[iCount] == NULL) {
				break;
			}
			updateTable(line[iCount]);
		}
		std::cout << "Output: " << getResult() << endl;
		printError();
		
	}
	readConfigFile.close();

	std::cout << "Press anything to exit...";
	std::cin >> userInput;

	return 0;
}