public class Solution
{
    public static string calcularAreaLivre(double larguraTerreno, double comprimentoTerreno, double larguraCasa, double comprimentoCasa)
    {
        var areaTerreno = larguraTerreno * comprimentoTerreno;
        var areaCasa = larguraCasa * comprimentoCasa;
        var areaLivre = areaTerreno - areaCasa;
        var porcentagem = 100 - ((areaLivre * 100) / areaTerreno);

        return $"{areaLivre:#.00} m2 | {porcentagem:#.00} %";
    }
}