public class BaselineInt {
    public static void main(String[] args) {
        int[] vec1 = new int[256];
        int[] vec2 = new int[256];
        for (int i = 0; i < 256; i++) {
            vec1[i] = (int)(Math.random() * 16384);
            vec2[i] = (int)(Math.random() * 16384);
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
