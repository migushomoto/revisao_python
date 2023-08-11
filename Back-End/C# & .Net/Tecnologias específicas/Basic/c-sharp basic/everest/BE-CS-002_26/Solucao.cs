public class Imovel
{
    public Imovel(bool estaAVenda, double preco)
    {
        Preco = estaAVenda ? preco : 0;
        EstaAVenda = estaAVenda;
    }

    public double Preco { get; set; }
    public bool EstaAVenda { get; set; }

    public double PrecoDeVenda(double comissao)
    {
        if (!EstaAVenda)
        {
            return 0;
        }

        return Preco + comissao;
    }
}

public class ImovelSeminovo : Imovel
{
    public ImovelSeminovo(bool estaAVenda, double preco, double desconto) : base(estaAVenda, preco)
    {
        Desconto = desconto;
    }

    public double Desconto { get; set; }

    public double PrecoDeVenda(double comissao)
    {
        if (!EstaAVenda)
        {
            return 0;
        }

        if (Desconto > Preco + comissao)
        {
            return 0;
        }

        return Preco + comissao - Desconto;
    }
}

