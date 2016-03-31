package cci.chap6;

public class BottleOfPills {

    public static double findTheUnique(double[] bottles) {
        double total = 0;
        for (int i = 0; i < 20; i++) {
            total += i * bottles[i];
        }
        return (total - 190) * 10;
    }

}
