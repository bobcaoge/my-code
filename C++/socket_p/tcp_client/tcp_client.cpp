#include <iostream>
#include <boost/asio.hpp>
using namespace std;
using namespace boost::asio;
int main() {
	io_service service;
	ip::tcp::socket tcp_socket(service);
	ip::tcp::endpoint ip_port(ip::address_v4::from_string("127.0.0.1"), 9999);
	tcp_socket.connect(ip_port);
	char str[1024] = { 0 };
	while (1) {
		cout << "�����룺";
		cin >> str;
		tcp_socket.write_some(buffer(str, 1024));
		memset(str, 0, 1024);
		tcp_socket.read_some(buffer(str, 1024));
		cout << "�յ�����: " << str << endl;
		memset(str, 0, 1024);
	}
	return 0;
}