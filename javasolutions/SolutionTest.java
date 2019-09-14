import java.io.*;
public class SolutionTest{
   public static void printArray(int[] array) {
  for (int x : array) {
    System.out.print(x);
    System.out.print("\n");
  }
}

   public static void main(String[] args){
      int[] t={2,7,11,15};
      Solution rr = new Solution();

      printArray(rr.twoSum(t,9));
 
   }
}