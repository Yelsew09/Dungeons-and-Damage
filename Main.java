public class Main {
    public static void main(String[] args){
        var scanner = new java.util.Scanner(System.in);
        
        scanner.close();
    }
    static void pause(long time){
        try {
            Thread.sleep(time);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
    static void roll(String text){
        for (int i = 0; i < text.length();i++){
            System.out.print(text.charAt(i));
            pause(20L);
        }
    }
}