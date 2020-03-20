package observer_pattern;

public class CurrentConditionDisplay implements Observer, DisplayElement{
    private float temperature;
    private float pressure;
    private float humidity;
    private WeatherData weatherData;
    public CurrentConditionDisplay(Subject subject){
         if (subject instanceof WeatherData) {
             this.weatherData = (WeatherData) subject;
             weatherData.addObservers(this);
         }
    }
    @Override
    public void update(float temperature, float humidity, float pressure) {
        this.temperature = temperature;
        this.pressure = pressure;
        this.humidity = humidity;
        this.display();
    }

    @Override
    public void display() {
        System.out.println("Current condition temperature/humidity/pressure: "+this.temperature+"/"+this.humidity+"/"+this.pressure);

    }
}
