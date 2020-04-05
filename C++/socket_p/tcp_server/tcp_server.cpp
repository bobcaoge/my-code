#include <iostream>
#include <boost/asio.hpp>
#include <stdlib.h>
#include <boost/thread.hpp>
#include<thread>
using namespace std;
using namespace boost::asio;
/*
void manager(ip::tcp::socket tcp_socket) {
	char receive_str[1023] = { 0 };
	while(1){
		try{
			boost::system::error_code ec;
			tcp_socket.read_some(buffer(receive_str, 1023), ec);
			cout << "�յ���Ϣ��" << receive_str << endl;
			system(receive_str);
			tcp_socket.write_some(buffer(receive_str, 1023), ec);
			memset(receive_str, -1, 1024);
		}
		catch (boost::exception &e) {
			cout << "�ͻ��ˣ�" << tcp_socket.remote_endpoint().address() << ":" <<
				tcp_socket.remote_endpoint().port() << "�Ͽ�����" << endl;
		}
	}
}
*/
int main() {
	io_service service;
	ip::tcp::socket tcp_socket(service);
	ip::tcp::endpoint ip_port(ip::address_v4::from_string("127.0.0.1"), 9999);
	ip::tcp::acceptor acceptor(service, ip_port);
	char receive_str[1024] = { 0 };
	while (1) {
		acceptor.accept(tcp_socket);
		cout << "�ͻ��ˣ�" << tcp_socket.remote_endpoint().address() << ":" << tcp_socket.remote_endpoint().port() << "������" << endl;
		while(1){
			boost::system::error_code ec;
			tcp_socket.read_some(buffer(receive_str, 1024), ec);
			if (ec.value() != 0) {
				cout << "�ͻ��ˣ�" << tcp_socket.remote_endpoint().address() << ":" << tcp_socket.remote_endpoint().port() << "�Ͽ�����" << endl;
				tcp_socket.close();
				break;
			}
			cout << "�յ���Ϣ��" << receive_str << endl;
			system(receive_str);
			tcp_socket.write_some(buffer(receive_str, 1024), ec);
			memset(receive_str, 0, 1024);
		}
	}






	return 0;
}