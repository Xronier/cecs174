import java.util.Scanner;
public class digitalLove {
    public static boolean isIncreasing(int[] values) {
        for (int i = 0; i < values.length - 1; i++) {
            // Look to the value one digit over from i and determine if it is less
            if (values[i] >= values[i + 1]) {
                return false;
            }
        }
        return true;
    }


    public static int getNumber() {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter a positive number");
        int userInteger = input.nextInt();
        // Validation
        while(userInteger <= 0) {
            System.out.println("Invalid, enter a positive number");
            userInteger = input.nextInt();
        }
        return userInteger;
    }


    public static int[] getDigits(int number) {
        // Cast the Math.log10 to an int as it would instead return a double.
        // Then, add 1 to Math.log10 as the log of 10 always returns the number of digits - 1
        int[] userArray = new int [(int) Math.log10(number) + 1];
        for(int i = userArray.length - 1; i >= 0; i--) {
            // Cut off the rightmost digit of number and assign it to the rightmost index of userArray
            int rightmostDigit = number % 10;
            userArray[i] = rightmostDigit;
            // Divide by 10 to shorten number by 1 digit
            number /= 10;
        }
        return userArray;
    }


    public static void main(String[] args) {
        int[] userDigits = getDigits(getNumber());
        if (isIncreasing(userDigits)){
            System.out.println("Those numbers are in increasing order");
        }
        else {
            System.out.println("Those numbers are not in increasing order");
        }
    }
}
