public class Problem2{

	public static void main(String[] args){
		int limit=4000000;
		System.out.println(getFibonacciSum(limit));
	}

	public static int getFibonacciSum(int limit){
		if(limit<2)
			return 0;

		int sum = 0, prev = 0, current=1;
		while(current<limit){
			int temp=current;
			current=prev+current;
			prev=temp;
			if(current%2==0)
				sum+=current;
		}
		return sum;
	}
}