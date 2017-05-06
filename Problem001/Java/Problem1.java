public class Problem1{
    public static void main(String[] args){
        int limit=1000;
        System.out.println(String.format("The sum of all the multiples of 3 or 5 below %d is: %d\n",limit,(geometricSolution(limit))));
    }
    
    public static int geometricSolution(int limit){
        //Substract the numbers that are divisible by 3 and 5 in order to avoid being counted twice
        return sumDivisibleBy(3,limit-1)+sumDivisibleBy(5,limit-1)-sumDivisibleBy(15,limit-1);
    }
    
    public static int sumDivisibleBy(int m, int greatest){
        int n=greatest/m;
        return m * (n * ( n + 1 ) / 2 );
    }
}