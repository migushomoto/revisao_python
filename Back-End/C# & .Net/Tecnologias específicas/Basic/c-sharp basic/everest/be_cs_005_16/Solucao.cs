public class Solution
{
    public static int somaVetor(int[] vetor)
    {
        int soma = 0;
        for (var i = 0; i < vetor.Length; i++)
            soma += vetor[i];

        return soma;
    }
}