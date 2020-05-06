

class HashTableBasic{

    public static void main(String args[]){

        MyHashTable ht = new MyHashTable();

        ht.insert("zy", "value");
        ht.insert("zx", "talue");
        
        
        System.out.println(ht.getValue("zx"));

    }
}