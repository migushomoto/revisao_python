public class Solution
{
    public static string ParEImpar(params int[] input)
    {
        int pares = 0;
        int impares = 0;
        for (var i = 0; i < input.Length; i++)
        {
            if (input[i] % 2 == 0)
                pares++;
            else
                impares++;
        }

        return $"{pares} pares, {impares} ímpares";
    }
}