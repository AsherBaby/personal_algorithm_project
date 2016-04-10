package cci.chap6;

import java.util.Arrays;

public class BottleOfPills {

    public static int findTheUnique(double[] bottles) {
        double total = 0;
        for (int i = 0; i < 20; i++) {
            total += i * bottles[i];
        }
        return (int)((total - 190) * 10);
    }

    public static void test() {
        double[] bottles = new double[20];
        Arrays.fill(bottles, 1);
        bottles[5] += 0.1;
        if (findTheUnique(bottles) != 5) {
            System.out.println("Error");
        }
    }

}
