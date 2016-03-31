package cci.chap6;


public class Main {

    public static void main(String[] args) {
        double[] bottles = new double[20];
        for (int i = 0; i < 20; i++) {
            bottles[i] = 1;
        }
        bottles[5] = 1.1;
        System.out.println(BottleOfPills.findTheUnique(bottles));
    }
}
