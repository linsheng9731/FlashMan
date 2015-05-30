package com.alipay.FlashMan.ReadConfig.Interface;

import com.alipay.FlashMan.ReadConfig.Utils.ConfigResults;

/**
 * Created by damon_lin on 15/5/25.
 */
public interface Generator {
    /**
     * generate code by templates
     * @param results
     */
    public void generateCode(ConfigResults results,String configPath);
}
