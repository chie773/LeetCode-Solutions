class LongestConsecutive {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> newTable = new HashSet<>();

        for (int i=0; i < nums.length; i++) {
            newTable.add(nums[i]); //This happens in constant time? I think?
        }
        if (nums.length < 1) {
            return 0;
        }

        int count = 0;
        int max = 1;

        for (int j = 0; j < nums.length; j++) {
            /* Basically, I need to see nums[j] - 1 exists. If so, then I need to move to the next question
               If it doesn't, I need to start counting and looking for the next digit in nums[j] + 1 subsequence
             */

            if (newTable.contains(nums[j] - 1)) { // if the number - 1 doesn't exist. i.e. if nums[j] = 100, does 99 exist?
                //Since it doesn't exist --->
                // This doesn't work for some reason, why?
                //^ This works now, stupid sets
            }
            else{
                count = 1;
                while (newTable.contains(count + nums[j])) {
                    count++;
                }
                if (count > max) {
                    max = count;
                }
            }


        }









        return max;
    }
}
