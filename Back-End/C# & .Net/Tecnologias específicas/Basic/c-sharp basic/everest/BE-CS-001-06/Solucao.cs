public class Solution
{
    public static string[] SoletrandoStr(string input)
    {
        string[] soletrar = new string[input.Length];
        for (var i = 0; i < input.Length; i++)
        {
            soletrar[i] = input[i].ToString();
        }

        return soletrar;
    }
}