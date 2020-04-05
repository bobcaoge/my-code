// 通过设计一个气象站布告来体现观察者模式，来自head first设计模式
#include <iostream>
#include <vector>
using namespace std;
class Obverser{
public:
	virtual void update(double temperature, double humidity, double pressure) = 0;
};
class Subject{
public:
	virtual void addObverser(Obverser* obverser) = 0;
	virtual void deleteObverser(Obverser* obverser) = 0;
	virtual void notify() = 0;
};
class Displayment{
	virtual void display() = 0;
};
class WeatherData : public Subject
{
public:
	double temperature;
	double humidity;
	double pressure;
	vector<Obverser*> obversers;

public:
	void addObverser(Obverser* obverser){
		obversers.push_back(obverser);
	}
	void deleteObverser(Obverser* obverser){
		auto it = find(obversers.begin(), obversers.end(), obverser);
		if (it != obversers.end()){
			obversers.erase(it);
		}
	}
	void notify(){
		for (auto obverser : obversers){
			obverser->update(temperature, humidity, pressure);
		}
	}
	void setMeasurement(double temperature, double humidity, double pressure){
		this->temperature = temperature;
		this->humidity = humidity;
		this->pressure = pressure;
		notify();
	}
};
class CurrentConditionDisplay :public Obverser, public Displayment
{
public:
	double temperature;
	double humidity;
	double pressure;
	WeatherData* weatherData;
public:
	CurrentConditionDisplay(Subject* sub){
		this->weatherData = dynamic_cast<WeatherData*>(sub);
		this->weatherData->obversers.push_back(this);
	}
	void display(){
		cout << "current condition: temperatrue is " << temperature << " humidity is " << humidity << " pressure is " << pressure << endl;
	}
	void update(double temperature, double humidity, double pressure){
		this->temperature = temperature;
		this->humidity = humidity;
		this->pressure = pressure;
		display();
	}
};
int main(){
	WeatherData* weatherDate = new WeatherData();
	Obverser* obv = new CurrentConditionDisplay(weatherDate);
	weatherDate->setMeasurement(10, 20, 30);
	weatherDate->setMeasurement(20.2, 32, 19);
	weatherDate->setMeasurement(13, 24, 13);
	cin.get();
	return 0;
}