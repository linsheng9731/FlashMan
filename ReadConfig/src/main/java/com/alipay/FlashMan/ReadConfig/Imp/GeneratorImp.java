package com.alipay.FlashMan.ReadConfig.Imp;

import com.alipay.FlashMan.ReadConfig.Interface.Generator;
import com.alipay.FlashMan.ReadConfig.Utils.ConfigResults;
import com.alipay.FlashMan.ReadConfig.Utils.Logger;
import com.alipay.FlashMan.ReadConfig.Utils.Node;
import org.apache.velocity.Template;
import org.apache.velocity.VelocityContext;
import org.apache.velocity.app.Velocity;

import java.io.File;
import java.io.FileWriter;
import java.util.*;


/**
 * Created by damon_lin on 15/5/25.
 */
public class GeneratorImp implements Generator {

    // the flag used to mark the root node
    private boolean flag = true;
    // the flag used to mark first time iterate
    private boolean first = true;
    // the flag used to mark last one item
    private boolean last = false;
    // the app's name
    private String project = "";

    /**
     * generate code by templates
     *
     * @param results
     */
    public void generateCode(ConfigResults results, String configPath) {
        try {
            Velocity.init(configPath); // specific the dir of properties file
            this.project = results.root.value;
            File targetDir = new File("./" + this.project);
            if (!targetDir.exists()) {
                targetDir.mkdir();
            }
            File initFile = new File("./" + this.project + "/__init__.py");
            if (!initFile.exists())
                initFile.createNewFile();
            int cnt =0 ;
            for (Node n : results.root.childs) {
                List<Map> models = new ArrayList<Map>();
                dp_iter(n, models);
                cnt++;
                if (cnt==results.root.childs.size()){
                    this.last = true;
                }

                generateViews(n, models);
                generateModels(models);
                generateUrls(models);

                first = false;
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // generate urls code
    private void generateUrls(List<Map> models) throws Exception {
        VelocityContext context = new VelocityContext();
        flag = true;
        context.put("models", models);
        context.put("project", this.project);
        Template template = null;
        File urlsFile = new File("./" + this.project + "/" + "urls.py");
        if (first) {
            template = Velocity.getTemplate("urls.vm");
            if (urlsFile.exists()) {
                urlsFile.delete();
                urlsFile.createNewFile();
            }
        } else {
            template = Velocity.getTemplate("urls_body.vm");
        }
        FileWriter writer = new FileWriter(urlsFile, true);
        template.merge(context, writer);
        if (last)
            writer.append(']');
        writer.flush();
        writer.close();
        Logger.println(writer.toString());
    }

    /**
     * generate models code
     *
     * @param models
     */
    private void generateModels(List<Map> models) throws Exception {
        VelocityContext context = new VelocityContext();
        flag = true;
        Collections.reverse(models); // the dp_search add node reverse
        context.put("models", models);
        context.put("project", "ECommunity");
        Template template = null;
        File modelsFile = new File("./" + this.project + "/models.py");
        if (first) {
            modelsFile.delete();
            modelsFile = new File("./" + this.project + "/models.py");
            template = Velocity.getTemplate("models.vm");
        } else {
            template = Velocity.getTemplate("models_body.vm");
        }

        FileWriter writer = new FileWriter(modelsFile, true);
        template.merge(context, writer);
        writer.flush();
        writer.close();
        Logger.println(writer.toString());
    }

    /**
     * generate views code
     *
     * @param models
     */
    private void generateViews(Node n, List<Map> models) throws Exception {
        VelocityContext context = new VelocityContext();
        flag = true;
        context.put("models", models);
        context.put("project", this.project);
        Template template = Velocity.getTemplate("views.vm");
        FileWriter writer = new FileWriter(new File("./" + this.project + "/" + n.value + "_view.py"));
        template.merge(context, writer);
        writer.flush();
        writer.close();
        Logger.println(writer.toString());
    }

    /**
     * deep first iterate
     *
     * @param models
     */
    public void dp_iter(Node root, List<Map> models) {
        LinkedHashMap model = new LinkedHashMap();
        if (root.name != null) {
            if (flag) {
                model.put("father", "true");
                flag = false;
            }
            model.put("name", root.value);  //record model
        }
        List attrs = new ArrayList();
        for (Node n : root.childs) {
            Logger.println(n.name + ":" + n.value);

            if (n.childs.size() > 0) {
                dp_iter(n, models);  // has childs deep in; a model
            } else {  // has none childs; a attr
                attrs.add(n.value);  //record attr
            }
        }
        if (attrs.size() > 0) {
            model.put("attrs", attrs);
            models.add(model);
        }


    }
}
