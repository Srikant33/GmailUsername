package stringManupulation;

import java.util.ArrayList;
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
    if (s.length()>5){
        res.add(s);
    }
    // System.out.println(res);
    
    List<List<String>> llCopy = new ArrayList<>(ll); // Create a copy of ll
    
    for (List<String> l : llCopy) {
        for (String str : l) {
            int i = ll.indexOf(l);
            String temp = str;
            
            ll.remove(l);
            res = combos(ll, s + temp, res);
            ll.add(i, l);
        }
    }
    
    return res;
}

}