package school;

import java.util.Arrays;
import java.util.Objects;
import java.util.StringJoiner;

public class Student implements Comparable<Student> {
    private final int id;
    private String name;
    private double allowance;
    public static Student[] all;
    private static int count;


    public Student(int id, String name, double allowance) {
        if (all == null) {
            all = new Student[2];
        } else if (count == all.length) {
            all = Arrays.copyOf(all, all.length * 2);
        } else if (id <= 0 && name == null && allowance < 0) {
            throw new IllegalArgumentException();
        }
        for (int i = 0; i < count; i++) {
            if (id == all[i].id) {
                throw new IllegalArgumentException();
            }
        }
        this.id = id;
        this.name = name;
        this.allowance = allowance;
        all[count] = this;
        count++;
    }

    public static double averageAllowance() {
        if (count == 0) {
            return -1;
        }
        double average = 0;
        for (int i = 0; i < count; i++) {
            average += all[i].allowance;
        }
        return average / count;
    }

    public static Student remove(int i) {
        for (int z = 0; z < count; z++) {
            if (all[z].id == i) {
                var temp = all[z];
                all[z] = all[count - 1];
                all[count - 1] = null;
                count--;
                return temp;
            }
        }
        return null;
    }

    public static void sort() {
        Arrays.sort(all,0,count);
    }

    public static String listAll() {
        StringJoiner sj = new StringJoiner(", ", "School [", "]");
        for (int i = 0; i < count; i++) {
            sj.add(all[i].toString());
        }
        return sj.toString();
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setAllowance(double allowance) {
        this.allowance = allowance;
    }

    public int getId() {
        return this.id;
    }

    public String getName() {
        return this.name;
    }

    public double getAllowance() {
        return this.allowance;
    }

    @Override
    public String toString() {
        return String.format("Student (id = %d ,name = %s ,allowance = %.2f)", this.id, this.name, this.allowance);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Student student)) return false;
        return id == student.id;
    }

    @Override
    public int hashCode() {
        return Objects.hash(id);
    }

    @Override
    public int compareTo(Student o) {
        return this.id - o.id;
    }
}
