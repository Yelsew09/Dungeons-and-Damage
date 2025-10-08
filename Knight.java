package the_player;
public class Knight implements Player{
    public Knight(int s[]){
        stats = s;
    }
    @Override
    public void heal(int amount){
        stats[0] += amount;
        if (stats[0] > stats[1]){
            stats[0] = stats[1];
        }
    }
    @Override
    public void damage(int amount){
        amount -= 2;
        stats[0] -= amount;
        if (stats[0] <= 0){
            alive = false;
        }
    }
    @Override
    public void next_turn(){
        if (effects[1] > 0){
            effects[1]--;
            if (effects[1] == 0){
                effects[0] = 0;
            }
        }
    }
}