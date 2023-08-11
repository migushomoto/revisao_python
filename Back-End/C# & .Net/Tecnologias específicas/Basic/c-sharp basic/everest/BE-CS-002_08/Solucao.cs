public class Vestuario
{
    public Vestuario() { }
    public Vestuario(string tamanho)
    {
        this.Tamanho = tamanho;
    }
    public Vestuario(string tamanho, string cor)
    {
        this.Tamanho = tamanho;
        this.Cor = cor;
    }

    public string Tamanho { get; set; }
    public string Cor { get; set; }

    public string info()
    {
        return $"{this.Tamanho}_{this.Cor}";
    }
}

public class Solution
{
    public static string solution(string tamanho, string cor)
    {
        var v1 = new Vestuario();
        var v2 = new Vestuario(tamanho);
        var v3 = new Vestuario(tamanho, cor);
        return $"{v1.info()}|{v2.info()}|{v3.info()}";
    }
}