import java.util.Scanner;

public class IEEE_task6 {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        System.out.println("Please enter the 1st number:");
        int num1 = input.nextInt();
        System.out.println("Please enter the 2nd number");
        int num2 = input.nextInt();
        int GCD = 1;
        for (int i = 1; i <= num1 && i <= num2; i++) {
            if (num1 % i == 0 && num2 % i == 0) {
                GCD = i;
            }
        }
        System.out.println(GCD);
    }

}
