import utilOchi.Tool051;
import valuableOchi.Container051;
import valuableOchi.Item051;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
//        testTool051();
        testItem051();
//        testContainer();
    }

    private static void testContainer() {
        Container051 c = new Container051();
        Item051 i = Item051.create("Naruedom",10);
        Item051 a = Item051.create("Monkey",8);
        c.add(i);
        c.add(a);
        c.remove(a);
        System.out.println(c);
    }

    private static void testItem051() {
        System.out.println("<<< testItem051 >>>");
        System.out.println("---- 2.1 - 2.4 ----");
        Item051 i = Item051.create("Naruedom",10);
        Item051 ii = Item051.create("Ochi",20);
        System.out.println(ii);
        System.out.println(i);
        System.out.println("---- 2.5 ----");
        System.out.println(i.add(ii));
        System.out.println("---- 2.6 ----");
        System.out.println(i.isMatched(ii));
    }

    private static void testTool051() {
        System.out.println("<<< testTool051 >>>");
        Object [] num = {10,20,30};
        System.out.println("---- 1.1 ----");
        System.out.println(Tool051.isUsable051(""));
        System.out.println("---- 1.2 ----");
        System.out.println(Tool051.isUsable051(num));
        System.out.println("---- 1.3 ----");
        System.out.println(Tool051.count051(num));
    }
}
