public class Solution
{
    public static double CustoCompra(int input)
    {
        var valorQuantidadeMenor10 = 1.25;
        var valorQuantidadeMaior10 = 1.45;

        if (input > 10)
            return input * valorQuantidadeMenor10;
        else
            return input * valorQuantidadeMaior10;
    }
}