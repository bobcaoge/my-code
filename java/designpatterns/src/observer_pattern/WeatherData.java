package observer_pattern;

import java.util.ArrayList;

public class WeatherData implements Subject{
    private float humidity;
    private float temperature;
    private float pressure;
    private ArrayList<Observer> observers;
    public WeatherData(){
        this.observers = new ArrayList<>();
    }
    @Override
    public void addObservers(Observer observer) {
        this.observers.add(observer);
    }

    @Override
    public void deleteObservers(Observer observer) {
        int index = this.observers.indexOf(observer);
        if (index >= 0){
            this.observers.remove(observer);
        }
    }

    @Override
    public void notifyObservers() {
        for (Observer observer: this.observers) {
            observer.update(this.temperature, this.humidity, this.pressure);
        }
    }

    public void setMeasurement(float temperature, float humidity, float pressure){
        this.humidity = humidity;
        this.pressure = pressure;
        this.temperature = temperature;
        notifyObservers();
    }
}
