#include <iostream>
#include <boost/asio.hpp>
#include <string>
using namespace std;
using namespace boost::asio;
int main() {
	io_service service;
	ip::udp::socket socket(service);
	ip::udp::endpoint local_add(ip::address::from_string("127.0.0.1"), 1080);
	socket.open(local_add.protocol());
	string str;
	char* receive_str = new char[1024];
	while (1) {
		cout << "请输入命令：";
		cin >> str;
	//	cout << "echo: " << str << endl;
		socket.send_to(buffer(str.c_str(), str.size()), local_add);

		socket.receive_from(buffer(receive_str, 1024), local_add);
		cout << "收到反馈：" << receive_str << endl;
		memset(receive_str, 0, 1024);
	}
	return 0;
}