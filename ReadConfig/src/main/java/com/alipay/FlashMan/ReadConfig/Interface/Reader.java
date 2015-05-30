/**
 * Created by damon_lin on 15/5/25.
 */
package com.alipay.FlashMan.ReadConfig.Interface;
import com.alipay.FlashMan.ReadConfig.Utils.ConfigResults;

public interface Reader {

    /**
     * read xml config file
     */
    public ConfigResults readConfig(String filename);
}
