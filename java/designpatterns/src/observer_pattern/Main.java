package observer_pattern;

public class Main {
    public static void main(String[] args) {
        WeatherData weatherData = new WeatherData();
        CurrentConditionDisplay currentConditionDisplay = new CurrentConditionDisplay(weatherData);
        weatherData.setMeasurement(30, 20, 40);
        weatherData.setMeasurement(20, 30, 10);
        weatherData.setMeasurement(10, 40, 20);
    }
}
