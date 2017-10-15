from framework.Classes import Testcase

java_source_code_with_input = """
                import java.util.*;
                
                class Solution{
                    public static void main(String... args) {
                        Scanner scan = new Scanner(System.in);
                        int sum = scan.nextInt() + scan.nextInt();
                        System.out.println(sum);
                    }
                }
             """

java_source_code_with_no_input = """
                class Solution{
                    public static void main(String... args) {
                        System.out.println("Hello World");
                    }
                }
             """

java_source_code_with_exception = """
                class Solution{
                    public static void main(String... args) {
                        throw new RuntimeException();
                    }
                }
             """

java_source_code_with_compile_error = """
                class Solution{
                    public static void main(String... args) {
                        int a
                    }
                }
             """

tc1 = Testcase()
tc1.id = "1"
tc1.input = "23 34"
tc1.timeout = 1

tc2 = Testcase()
tc2.id = "2"
tc2.input = "21 34"
tc2.timeout = 1