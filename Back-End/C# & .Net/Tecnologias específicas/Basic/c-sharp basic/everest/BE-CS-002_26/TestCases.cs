using Xunit;

public class UnitTest
{
    [Fact]
    public void TestImoveis__cria_imovel_nao_a_venda_esperado_imovel_criado()
    {
        Imovel i = new Imovel(false, 200000.0);
        Assert.False(i.EstaAVenda);
        Assert.Equal(0, i.Preco);
    }

    [Fact]
    public void TestImoveis__cria_imovel_a_venda_esperado_imovel_criado()
    {
        Imovel i = new Imovel(true, 200000.0);
        Assert.True(i.EstaAVenda);
        Assert.Equal(200000.0, i.Preco);
    }
}

