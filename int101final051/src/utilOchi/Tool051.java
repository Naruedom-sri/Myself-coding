package utilOchi;

public final class Tool051 {
    private Tool051() {

    }

    public static boolean isUsable051(String s) {
        if (s == null || s.isBlank()) {
            return false;
        }
        return true;
    }

    public static boolean isUsable051(Object[] o) {
        if (o != null && o.length > 0) {
            return true;
        }
        return false;
    }

    public static int count051(Object[] o) {
        if (!isUsable051(o)) {
            return -1;
        }
        int count = 0;
        for (int i = 0; i < o.length; i++) {
            if (o[i] != null) {
                count++;
            }
        }
        return count;
    }
}
