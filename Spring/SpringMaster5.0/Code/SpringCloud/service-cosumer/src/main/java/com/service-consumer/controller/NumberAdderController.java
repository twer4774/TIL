import java.util.List;

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.netflix.hystrix.contrib.javanica.annotation.HystrixCommand;


@RestController
public class NumberAdderController {

    private Log log = LogFactory.getLog(NumberAdderController.class);


     @Value("${number.service.url}")
     private String numberServiceUrl;

     //실패시 getDefaultResponse 호출
    @HystrixCommand(fallbackMethod = "getDefaultResponse")
    @RequestMapping("/add")
    public Long add() {
        long sum = 0;

        ResponseEntity<Integer[]> responseEntity = new RestTemplate()
                .getForEntity(numberServiceUrl, Integer[].class);

        Intger[] numbers = responseEntity.getBody();

        for (int number : numbers) {
            sum += number;
        }

        log.warn("Returning " + sum);

        return sum;
    }

    public Long getDefaultResponse() {
        return 10000L;
    }

}