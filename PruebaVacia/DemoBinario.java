package primero;
import java.io.*;

public class DemoBinario {
public static void main(String[] args) throws IOException {
FileOutputStream fos = new FileOutputStream("datos.bin");
fos.close();

FileInputStream fis = new FileInputStream("datos.bin");

int b;
while ((b = fis.read()) != -1) {
System.out.println("Byte leído: " + b + " -> " + (char) b);
}
fis.close();
}
}
