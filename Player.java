package the_player;
import java.util.ArrayList;
public interface Player { 
    int stats[] = new int[10];
    int effects[] = new int[5];
    ArrayList<String> options = new ArrayList<>();
    String passive = new String();
    String activated = new String();
    boolean fence_set = false;
    boolean alive = true;
    void damage(int amount);
    void heal(int amount);
    void next_turn();
}