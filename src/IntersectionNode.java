// Find the intersection of two linked lists

public class IntersectionNode {


    private static class ListNode {
        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
            next = null;
        }
    }

    public static ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) {
            return null;
        }
        // if intersection exists:
        ListNode tempA = headA;
        int sizeA = 0;
        while (tempA != null) {
            sizeA++;
            tempA = tempA.next;
        }
        ListNode tempB = headB;
        int sizeB = 0;
        while (tempB != null) {
            sizeB++;
            tempB = tempB.next;
        }
        tempA = headA;
        tempB = headB;
        if (sizeA < sizeB) {
            int diff = sizeB - sizeA;
            for (int i = 0; i < diff; i++) {
                tempB = tempB.next;
            }
        }
        if (sizeB < sizeA) {
            int diff = sizeA - sizeB;
            for (int i = 0; i < diff; i++) {
                tempA = tempA.next;
            }
        }
        if (tempA.equals(tempB)) {
            return tempA;
        }
        while (tempA != null) {
            if (tempA.next == null || tempB.next == null) {
                return null;
            }
            if (tempA.next.equals(tempB.next)) {
                return tempA.next;
            }
            tempA = tempA.next;
            tempB = tempB.next;
        }

        return null;
    }


    public static void main(String[] args) {
        ListNode headA = new ListNode(4);
        headA.next = new ListNode(1);
        headA.next.next = new ListNode(8);
        ListNode headB = new ListNode(4);
        headB.next = new ListNode(5);
        headB.next.next = new ListNode(6);
        headB.next.next.next = new ListNode(1);

        //intersection begins:
        headB.next.next.next.next = headA.next.next;
        headA.next.next.next = new ListNode(4);
        headA.next.next.next.next = new ListNode(5);
        ListNode intersection = getIntersectionNode(headA, headB);
        if (intersection == null) {
            System.out.println("No intersection\n");
        }
        else {
            System.out.printf("Intersection at: %d\n", intersection.val);
        }

    }
}
