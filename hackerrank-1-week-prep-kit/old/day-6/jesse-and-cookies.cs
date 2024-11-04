using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;

class Result
{

    /*
     * Complete the 'cookies' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER k
     *  2. INTEGER_ARRAY A
     */

    public static int cookies(int k, List<int> A)
    {
        return cookiesHelper(k, A, 0);
    }

    private static int cookiesHelper(int k, List<int> A, int count)
    {
        if (A.Count < 2) return -1;

        int minA = A.Min();
        if (minA >= k)
        {
            return count;
        }

        A.Remove(minA);
        int minB = A.Min();
        A.Remove(minB);

        A.Add(minA + 2 * minB);
        return cookiesHelper(k, A, count + 1);
    }
}

class Solution
{
    public static void Main(string[] args)
    {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        string[] firstMultipleInput = Console.ReadLine().TrimEnd().Split(' ');

        int n = Convert.ToInt32(firstMultipleInput[0]);

        int k = Convert.ToInt32(firstMultipleInput[1]);

        List<int> A = Console.ReadLine().TrimEnd().Split(' ').ToList().Select(ATemp => Convert.ToInt32(ATemp)).ToList();

        int result = Result.cookies(k, A);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}