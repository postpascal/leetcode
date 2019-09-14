import java.io.*;
import java.util.HashMap;
class Solution {
    public int[] twoSum(int[] nums, int target) {
      if (nums == null) {
            throw new IllegalArgumentException("The argument cannot be null");
        } else if (nums.length <= 1) {
            throw new IllegalArgumentException("The argument nums[] contains invalid data");
        } else {
            HashMap<Integer, Integer> map = new HashMap<>();
            for (int i = 0; i < nums.length; i++) {
                if (map.containsKey(nums[i])) {
                    return new int[] { map.get(nums[i]), i };
                } else {
                    map.put(target - nums[i], i);
                }

            }
        }
        return new int[] { -1, -1 };
    }
}