package com.alipay.FlashMan.ReadConfig.Utils;

/**
 * Created by damon_lin on 15/5/25.
 */
public class ConfigResults {

    // the root of the tree
    public Node root;
    // the total level of this tree
    public int height=0;

    public  ConfigResults(Node root){
            this.root = root;
    }

}

