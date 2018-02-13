import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;
import java.lang.StringBuilder;

public class InputGenerator { 
    public static void main(String[] args) throws IOException { 
        long start = System.currentTimeMillis();
        // Parameters
        int n = 2, m = 1;
        int maxA = 100;
        File file = new File("input.txt");

        file.createNewFile();
        FileWriter writer = new FileWriter(file);

        // Line 1
        Random rn = new Random();
        writer.write(Integer.toString(n) + " " + Integer.toString(m) + "\n");
        
        // Line 2
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i < (1<<n); i++) {
            sb.append(Integer.toString(rn.nextInt(maxA) + 1));
            sb.append(" ");
        }
        sb.append(Integer.toString(rn.nextInt(maxA) + 1));
        sb.append("\n");
        writer.write(sb.toString());

        // Line 3
        sb.setLength(0);
        for (int i = 1; i < m; i++) {
            sb.append(Integer.toString(rn.nextInt(n+1)));
            sb.append(" ");
        }
        sb.append(Integer.toString(rn.nextInt(n+1)));
        sb.append("\n");
        writer.write(sb.toString());

        writer.flush();
        writer.close();
        long end = System.currentTimeMillis();
        System.out.println((end - start) / 1000f + " seconds");
    }
}
