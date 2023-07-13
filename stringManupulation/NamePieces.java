package stringManupulation;

import java.util.LinkedList;
import java.util.List;

public class NamePieces{
    public List<String> breakdown(String s){
        // System.out.println("okjss");
        List<String> l = new LinkedList<>();
        for (int i=s.length();i >0; i--){
            l.add(s.substring(0,i));
            System.out.println(s.substring(0,i));
        }
        return l;
    }
}