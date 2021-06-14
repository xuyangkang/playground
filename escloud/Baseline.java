public class Baseline {
    public static void main(String[] args) {
        double[] vec1 = new double[256];
        double[] vec2 = new double[256];
        for (int i = 0; i < 256; i++) {
            vec1[i] = Math.random();
            vec2[i] = Math.random();
        }
        double sum = 0;
        for (int count = 0; count < 800000; count++) {
            for (int i = 0; i < 256; i++) {
                sum += vec1[i] * vec2[i];
            }
        }
        System.out.println(sum);
    }
}
