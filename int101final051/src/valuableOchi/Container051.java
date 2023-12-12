package valuableOchi;

import utilOchi.Tool051;

import java.util.Arrays;

public class Container051 {
    private final Item051[] item = new Item051[051];
    private int count;

    public boolean add(Item051 item) {
        if (this.count == this.item.length) {
            return false;
        }
        for (int i = 0; i < this.item.length; i++) {
            if (this.item[i] == item) {
                this.item[i] = item;
            }
        }
        this.item[count] = item;
        this.count++;
        return true;
    }

    public boolean remove(Item051 item) {
        for (int i = 0; i < this.item.length; i++) {
            if (item == this.item[i]) {
                this.item[i] = null;
                return true;
            }
        }
        return false;
    }

    @Override
    public String toString() {
        return "Container051 {" + "item = " + Arrays.toString(this.item) + ", count = " + Tool051.count051(this.item) + "}";
    }
}
