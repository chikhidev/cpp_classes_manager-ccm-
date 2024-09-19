#ifndef USER_H
#define USER_H

#include <iostream>
#include <string>

class User {
	public:
		User();
		~User();
	private:
		void createUser(std::string name, int age);
};

#endif
