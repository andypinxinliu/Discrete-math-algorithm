import java.io.*;
import java.util.*;

public class GcdLcm
{
    static int originalNumber1;
    static int originalNumber2;
    static int method = 1;
    public static void main(String[] args)throws IOException
    {
        System.out.println("This program helps to prime factorization, coprime of the first input");
        System.out.println("3 methods here to use, input the number to run this program");
        System.out.println("0 == strop the program");
        System.out.println("1 == find GCD and LCM");
        System.out.println("2 == find factorization");
        System.out.println("3 == find those are not coprime in Webwork problem3");

        
        ArrayList<Integer> primes = new ArrayList<>();
        int i, j;
        for (i = 2; i < 500000; i++){
            int isPrime = 1;
            int maxprime = (int)Math.sqrt(i) + 1;
            for (j = 2; j < maxprime; j++){
                if (i % j == 0){
                    isPrime = 0;
                    break;
                }
            }
            if (isPrime == 1)
                primes.add(i);
        }
        
        while (method != 0){
            System.out.print("The method you want to use: ");
            BufferedReader reader1 = new BufferedReader(
                new InputStreamReader(System.in));
            String name3 = reader1.readLine();
            int method = Integer.parseInt(name3);
            run(method, primes);
            System.out.println();
            if (method == 0){
                break;
            }
            else if(method < 0 || method >= 4){
                System.out.print("Wrong input!");
            }
        }
    }
    static void run(int method, ArrayList<Integer> primes)throws IOException{
        if(method == 1){
            System.out.println("Now we find the GCD and LCM of two numbers");
            System.out.print("Enter two numbers, with a space in between: ");
            BufferedReader reader = new BufferedReader(
            new InputStreamReader(System.in));
  
            String name = reader.readLine();
            String[] test = name.split(" ", 2);
            int number1 = Integer.parseInt(test[0]);
            int number2 = Integer.parseInt(test[1]);
            originalNumber1 = number1;
            originalNumber2 = number2;
            int value;
            value = gcd(originalNumber1, originalNumber2);
            System.out.println("GCD for these two numbers are: "+ value);
            System.out.println("LCM of " + originalNumber1 + " and " + originalNumber2 + " is " + lcm(originalNumber1, originalNumber2));
        }
        else if(method == 2){
            System.out.print("Now, check the factorization, write down a number: ");
            BufferedReader bew = new BufferedReader(
            new InputStreamReader(System.in));
            
            String name2 = bew.readLine();
            int number3 = Integer.parseInt(name2);
            factor(number3, primes);
        }
        else if(method == 3){
            System.out.print("Now, check the coprime, write down a number: ");
            ArrayList<Integer> coprime = new ArrayList<>();
            BufferedReader bew = new BufferedReader(
            new InputStreamReader(System.in));
            
            String name2 = bew.readLine();
            int number3 = Integer.parseInt(name2);
        
            checkcoprime(number3, coprime);
            System.out.print("The coprime of " + number3 + " is: ");
            for (int a : coprime){
                System.out.print(a + " ");
            }
            System.out.println();
            System.out.println("ϕ("+number3+") = "+coprime.size());
        }
    }
    static int gcd(int a, int b)
    {
        if (a == 0)
            return b;
        return gcd(b % a, a);
    }
    
    // method to return LCM of two numbers
    static int lcm(int a, int b)
    {
        return (a / gcd(a, b)) * b;
    }
    
    static int coprime(int a, int b) {
        if ( gcd(a, b) == 1)
            return 1;
        else
            return 0;
    }
    static void checkcoprime(int number, ArrayList<Integer> coprime){
        for (int i = 1; i <= number; i++){
            if (coprime(i, number) == 1){
                coprime.add(i);
            }
        }
    }
    static void factor(int number, ArrayList<Integer> primes){
        ArrayList<Integer> divident = new ArrayList<>();
        originalNumber1 = number;
        for (int key : primes){
            while (number % key == 0){
                number = number / key;
                divident.add(key);
            }
            while (number % key == 0){
                number = number / key;
                divident.add(key);
            }
        }
        if (number != 1 && number != originalNumber1 && number != originalNumber2){
            System.out.println("Unable to do calculation in this range of primes!!!");
            StringBuilder s1 = new StringBuilder();
            for (int k = 0; k < divident.size() - 1; k++){
                s1 = s1.append(Integer.toString(divident.get(k)));
                s1 = s1.append(" * ");
            }
            s1.append(Integer.toString(divident.get(divident.size() - 1)));
            System.out.println(s1.toString() + "* some large prime numbers");
        }
        else if(number == originalNumber1){
                System.out.println("the first number you input is a prime");
            }
        else if (number == originalNumber2){
                System.out.println("the second number you input is a prime");
            }
        else{
            StringBuilder s1 = new StringBuilder();
            for (int k = 0; k < divident.size() - 1; k++){
                s1 = s1.append(Integer.toString(divident.get(k)));
                s1 = s1.append(" * ");
            }
            s1.append(Integer.toString(divident.get(divident.size() - 1)));
            System.out.println(originalNumber1 + " = " + s1.toString());
        }
    }
}
