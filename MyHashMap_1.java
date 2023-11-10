public class MyHashMap_1 {

    class Node {

        int key;
        int val;
        Node next;

        public  Node(int key, int val) {
            this.key = key;
            this.val = val;

        }
    }

    Node[] storage;
    int buckets;

    public MyHashMap_1() {
        this.buckets = 10000;
        this.storage = new Node[buckets];
    }

    private int hash(int key) {
        return key % buckets;

    }

    private Node find(Node head, int key) {
        Node pre = null;
        Node curr = head;
        while (curr != null && curr.key != key) {
            pre = curr;
            curr = curr.next;
        }
        return pre;

    }

    public void put(int key, int value) {
        int bucket = hash(key);
        if (storage[bucket] == null) {
            storage[bucket] = new Node (-1, -1);
        }
        Node pre = find(storage[bucket], key);
        if (pre.next == null) {
            pre.next = new Node(key, value);
        } else {
            pre.next.val = value;
        }

    }

    public void remove(int key) {
        int bucket = hash(key);
        if (storage[bucket] == null)
            return;
        Node pre = find(storage[bucket], key);
        if (pre.next == null)
            return;
        pre.next = pre.next.next;

    }

    public int get(int key) {
        int bucket = hash(key);
        if (storage[bucket] == null)
            return -1;
        Node pre = find(storage[bucket], key);
        if (pre.next == null)
            return -1;
        return pre.next.val;

    }
}