package observer_pattern;

public interface Subject {
    public void addObservers(Observer observer);
    public void deleteObservers(Observer observer);
    public void notifyObservers();
}
