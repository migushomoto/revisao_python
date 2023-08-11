using System.Collections.Generic;
using System.Linq;
public class Solution
{
    public static List<int> ordenaLista(List<int> lista)
    {
        return lista.OrderBy(x => x).ToList();
    }
}