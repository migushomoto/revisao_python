using Xunit;

public class UnitTest
{
    [Fact]
    public void TestImoveis__obtem_preco_imovel_a_venda_esperado_preco()
    {
        double preco = 200000.0;
        Imovel i = new Imovel(true, preco);
        double comissao = preco * 0.01;
        Assert.True(i.EstaAVenda);
        Assert.Equal(preco + comissao, i.PrecoDeVenda(comissao));
    }

    [Fact]
    public void TestImoveis__obtem_preco_imovel_nao_a_venda_esperado_preco_zero()
    {
        Imovel i = new Imovel(false, 200000.0);
        Assert.False(i.EstaAVenda);
        Assert.Equal(0, i.Preco);
        Assert.Equal(0, i.PrecoDeVenda(1000.0));
    }

    [Fact]
    public void TestImoveis__cria_imovel_seminovo_nao_a_venda_esperado_imovel_criado()
    {
        ImovelSeminovo i = new ImovelSeminovo(false, 200000.0, 20000.0);
        Assert.False(i.EstaAVenda);
        Assert.Equal(0, i.Preco);
    }

    [Fact]
    public void TestImoveis__cria_imovel_seminovo_a_venda_esperado_imovel_criado()
    {
        ImovelSeminovo i = new ImovelSeminovo(true, 200000.0, 20000.0);
        Assert.True(i.EstaAVenda);
        Assert.Equal(200000.0, i.Preco);
    }

    [Fact]
    public void TestImoveis__obtem_preco_imovel_seminovo_a_venda_esperado_preco()
    {
        double preco = 200000.0;
        double desconto = 20000.0;
        ImovelSeminovo i = new ImovelSeminovo(true, preco, desconto);
        double comissao = preco * 0.01;
        Assert.True(i.EstaAVenda);
        Assert.Equal(preco + comissao - desconto, i.PrecoDeVenda(comissao));
    }

    [Fact]
    public void TestImoveis__obtem_preco_imovel_seminovo_nao_a_venda_esperado_preco_zero()
    {
        ImovelSeminovo i = new ImovelSeminovo(false, 200000.0, 20000.0);
        Assert.False(i.EstaAVenda);
        Assert.Equal(0, i.Preco);
        Assert.Equal(0, i.PrecoDeVenda(1000.0));
    }

    [Fact]
    public void TestImoveis__obtem_preco_imovel_desconto_maior_que_preco_de_venda__esperado_preco_zero()
    {
        double preco = 200000.0;
        double desconto = 210000.0;
        ImovelSeminovo i = new ImovelSeminovo(true, preco, desconto);
        double comissao = preco * 0.01;
        Assert.True(i.EstaAVenda);
        Assert.Equal(0, i.PrecoDeVenda(comissao));
    }
}