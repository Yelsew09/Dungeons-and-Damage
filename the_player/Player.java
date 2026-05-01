package the_player;
import java.util.ArrayList;
public class Player {
    int stats[];
    int effects[];
    ArrayList<String> options;
    String passive;
    String activated;
    boolean fence_set;
    boolean alive;
    Player(){

    }
    void damage(int amount){
        stats[0] -= amount;
        if (stats[0] <= 0){
            alive = false;
        }
    }
    void heal(int amount){
        stats[0] += amount;
        if (stats[0] > stats[1]){
            stats[0] = stats[1];
        }
    }
    void next_turn(){}
}