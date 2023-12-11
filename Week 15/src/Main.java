import school.Student;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        testStudent();
    }

    private static void testStudent() {
        Student student1 = new Student(1, "Alice", 100);
        Student student2 = new Student(2, "Bob", 100);
        Student student3 = new Student(3, "Charlie", 100);
        Student student4 = new Student(4, "Diana", 100);
        Student student5 = new Student(5, "Ethan", 100);
        System.out.println(Student.listAll());
        System.out.println(Student.averageAllowance());
        System.out.println(Student.remove(3));
        System.out.println(Student.listAll());
        Student.sort();
        System.out.println(Student.listAll());
        System.out.println("Search for id = " + student1 + ": [" + Arrays.binarySearch(Student.all,student1) + "]");



        /*
    1) create a public class "Student" in package "school" having 3 private non-static fields:
       "id" (int,final), "name" (String), "allowance" (double).
    1.1) create setters for all non-static fields except "id",
         and getters for all non-static fields.
    1.2) @Override the "equals" and "hashCode" methods using only the "id" of Student.
    1.3) @Override the "toString" method to return a String in this format:
         "Student(id,'name',allowance)".
    1.4) implement Comparable<Student> for Student by comparing only the "id" of Student.
    1.5) add 2 private static fields: "all" (of Student array type) to store
         all Students created and "count" (of int type) to count
         the number of Students stored in the array.
    1.6) create a constructor that receives 3 parameters: "id", "name", "allowance"
         to initialize the 3 fields if a Student object can be created.
         A Student object can be created if "name" is not null,
         "allowance" is more than zero, "id" is not negative,
         and the "id" is not already in the Student array ("all").
         If a Student can be created, put it in the array "all" and increment the "count".
        Note that if "all" is null, create an array of size 2 first.
        If "all" is full, double its size.
        If a Student cannot be created, throws an IllegalArgumentException.
    1.7) create a public static method named "averagaAllowance" that receives no argument and
        returns the average allowance of "all" Student.  This method returns a negative value
        if "all" is null or there is no Student in "all".
    1.8) create a public static method named "remove" that receives an int (named "id").
        This method removes the Student with id equals to "id" from "all" and return that Student.
        This method returns null if "all" is null or there is no Student with that id in the array.
        When removing a Student from the array, move that last element in the array to replace
        the Student that is removed and decrement the "count".
    1.9) create a public static void method named "sort" to sort the array.
    1.10) create a public static method named "listAll" to return a String containing
          all Students in "all" separated by "; ".
    */
    }
}
