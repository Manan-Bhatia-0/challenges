// min number of insertions required to make a string a palindrome

public class minimumInsertions {
    public static int minInsertions(String s) {
        return solution(s, 0, s.length() - 1);
    }

    public static int solution(String s, int first, int last) {
        if (first > last || first == last)
            return 0;
        if (s.charAt(first) == s.charAt(last)) {
            return solution(s, first + 1, last - 1);
        } else {
            return (Integer.min(solution(s, first, last - 1), solution(s, first + 1, last)) + 1);
        }
    }

    public static void main(String[] args) {
        System.out.println(minInsertions("bobbb"));
    }
}
