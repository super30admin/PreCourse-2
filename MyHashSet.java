import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class MyHashSet {
    private final int MAX_VALUE = 1000000;
    private final int MAX_RANGE = 100;
    private List<List<Integer>> parentList;

    public MyHashSet() {
        parentList = new ArrayList<>(MAX_RANGE);
        for (int i = 0; i < MAX_RANGE; i++) {
            parentList.add(null);
        }
    }

    public void add(int key) {
        int index = key % MAX_RANGE;
        List<Integer> childlist = parentList.get(index);
        if (childlist == null) {
            List<Integer> list = new LinkedList<>();
            list.add(key);
            parentList.set(index, list);
        } else {
            if (!childlist.contains(key)) {
                childlist.add(key);
            }
        }
    }

    public void remove(int key) {
        int index = key % MAX_RANGE;
        List<Integer> childlist = parentList.get(index);
        if (childlist != null) {
            childlist.remove(Integer.valueOf(key));
        }
    }

    public boolean contains(int key) {
        int index = key % MAX_RANGE;
        List<Integer> childList = parentList.get(index);
        return childList != null && childList.contains(key);
    }

}