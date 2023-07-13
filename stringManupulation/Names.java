package stringManupulation;

import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

public class Names{
    public List<String> nameCombos(List<List<String>> ll){
        List<String> res = new LinkedList<>();
        combos(ll, "", res);
        Collections.sort(res, (a,b)-> a.length()-b.length());
        System.out.println(res);
        return res;
    }

    public List<String> combos(List<List<String>> ll, String s, List<String> res) {
        res.add(s);
        System.out.println(res.size());
        for (List<String> l : ll){
            for (String str: l){
                ll.remove(l);
                res = combos(ll, s+str, res);
                ll.add(l);
            }
        }
        return res;
    }
}