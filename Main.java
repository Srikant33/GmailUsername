import stringManupulation.*;

import java.util.*;

import java.io.FileWriter;
import java.io.IOException;


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
        
        // System.out.println(possible);
        try (FileWriter writer = new FileWriter("output.txt")) {
            for (String str : possible) {
                writer.write(str + System.lineSeparator()); // Write each string to a new line
            }
            // writer.write(possible);
            System.out.println("Result saved to file.");
        } catch (IOException e) {
            System.out.println("An error occurred while writing to the file.");
            e.printStackTrace();
        }

    }
}


