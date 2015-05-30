package com.alipay.FlashMan.ReadConfig.Utils;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by damon_lin on 15/5/25.
 */
public class Node{

    // the name of this node
    public String name;
    // the value of this node
    public String value;
    // the parent node of this node
    public Node parent;
    // the childs node of this node
    public List<Node> childs = new ArrayList<Node>();
    // the brother nodes of this node
    public List<Node> brothers = new ArrayList<Node>();


}