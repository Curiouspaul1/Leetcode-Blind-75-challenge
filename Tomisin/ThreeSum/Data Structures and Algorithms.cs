using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    public class Data_Structures_and_Algorithms
    {

        public static IList<IList<int>> threeSumClose(int[] nums)
        {
            int target = 0;
            IList<IList<int>> triplets = new List<IList<int>>();
            HashSet<string> keys = new HashSet<string>(); // -1, 0, 1 -> key string" "-1,0,1,"

            if (nums == null || nums.Length == 0)
                return triplets;

            Array.Sort(nums);

            int len = nums.Length;

            for (int i = 0; i < len - 2; i++)  // len = 3, test case passes! 
            {
                int[] trialTriplet = new int[3];
                trialTriplet[0] = nums[i];

                // call two sum function 
                int newTarget = target - trialTriplet[0];
                int head = i + 1;
                int tail = len - 1;

                while (head < tail)
                {
                    trialTriplet[1] = nums[head];
                    trialTriplet[2] = nums[tail];

                    int twoSumValue = trialTriplet[1] + trialTriplet[2];

                    if (twoSumValue == newTarget)   // newTarget, not target 
                    {
                        // check if the key is in key hashset or not, 
                        // if yes, then skip it; otherwise, add it to result 
                        string key = getKey(trialTriplet, 3);

                        if (!keys.Contains(key))
                        {
                            keys.Add(key);

                            IList<int> triplet = new List<int>();

                            for (int j = 0; j < 3; j++)
                                triplet.Add(trialTriplet[j]);

                            triplets.Add(triplet);
                        }

                        // continue to search 
                        head++;
                        tail--;

                    }
                    else if (twoSumValue > newTarget)
                    {
                        tail--;
                    }
                    else if (twoSumValue < newTarget)
                    {
                        head++;
                    }
                }
            }

            return triplets;
        }

        private static string getKey(int[] arr, int len)
        {
            string key = "";

            for (int j = 0; j < 3; j++)
            {
                key += arr[j].ToString();
                key += ",";
            }

            return key;
        }
    }
}