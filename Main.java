import java.util.LinkedList;

import stringManupulation.*;

import java.util.*;


public class Main {
    public static void main(String[] args) {
        String name = "Kasiviswanathan Srikant Iyer";
        name.toLowerCase();
        

        String[] parts= name.split(" ");
        LinkedList<List<String>> ll= new LinkedList<>(); 
        NamePieces np = new NamePieces();
        for (String s: parts){
            List<String> l= np.breakdown(s);
            ll.add(l);
        }
        Names names = new Names();
        List<String> possible= names.nameCombos(ll);
        System.out.println(possible);
    }
}