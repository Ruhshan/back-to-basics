import java.util.ArrayList;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;

class MyHashTable{
    private List<LinkedList<KeyValuePair>> lol;
    
    public MyHashTable(){
        this.lol = new ArrayList<>(26);
        for(int i=0;i<26;i++){
            lol.add(i,null);
        }
    }

    public void insert(String key, String value){
        int i = this.getIndex(key);

    
        if(lol.get(i)==null){
            KeyValuePair kvp = new KeyValuePair(key, value);
            LinkedList<KeyValuePair> ll = new LinkedList<>();
            ll.add(kvp);
            lol.add(i, ll);
        }
        else{
            KeyValuePair kvp = new KeyValuePair(key, value);
            var ll = lol.get(i);
            ll.add(kvp);
        }
    
    }

    public String getValue(String key){
        int index = this.getIndex(key);
        var ll = this.lol.get(index);

        if(ll!=null){
            Iterator<KeyValuePair> itr = ll.iterator();
            
            while(itr.hasNext()){
                KeyValuePair keyValuePair = itr.next();

                if(keyValuePair.getKey().equals(key)){
                    return keyValuePair.getValue();
                }
            }

            return null;
        }

        return null;


    }



    private int getIndex(String key){
        return (int)key.charAt(0)-97;
    }
}