import com.alipay.FlashMan.ReadConfig.Imp.GeneratorImp;
import com.alipay.FlashMan.ReadConfig.Interface.Generator;
import com.alipay.FlashMan.ReadConfig.Utils.ConfigResults;
import com.alipay.FlashMan.ReadConfig.Imp.ReaderImp;
import com.alipay.FlashMan.ReadConfig.Interface.Reader;
/**
 * Created by damon_lin on 15/5/25.
 */
public class Tester {
    public static void main(String args[]){
        System.out.println("main start--------");

        Reader reader = new ReaderImp();
        ConfigResults r = reader.readConfig("/Users/damon_lin/Documents/test.xml");

        Generator generator = new GeneratorImp();
        generator.generateCode(r,"/Users/damon_lin/Documents/SVN/FlashMan/ReadConfig/src/velocity.properties");

        System.out.println("main end-----------");
    }
}
