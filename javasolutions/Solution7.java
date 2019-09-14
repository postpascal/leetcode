class Solution7 {
    public int reverse(int x) {
        boolean isNegative = false;
        if(x == 0 || x > Integer.MAX_VALUE || x < Integer.MIN_VALUE) {
            return 0;
        }else if (x < 0) {
            isNegative = true;
            x = Math.abs(x);
        }
        int size = String.valueOf(x).length();

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < size; i++) {
            sb.append(x % 10);
            x = x / 10;
        }
        try {
            x = Integer.parseInt(sb.toString());
        }catch(NumberFormatException e) {
            return 0;  
        }
        return isNegative ? x * -1 : x;
    }
    public static void main(String[] args){
        Solution7 rr= new Solution7();
        System.out.println(rr.reverse(-786));
    }
}