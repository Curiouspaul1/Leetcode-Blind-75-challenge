using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    public class Data_Structures_and_Algorithms
    {

        public static int[] MaximumNum(int[] nums, int target)
        {
            var numsDictionary = new Dictionary<int, int>();

            int complement = 0;
            for (int i = 0; i < nums.Count(); i++)
            {
                complement = target - nums[i];
                int index = 0;
                if (numsDictionary.TryGetValue(complement, out index))
                {
                    int[] twoSumSolution = { index, i };
                    return twoSumSolution;
                }

                if (!numsDictionary.ContainsKey(nums[i]))
                {
                    numsDictionary.Add(nums[i], i);
                }
            }

            return null;
        }
    }
}