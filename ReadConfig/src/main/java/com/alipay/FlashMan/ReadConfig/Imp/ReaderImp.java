package com.alipay.FlashMan.ReadConfig.Imp;

import com.alipay.FlashMan.ReadConfig.Interface.Reader;
import com.alipay.FlashMan.ReadConfig.Utils.ConfigResults;
import com.alipay.FlashMan.ReadConfig.Utils.Logger;
import com.alipay.FlashMan.ReadConfig.Utils.Node;
import org.dom4j.Document;
import org.dom4j.DocumentException;
import org.dom4j.Element;
import org.dom4j.io.SAXReader;

import java.io.File;
import java.util.Iterator;

/**
 * Created by damon_lin on 15/5/25.
 */

/**
 * read the xml config file
 * @param Filename
 */
public class ReaderImp implements Reader {
    public ConfigResults readConfig(String Filename) {
        SAXReader reader = new SAXReader();
        Node root = new Node();
        try {
            Document document = reader.read(new File(Filename));
            Element element = document.getRootElement();
            root.name = (element.getName());
            root.value = (element.attributeValue("name"));
            dp_search(element, 0, root);
            Logger.println("read config complete");
        } catch (DocumentException e) {
            e.printStackTrace();
        }
        return new ConfigResults(root); //wrapped result
    }

    // deep first search
    public void dp_search(Element element, int cnt, Node node) {
        cnt++;
        for (Iterator it = element.elementIterator(); it.hasNext(); ) {
            Element e = (Element) it.next();
            Node child = new Node();
            node.childs.add(child);
            child.parent = node;
            if (e.attributeValue("name") != null) {
                child.name = e.getName();  // get name of this attr
                child.value = e.attributeValue("name");  //get value of this name attr
                Logger.println(reapetStr("  ", cnt) + e.getName() + " ");
                Logger.println(e.attributeValue("name"));
            } else {
                child.name = e.getName();  // get name of this attr
                child.value = e.getText();
                Logger.println(reapetStr("  ", cnt) + e.getName() + " ");
            }

            if (e.elementIterator().hasNext()) {  // next level deep in
                dp_search(e, cnt, child);
            }
        }
    }


    public String reapetStr(String str, int cnt) {
        for (int i = 0; i < cnt; i++) {
            str += str;
        }
        return str;
    }
}
